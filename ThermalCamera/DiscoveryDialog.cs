using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Windows.Forms;
using DrValidate;
using Flir.Atlas.Live.Device;
using Flir.Atlas.Live.Discovery;
using Flir.Atlas.Live.Security;
using Thermal_Camera;

namespace DualCamera
{
    public partial class DiscoveryDialog : Form
    {
        private ThermalCameraScanner scanner;

        public DiscoveryDialog()
        {
            InitializeComponent();
        }

        private void DiscoveryDialog_Load(object sender, EventArgs e)
        {
            scanner = new ThermalCameraScanner();
            scanner.DeviceFound += Scanner_DeviceFound;
            scanner.DeviceLost += Scanner_DeviceLost;
            scanner.Start(Interface.Default);
        }

        private void Scanner_DeviceLost(object sender, CameraLostEventArgs e)
        {
            BeginInvoke((Action)(() => OnDeviceLost()));
        }

        private void Scanner_DeviceFound(object sender, CameraDiscoveredEventArgs e)
        {
            BeginInvoke((Action)(() => OnDeviceFound(e.Device)));
        }

        void OnDeviceFound(DeviceIdentifier deviceIdentifier)
        {
            var lvi = new ListViewItem(string.Format("{0}", deviceIdentifier.Name));
            lvi.SubItems.Add(deviceIdentifier.DeviceId);
            lvi.SubItems.Add(deviceIdentifier.Interface.ToString());
            lvi.Tag = deviceIdentifier;

            listViewDevices.Items.Add(lvi);
        }

        void OnDeviceLost()
        {
            listViewDevices.Items.Clear();
            PopulateListView();
        }

        void PopulateListView()
        {
            foreach (var item in scanner.Cameras)
            {
                var lvi = new ListViewItem(string.Format("{0}", item.Name));
                lvi.SubItems.Add(item.DeviceId);
                lvi.SubItems.Add(item.Interface.ToString());
                lvi.Tag = item;

                listViewDevices.Items.Add(lvi);
            }
        }

        private void RemoveDevice(CameraDeviceInfo cameraDeviceInfo)
        {
            foreach (ListViewItem item in listViewDevices.Items)
            {
                var device = item.Tag as CameraDeviceInfo;
                if (device != null && device.DeviceIdentifier == cameraDeviceInfo.DeviceIdentifier)
                {
                    listViewDevices.Items.Remove(item);
                }
            }
        }

        public CameraDeviceInfo SelectedCameraDevice { get; set; }

        public bool AuthenticatedCamera { get; set; }

        private void DiscoveryDialog_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (scanner != null)
            {
                scanner.DeviceFound -= Scanner_DeviceFound;
                scanner.DeviceLost -= Scanner_DeviceLost;
                scanner.Stop();
                scanner.Dispose();
                scanner = null;
            }
        }

        private void networkCameraToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ShowStaticIpDialog(Interface.Network);
        }

        private void gigeVisionCameraToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ShowStaticIpDialog(Interface.Spinnaker);
        }

        void ShowStaticIpDialog(Interface adapter)
        {
            var dlg = new StaticIpDialog();
            AuthenticatedCamera = checkBoxAuthenticate.Checked;
            if (dlg.ShowDialog() == DialogResult.OK)
            {
                var di = new DeviceIdentifier();

                di.Source = dlg.Ip;
                di.Interface = adapter;
                var sp = new SecurityParameters();

                var status = ThermalCameraScanner.Resolve(di, checkBoxAuthenticate.Checked ? new SecurityParameters() : null, out CameraDeviceInfo cameraDeviceInfo);
                if (status != AuthenticationStatus.Approved)
                {
                    MessageBox.Show("Authentication response: " + status.ToString());
                    return;
                }
                if (cameraDeviceInfo == null)
                {
                    MessageBox.Show("Couldn't resolve camera");
                    return;
                }
                SelectedCameraDevice = cameraDeviceInfo;

                if (SelectedCameraDevice.StreamingFormats != null && SelectedCameraDevice.StreamingFormats.Count >= 1)
                {
                    if (SelectedCameraDevice.StreamingFormats.Count >= 2)
                    {
                        var selectStreamingFormat = new SelectStreamingFormatWindow(SelectedCameraDevice.StreamingFormats);
                        if (selectStreamingFormat.ShowDialog() == DialogResult.OK)
                        {
                            SelectedCameraDevice.SelectedStreamingFormat = selectStreamingFormat.SelectedFormat;
                            DialogResult = DialogResult.OK;
                            Close();
                        }
                    }
                    else
                    {
                        SelectedCameraDevice.SelectedStreamingFormat = SelectedCameraDevice.StreamingFormats[0];
                        DialogResult = DialogResult.OK;
                        Close();
                    }
                }
                else
                {
                    MessageBox.Show("The selected camera doesn't support any streaming formats");
                }
            }
        }

        private void listViewDevices_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            var items = listViewDevices.SelectedItems;
            if (items.Count > 0)
            {
                var lv = items[0];
                DeviceIdentifier di = (DeviceIdentifier)lv.Tag;

                AuthenticatedCamera = checkBoxAuthenticate.Checked;
                var status = ThermalCameraScanner.Resolve(di, checkBoxAuthenticate.Checked ? new SecurityParameters() : null, out CameraDeviceInfo cameraDeviceInfo);
                if (status != AuthenticationStatus.Approved)
                {
                    MessageBox.Show("Authentication response: " + status.ToString());
                    return;
                }
                if (cameraDeviceInfo == null)
                {
                    MessageBox.Show("Couldn't resolve camera");
                    return;
                }
                SelectedCameraDevice = cameraDeviceInfo;

                if (SelectedCameraDevice.StreamingFormats != null && SelectedCameraDevice.StreamingFormats.Count >= 1)
                {
                    if (SelectedCameraDevice.StreamingFormats.Count >= 2)
                    {
                        var selectStreamingFormat = new SelectStreamingFormatWindow(SelectedCameraDevice.StreamingFormats);
                        if (selectStreamingFormat.ShowDialog() == DialogResult.OK)
                        {
                            SelectedCameraDevice.SelectedStreamingFormat = selectStreamingFormat.SelectedFormat;
                            DialogResult = DialogResult.OK;
                            Close();
                        }
                    }
                    else
                    {
                        SelectedCameraDevice.SelectedStreamingFormat = SelectedCameraDevice.StreamingFormats[0];
                        DialogResult = DialogResult.OK;
                        Close();
                    }
                }
                else
                {
                    MessageBox.Show("The selected camera doesn't support any streaming formats");
                }

            }
        }

        private void checkBoxScanGige_CheckedChanged(object sender, EventArgs e)
        {
            scanner.Stop();
            listViewDevices.Items.Clear();
            scanner.Start(GetScanFlags());
        }

        private void checkBoxEbus_CheckedChanged(object sender, EventArgs e)
        {
            scanner.Stop();
            listViewDevices.Items.Clear();
            scanner.Start(GetScanFlags());
        }

        Interface GetScanFlags()
        {
            var interfaces = Interface.Default;
            if (checkBoxScanGige.Checked)
                interfaces |= Interface.Spinnaker;
            if (checkBoxEbus.Checked)
                interfaces |= Interface.Gigabit;
            return interfaces;
        }
    }
}
