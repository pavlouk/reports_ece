using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Flir.Atlas.Live.Device;
using System.Globalization;
using Flir.Atlas.Live.Remote;

namespace Thermal_Camera
{
    public partial class CameraControl : UserControl
    {
        private const NumberStyles StyleDouble = NumberStyles.AllowDecimalPoint | NumberStyles.AllowThousands | NumberStyles.AllowLeadingSign;

        private Camera _camera;

        public CameraControl()
        {
            InitializeComponent();
        }

        public void SetCamera(Camera camera)
        {
            groupBoxFocus.Enabled = false;
            buttonNuc.Enabled = false;
            if (_camera != null)
            {
                _camera.ConnectionStatusChanged -= _camera_ConnectionStatusChanged;
                _camera = null;
            }
            if (camera != null)
            {
                _camera = camera;
                _camera.ConnectionStatusChanged += _camera_ConnectionStatusChanged;
                BeginInvoke(((Action)(() => UpdateButtons(_camera.ConnectionStatus))));
            }
        }

        private void UpdateButtons(ConnectionStatus connectionStatus)
        {
            if (connectionStatus == ConnectionStatus.Connected)
            {
                buttonNuc.Enabled = _camera.RemoteControl.CameraSettings.IsShutterSupported();

                if (_camera.RemoteControl.Focus.IsSupported())
                {
                    groupBoxFocus.Enabled = true;
                }
                else
                {
                    groupBoxFocus.Enabled = false;
                }
            }
        }

        void _camera_ConnectionStatusChanged(object sender, Flir.Atlas.Live.ConnectionStatusChangedEventArgs e)
        {
            BeginInvoke(((Action)(() => UpdateButtons(e.Status))));
        }

        private void buttonFocusNear_MouseDown(object sender, MouseEventArgs e)
        {
            if (_camera != null)
            {
                _camera.RemoteControl.Focus.Mode(FocusMode.Near);
            }
        }

        private void buttonFocusNear_MouseUp(object sender, MouseEventArgs e)
        {
            if (_camera != null)
            {
                _camera.RemoteControl.Focus.Mode(FocusMode.Stop);
            }
        }

        private void buttonFocusFar_MouseDown(object sender, MouseEventArgs e)
        {
            if (_camera != null)
            {
                _camera.RemoteControl.Focus.Mode(FocusMode.Far);
            }
        }

        private void buttonFocusFar_MouseUp(object sender, MouseEventArgs e)
        {
            if (_camera != null)
            {
                _camera.RemoteControl.Focus.Mode(FocusMode.Stop);
            }
        }

        private void buttonFocusAuto_Click(object sender, EventArgs e)
        {
            if (_camera != null)
            {
                _camera.RemoteControl.Focus.Mode(FocusMode.Auto);
            }
        }

        private void buttonNuc_Click_1(object sender, EventArgs e)
        {
            if (_camera != null)
                _camera.RemoteControl.CameraAction.Nuc();
        }

        private void CameraControl_Load(object sender, EventArgs e)
        {
            groupBoxFocus.Enabled = false;
            buttonNuc.Enabled = false;
        }
    }
}
