using DualCamera;
using Flir.Atlas.Image;
using Flir.Atlas.Live.Device;
using Flir.Atlas.Live.Discovery;
using Flir.Atlas.Live.Log;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Thermal_Camera
{
    public partial class MainWindow : Form
    {
        readonly Timer TimerRefreshUi = new Timer();
        Camera Camera { get; set; }

        PerformanceMonitor performanceMonitor;

        ImageBase GetImage()
        {
            if (Camera != null)
                return Camera.GetImage();
            return null;
        }

        public MainWindow()
        {
            InitializeComponent();

            TimerRefreshUi.Interval = 10;
            TimerRefreshUi.Tick += TimerRefreshUi_Tick;

            LogWriter.Instance.Updated += Instance_Updated;

            performanceMonitor = new PerformanceMonitor();
            performanceMonitor.Updated += PerformanceMonitor_Updated;
            performanceMonitor.Start(Process.GetCurrentProcess());
        }

        private void PerformanceMonitor_Updated(object sender, EventArgs e)
        {
            labelSystemCpu.Text = performanceMonitor.Cpu;
            labelSystemMemory.Text = performanceMonitor.WorkingSet64;
        }

        private void Instance_Updated(object sender, LogEventArgs e)
        {
            BeginInvoke((Action)(() => UpdateLog(e.Message)));
        }

        void UpdateLog(LogMessage entry)
        {
            if (listBoxLogger.Items.Count > 1000)
            {
                listBoxLogger.Items.Clear();
            }
            listBoxLogger.Items.Insert(0, string.Format("{0} {1}\t{2}", entry.LogDate, entry.LogTime, entry.Message));
        }

        private void TimerRefreshUi_Tick(object sender, EventArgs e)
        {
            if (!refreshUi || !isInitialized)
                return;

            refreshUi = false;

            try
            {
                RefreshUi();
            }
            catch (Exception ex)
            {
                Trace.Write(ex.Message);
            }

        }

        ImageOverlay overlay;
        void RefreshUi()
        {
            if (Camera != null)
            {
                toolStripFps.Text = string.Format("{0:G3}", Camera.Fps);
                toolStripFrameCounter.Text = string.Format("{0}", Camera.FrameCount);
                toolStripLostImages.Text = string.Format("{0}", Camera.LostImages);
            }

            var image = GetImage();

            if (image != null)
            {
                if (pictureBoxThermal.Image != null)
                {
                    pictureBoxThermal.Image.Dispose();
                }
                try
                {
                    image.EnterLock();
                    var img = image.Image;

                    using (var graphics = Graphics.FromImage(img))
                    {
                        if (overlay == null)
                        {
                            overlay = new ImageOverlay(img.Width);
                        }

                        if (image is ThermalImage thermalImage)
                        {
                            overlay.Draw(graphics, thermalImage);
                        }
                        overlay.Draw(graphics, fpsLoadData);
                    }

                    pictureBoxThermal.Image = img;
                }
                catch (Exception ex)
                {
                    Debug.Write(ex.Message);
                }
                finally
                {
                    image.ExitLock();
                }
            }
            if (Camera is DualStreamingThermalCamera dualStreamingThermalCamera)
            {
                dualStreamingThermalCamera.Visual.EnterLock();
                try
                {
                    if (pictureBoxVisualImage.Image != null)
                        pictureBoxVisualImage.Image.Dispose();
                    pictureBoxVisualImage.Image = dualStreamingThermalCamera.Visual.Image;
                }
                finally
                {
                    dualStreamingThermalCamera.Visual.ExitLock();
                }
            }
            labelSystemRunning.Text = elapsedTime.Elapsed.ToString();
        }

        private void discoveryToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Disconnect();
            DiscoveryDialog ddialog = ShowDiscovery();

            if (ddialog.SelectedCameraDevice != null)
            {
                Connect(ddialog.SelectedCameraDevice, ddialog.AuthenticatedCamera);
            }
        }

        Stopwatch elapsedTime = new Stopwatch();
        void Connect(CameraDeviceInfo camera, bool authenticated)
        {
            try
            {
                Disconnect();

                isInitialized = false;

                if (pictureBoxVisualImage.Image != null)
                    pictureBoxVisualImage.Image.Dispose();
                pictureBoxVisualImage.Image = null;

                if (pictureBoxThermal.Image != null)
                    pictureBoxThermal.Image.Dispose();
                pictureBoxThermal.Image = null;

                switch (camera.SelectedStreamingFormat)
                {
                    case ImageFormat.FlirFileFormat:
                        Camera = new ThermalCamera();
                        break;
                    case ImageFormat.Argb:
                        Camera = new VideoOverlayCamera();
                        break;
                    case ImageFormat.Dual:
                        Camera = new DualStreamingThermalCamera(true, DualStreamingFormat.Fusion);
                        break;
                    case ImageFormat.Unknown:
                    default:
                        MessageBox.Show("Unsupported camera format: " + camera.SelectedStreamingFormat.ToString());
                        break;
                }
                Camera.DeviceError += ThermalCamera_DeviceError;
                Camera.ConnectionStatusChanged += ThermalCamera_ConnectionStatusChanged;
                Camera.ImageReceived += ThermalCamera_ImageReceived;
                Camera.ImageInitialized += ThermalCamera_ImageInitialized;

                Camera.Connect(camera, authenticated ? new Flir.Atlas.Live.Security.SecurityParameters() : null);

                cameraControl1.SetCamera(Camera);

                var dateTimeNow = DateTime.Now;
                labelSystemStarted.Text = dateTimeNow.ToString();

                TimerRefreshUi.Start();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                Disconnect();
            }
        }

        bool isInitialized;
        private void ThermalCamera_ImageInitialized(object sender, EventArgs e)
        {
            BeginInvoke((Action)(() =>
            {
                var image = GetImage();
                if (image == null)
                    return;
                image.EnterLock();
                try
                {
                    UpdateCameraInformation(image);
                    if (image is ThermalImage thermalImage)
                    {
                        thermalImage.Scale.IsAutoAdjustEnabled = true;
                    }
                }
                finally
                {
                    image.ExitLock();
                }
                isInitialized = true;
            }));

            Trace.WriteLine("Initialized");
        }

        void UpdateCameraInformation(ImageBase image)
        {
            try
            {
                labelCamInfoSize.Text = string.Format("{0} x {1}", image.Width, image.Height);
                if (Camera.CameraDeviceInfo.IpSettings != null)
                {
                    labelCamInfoIp.Text = Camera.CameraDeviceInfo.IpSettings.IpAddress;
                }
                else
                {
                    labelCamInfoIp.Text = "N/A";
                }
                labelCamInfoName.Text = Camera.CameraDeviceInfo.Name;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        void Disconnect()
        {
            TimerRefreshUi.Stop();
            if (Camera != null)
            {
                cameraControl1.SetCamera(null);
                Camera.DeviceError -= ThermalCamera_DeviceError;
                Camera.ConnectionStatusChanged -= ThermalCamera_ConnectionStatusChanged;
                Camera.ImageReceived -= ThermalCamera_ImageReceived;
                Camera.ImageInitialized -= ThermalCamera_ImageInitialized;
                Camera.StopGrabbing();
                Camera.Disconnect();
                Camera.Dispose();
                Camera = null;
            }
            BeginInvoke((Action)(() => toolStripConnectionStatus.Text = ConnectionStatus.Disconnected.ToString()));
        }

        bool refreshUi;

        double fpsLoadData = 0.0;
        readonly Stopwatch stopwatchFps = new Stopwatch();
        int frameCounterFps = 0;
        private void ThermalCamera_ImageReceived(object sender, ImageReceivedEventArgs e)
        {
            if (isLoadDisabled)
                return;

            if ((Camera.FrameCount % skipFrames) != 0)
            {
                return;
            }

            frameCounterFps++;
            if (stopwatchFps.IsRunning)
            {
                if (stopwatchFps.ElapsedMilliseconds >= 3000)
                {
                    fpsLoadData = frameCounterFps * 1000.0 / stopwatchFps.ElapsedMilliseconds;
                    frameCounterFps = 0;
                    stopwatchFps.Restart();
                }
            }
            else
            {
                stopwatchFps.Start();
            }

            refreshUi = true;
        }

        private void ThermalCamera_ConnectionStatusChanged(object sender, Flir.Atlas.Live.ConnectionStatusChangedEventArgs e)
        {
            BeginInvoke((Action)(() => toolStripConnectionStatus.Text = e.Status.ToString()));

            if (e.Status == ConnectionStatus.Connected)
            {
                elapsedTime.Start();
            }
            else if (elapsedTime.IsRunning)
            {
                elapsedTime.Stop();
            }
        }

        private void ThermalCamera_DeviceError(object sender, DeviceErrorEventArgs e)
        {
            BeginInvoke((Action)(() => ShowError(e.ErrorMessage)));
        }

        private void ShowError(string message)
        {
            toolStripStatusLabel5.Text = message;
        }

        private void MainWindow_Load(object sender, EventArgs e)
        {
            Text = "Thermal Camera Sample, running Atlas version: " + ImageBase.Version;
        }

        static DiscoveryDialog ShowDiscovery()
        {
            
            var dlg = new DiscoveryDialog();
            if (dlg.ShowDialog() == DialogResult.OK)
            {
                return dlg;
            }
            return null;
        }

        private void MainWindow_FormClosing(object sender, FormClosingEventArgs e)
        {
            
            Disconnect();

            LogWriter.Instance.Updated -= Instance_Updated;

            performanceMonitor.Stop();
        }

        private void disconnectToolStripMenuItem_Click(object sender, EventArgs e)
        {

            Disconnect();
        }

        
        bool isLoadDisabled;
        int skipFrames = 1;
        private void highestToolStripMenuItem_Click(object sender, EventArgs e)
        {
            skipFrames = 1;
            isLoadDisabled = false;
        }

        private void halfToolStripMenuItem_Click(object sender, EventArgs e)
        {
            skipFrames = 2;
            isLoadDisabled = false;
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            skipFrames = 3;
            isLoadDisabled = false;
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            skipFrames = 4;
            isLoadDisabled = false;
        }

        private void disableToolStripMenuItem_Click(object sender, EventArgs e)
        {
            isLoadDisabled = true;
            fpsLoadData = 0.0;
            refreshUi = true;
        }

        private void addCenterRectangleToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var image = GetImage();

            if (image != null)
            {
                image.EnterLock();
                try
                {
                    if (image is ThermalImage thermalImage)
                    {
                        thermalImage.Measurements.Add(new Rectangle(image.Width / 4, image.Height / 4, image.Width / 2, image.Height / 2));
                    }
                }
                finally
                {
                    image.ExitLock();
                }
            }
        }
    }
}
