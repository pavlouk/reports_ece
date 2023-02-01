using DualCamera;
using Flir.Atlas.Gigevision;
using Flir.Atlas.Gigevision.Remote;
using Flir.Atlas.Gigevision.Streaming;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Windows.Forms;

namespace GigeVisionSample
{
    public partial class MainWindow : Form
    {
        readonly Timer TimerRefreshUi = new Timer();
        GigeVisionThermalCamera gigeVisionCamera;

        public MainWindow()
        {
            InitializeComponent();

            TimerRefreshUi.Interval = 20;
            TimerRefreshUi.Tick += TimerRefreshUi_Tick;
        }

        private void TimerRefreshUi_Tick(object sender, EventArgs e)
        {
            toolStripStatusLabelSystemRunning.Text = elapsedTimeConnected.Elapsed.ToString();

            if (!refreshUi)
                return;

            refreshUi = false;

            toolStripFps.Text = fps.ToString("F01");
            toolStripFrameCounter.Text = gigeVisionCamera.Stream.FramesReceived.ToString();

            var th = gigeVisionCamera.ThermalStream.GetThermalImage();
            if (th == null)
                return;

            try
            {
                th.EnterLock();

                if (pictureBoxThermal.Image != null)
                    pictureBoxThermal.Image.Dispose();

                pictureBoxThermal.Image = th.Image;
            }
            catch (Exception ex)
            {

                Trace.Write(ex.Message);
            }
            finally
            {
                th.ExitLock();
            }

        }

        private void connectToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var discovery = new DiscoveryDialog();
            if (discovery.ShowDialog() == DialogResult.OK)
            {
                Connect(discovery.SelectedCamera);
            }
        }

        bool refreshUi;
        Stopwatch elapsedTimeConnected = new Stopwatch();

        bool isInitializing;
        async void Connect(GigeVisionDevice gigeVisionDevice)
        {
            BeginInvoke((Action)(() => toolStripConnectionStatus.Text = "Connecting"));

            isInitializing = true;

            gigeVisionCamera = new GigeVisionThermalCamera();
            var stream = gigeVisionCamera.ThermalStream;
            stream.ThermalFrameReceived += Stream_ThermalFrameReceived;
            var error = await gigeVisionCamera.Connect(gigeVisionDevice.IpAddress);

            elapsedTimeConnected.Reset();

            if (error == GigeVisionError.OK)
            {
                elapsedTimeConnected.Start();
                stream.StartGrabbing();
                BeginInvoke((Action)(() =>
                {
                    toolStripConnectionStatus.Text = "Connected";

                    error = gigeVisionCamera.ThermalRemoteControl.FocusControl.GetPosition(out int pos);
                    if (error == GigeVisionError.OK)
                        textBoxFocusPos.Text = pos.ToString();

                    error = gigeVisionCamera.ThermalRemoteControl.FocusControl.GetDistance(out float distance);
                    if (error == GigeVisionError.OK)
                        textBoxFocusDist.Text = distance.ToString();

                    error = gigeVisionCamera.ThermalRemoteControl.CameraControl.GetNucMode(out NucMode nucMode);
                    if (error == GigeVisionError.OK)
                        comboBoxNucMode.SelectedIndex = (int)nucMode;

                    error = gigeVisionCamera.ThermalRemoteControl.FocusControl.GetSpeed(out int speed);
                    if (error == GigeVisionError.OK)
                        textBoxFocusSpeed.Text = speed.ToString();

                    if (gigeVisionCamera.ThermalRemoteControl.CameraControl.GetTemperatureRanges(out List<TemperatureRange> ranges) == GigeVisionError.OK)
                    {
                        comboBoxTempRanges.Tag = ranges;
                        foreach (var item in ranges)
                        {
                            comboBoxTempRanges.Items.Add(string.Format("Min {0:F} - Max {1:F}", item.Min, item.Max));
                        }

                        if (gigeVisionCamera.ThermalRemoteControl.CameraControl.GetSelectedTemperatureIndex(out int selectedIndex) == GigeVisionError.OK)
                        {
                            for (int i = 0; i < ranges.Count; i++)
                            {
                                if (ranges[i].Index == selectedIndex)
                                {
                                    comboBoxTempRanges.SelectedIndex = i;
                                    break;
                                }
                            }
                        }
                    }

                    isInitializing = false;
                    groupBoxCameraControl.Enabled = true;
                    groupBoxFocusControls.Enabled = true;
                    TimerRefreshUi.Start();
                }));
            }
            else
            {
                stream.ThermalFrameReceived -= Stream_ThermalFrameReceived;
                gigeVisionCamera.Dispose();
                gigeVisionCamera = null;
                BeginInvoke((Action)(() => MessageBox.Show("Failed to connect", "Error", MessageBoxButtons.OK)));
                isInitializing = false;
            }
        }

