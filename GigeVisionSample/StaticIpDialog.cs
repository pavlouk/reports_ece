using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Thermal_Camera
{
    public partial class StaticIpDialog : Form
    {
        public StaticIpDialog()
        {
            InitializeComponent();

            textBoxIpAddress.Text = "169.254.";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Ip = textBoxIpAddress.Text;
            DialogResult = DialogResult.OK;
            Close();
        }

        public string Ip { set; get; }

    }
}
