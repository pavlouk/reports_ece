using System;
using System.Windows.Forms;
using Flir.Atlas.Gigevision;
using Thermal_Camera;

namespace DualCamera
{
    public partial class DiscoveryDialog : Form
    {
        GigeVisionScanner gigeVisionScanner;

        public DiscoveryDialog()
        {
            InitializeComponent();
        }

        private void DiscoveryDialog_Load(object sender, EventArgs e)
        {
            PopulateDevices();
        }

        private void buttonRefresh_Click(object sender, EventArgs e)
        {
            PopulateDevices();
        }

        async void PopulateDevices()
        {
            if (gigeVisionScanner == null)
                gigeVisionScanner = new GigeVisionScanner();

            var devices = await gigeVisionScanner.Scan();

            BeginInvoke((Action)(() =>
            {
                listViewDevices.Items.Clear();
                foreach (var item in devices)
                {
                    var lvItem = new ListViewItem(new string[] { item.Name, item.IpAddress, item.DeviceId })
                    {
                        Tag = item
                    };
                    listViewDevices.Items.Add(lvItem);
                }
            }));
        }

        public GigeVisionDevice SelectedCamera { get; set; }

        private void DiscoveryDialog_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (gigeVisionScanner != null)
            {
                gigeVisionScanner.Dispose();
            }
        }

        void ShowStaticIpDialog()
        {
            var dlg = new StaticIpDialog();
            if (dlg.ShowDialog() == DialogResult.OK)
            {
                SelectedCamera = new GigeVisionDevice() { IpAddress = dlg.Ip };
                DialogResult = DialogResult.OK;
                Close();
            }
        }

        private void staticIPToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ShowStaticIpDialog();
        }

        private void listViewDevices_MouseDoubleClick_1(object sender, MouseEventArgs e)
        {
            var items = listViewDevices.SelectedItems;
            if (items.Count > 0)
            {
                var lv = items[0];

                SelectedCamera = (GigeVisionDevice)lv.Tag;

                DialogResult = DialogResult.OK;
                Close();
            }
        }
    }
}
