using Flir.Atlas.Image;
using Flir.Atlas.Image.Measurements;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Thermal_Camera
{
    public class ImageOverlay
    {
        protected Font _textFont;
        protected Font _textFontBig;
        protected Pen _pen = Pens.White;
        protected Brush _textBrush = Brushes.White;

        public ImageOverlay(int width)
        {
            Width = width;
            _textFont = new Font(FontFamily.GenericSansSerif, Gain * 5);
            _textFontBig = new Font(FontFamily.GenericSansSerif, Gain * 10);
        }

        public float Gain { get { return Math.Max(1.0f, Width / 320.0f); } }
        public int Width { get; }

        public void Draw(System.Drawing.Graphics graphics, ThermalImage thermalImage)
        {
            if (graphics == null)
            {
                throw new ArgumentNullException(nameof(graphics));
            }

            foreach (MeasurementRectangle rectangle in thermalImage.Measurements.MeasurementRectangles)
            {
                DrawArea(rectangle, graphics);
            }
        }

        public void Draw(Graphics graphics, double fps)
        {
            var y = 20;
            var x = 20;
            var str = string.Format("Fps {0:G3}", fps);
            graphics.DrawString(str, _textFontBig, _textBrush, x, y);
        }

        private void DrawArea(MeasurementRectangle rectangle, System.Drawing.Graphics graphics)
        {
            Rectangle rect = new Rectangle(rectangle.Location.X, rectangle.Location.Y, rectangle.Width, rectangle.Height);
            graphics.DrawRectangle(_pen, rect);

            var strMin = "Min " + rectangle.Min.Value.ToString("F01");
            if (rectangle.Min.State != ThermalValueState.Ok)
                strMin += "*";

            var strMax = "Max " + rectangle.Max.Value.ToString("F01");
            if (rectangle.Max.State != ThermalValueState.Ok)
                strMax += "*";

            var strAvg = "Avg " + rectangle.Average.Value.ToString("F01");
            if (rectangle.Average.State != ThermalValueState.Ok)
                strAvg += "*";

            var str = strMin + " - " + strMax + " - " + strAvg;

            var y = rect.Y - Gain * 20;
            if (y < 0)
                y = rect.Y + Gain * 20;

            graphics.DrawString(str, _textFontBig, _textBrush, rectangle.Location.X, y);
        }
    }
}
