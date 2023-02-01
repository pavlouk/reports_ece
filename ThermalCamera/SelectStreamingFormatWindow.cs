using Flir.Atlas.Live.Discovery;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DrValidate
{
    public partial class SelectStreamingFormatWindow : Form
    {
        public SelectStreamingFormatWindow(List<ImageFormat> formats)
        {
            InitializeComponent();
            Formats = formats;
        }

        public List<ImageFormat> Formats { get; }

        private void SelectStreamingFormatWindow_Load(object sender, EventArgs e)
        {
            if (Formats == null)
                return;

            foreach (var item in Formats)
            {
                listBox1.Items.Add(item.ToString());
            }
        }

        private void listBox1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            if (listBox1.SelectedIndex >= 0)
            {
                SelectedFormat = (ImageFormat)Enum.Parse(typeof(ImageFormat), listBox1.SelectedItem.ToString());
                DialogResult = DialogResult.OK;
            }
            else
            {
                DialogResult = DialogResult.Cancel;
            }
            Close();
        }

        public ImageFormat SelectedFormat { get; set; }
    }
}