        double fps;
        private void Stream_ThermalFrameReceived(object sender, ThermalFrameReceivedEventArgs e)
        {
            fps = gigeVisionCamera.ThermalStream.Fps;
            refreshUi = true;
        }

        void Clear()
        {
            if (gigeVisionCamera != null)
            {
                gigeVisionCamera.ThermalStream.StopGrabbing();
                gigeVisionCamera.Disconnect();
                gigeVisionCamera.Dispose();
                gigeVisionCamera = null;
            }
        }

        void Disconnect()
        {
            toolStripConnectionStatus.Text = "Disconnecting";
            groupBoxCameraControl.Enabled = false;
            groupBoxFocusControls.Enabled = false;
            TimerRefreshUi.Stop();
            Clear();
            toolStripConnectionStatus.Text = "Disconnected";
        }

        private void disconnectToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Disconnect();
        }

        private void MainWindow_FormClosing(object sender, FormClosingEventArgs e)
        {

            Disconnect();
        }

        private void buttonFocusSet_Click(object sender, EventArgs e)
        {
            if (int.TryParse(textBoxFocusPos.Text, out int pos))
            {
                gigeVisionCamera.ThermalRemoteControl.FocusControl.SetPosition(pos);
            }
        }

        private void buttonFocusDist_Click(object sender, EventArgs e)
        {
            if (float.TryParse(textBoxFocusDist.Text, out float focusDist))
            {
                gigeVisionCamera.ThermalRemoteControl.FocusControl.SetDistance(focusDist);
            }
        }

        private void buttonFocusSpeed_Click(object sender, EventArgs e)
        {
            if (int.TryParse(textBoxFocusSpeed.Text, out int speed))
            {
                gigeVisionCamera.ThermalRemoteControl.FocusControl.SetSpeed(speed);
            }
        }

        private void comboBoxNucMode_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (isInitializing)
                return;

            var mode = (NucMode)comboBoxNucMode.SelectedIndex;
            gigeVisionCamera.ThermalRemoteControl.CameraControl.SetNucMode(mode);
        }

        private void buttonNuc_Click(object sender, EventArgs e)
        {
            gigeVisionCamera.ThermalRemoteControl.CameraControl.Nuc();
        }

        private void buttonFocusFar_MouseDown(object sender, MouseEventArgs e)
        {
            gigeVisionCamera.ThermalRemoteControl.FocusControl.SetFocusDirection(FocusDirection.Far);
        }

        private void buttonFocusFar_MouseUp(object sender, MouseEventArgs e)
        {
            gigeVisionCamera.ThermalRemoteControl.FocusControl.SetFocusDirection(FocusDirection.Stop);
        }

        private void buttonFocusNear_MouseDown(object sender, MouseEventArgs e)
        {
            gigeVisionCamera.ThermalRemoteControl.FocusControl.SetFocusDirection(FocusDirection.Near);
        }

        private void buttonFocusNear_MouseUp(object sender, MouseEventArgs e)
        {
            gigeVisionCamera.ThermalRemoteControl.FocusControl.SetFocusDirection(FocusDirection.Stop);
        }

        private void buttonFocusAuto_Click(object sender, EventArgs e)
        {
            gigeVisionCamera.ThermalRemoteControl.FocusControl.AutoFocus();
        }

        private void comboBoxTempRanges_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (isInitializing)
                return;

            List<TemperatureRange> ranges = (List<TemperatureRange>)comboBoxTempRanges.Tag;
            if (ranges != null)
            {
                var index = comboBoxTempRanges.SelectedIndex;
                var range = ranges[index];
                gigeVisionCamera.ThermalRemoteControl.CameraControl.SelectTemperatureRange(range);
            }
        }

        private void MainWindow_Load(object sender, EventArgs e)
        {
            groupBoxCameraControl.Enabled = false;
            groupBoxFocusControls.Enabled = false;
        }
    }
}
