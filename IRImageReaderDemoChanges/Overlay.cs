using Flir.Atlas.Image;
using Flir.Atlas.Image.Measurements;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text;

namespace IRImageApplication
{
    public class Overlay
    {
        #region Construction

        public Overlay(ThermalImageFile image)
        {
            _image = image;

            Color color = Color.White;
            Color semiTransparentColor = Color.FromArgb(128, color.R, color.G, color.B);
            _transparentBrush = new SolidBrush(semiTransparentColor);
            _textFont = new Font(FontFamily.GenericSansSerif, 9);
        }
        #endregion

        #region Public methods

        public void Draw(Graphics graphics)
        {
            foreach (MeasurementSpot spot in _image.Measurements.MeasurementSpots)
            {
                DrawSpot(spot, graphics);
            }
            foreach (MeasurementRectangle rectangle in _image.Measurements.MeasurementRectangles)
            {
                DrawAdiposeArea(rectangle, graphics);
            }
            foreach (MeasurementLine line in _image.Measurements.MeasurementLines)
            {
                DrawLine(line, graphics);
            }
        }
        #endregion

        #region Private menbers

        private void DrawSpot(MeasurementSpot spot, Graphics graphics)
        {
            int dist = 17;
            int r = 4;
            graphics.DrawEllipse(_pen, spot.X - r / 2, spot.Y - r / 2, r, r);

            Point p1 = new Point(spot.X, spot.Y - dist);
            Point p2 = new Point(spot.X, spot.Y - r);
            graphics.DrawLine(_pen, p1, p2);

            Point p3 = new Point(spot.X, spot.Y + r);
            Point p4 = new Point(spot.X, spot.Y + dist);
            graphics.DrawLine(_pen, p3, p4);

            p1 = new Point(spot.X - dist, spot.Y);
            p2 = new Point(spot.X - r, spot.Y);
            graphics.DrawLine(_pen, p1, p2);

            p3 = new Point(spot.X + r, spot.Y);
            p4 = new Point(spot.X + dist, spot.Y);
            graphics.DrawLine(_pen, p3, p4);

            string str = string.Format("{0} {1:F01}", spot.Name, spot.Value.Value);
            //string str = spot.Value.Value.ToString("F01");
            graphics.DrawString(str, _textFont, _textBrush, spot.X + dist / 2, spot.Y - dist);
        }

        private static Rectangle PadHitArea(Point pt)
        {
            return new Rectangle(pt.X - 3, pt.Y - 3, 6, 6);
        }

        private void DrawAreaSelection(MeasurementRectangle rectangle, Graphics graphics)
        {
            Rectangle selection = PadHitArea(new Point(rectangle.Location.X, rectangle.Location.Y));

            // Upper left
            graphics.DrawLine(_pen, selection.Location, new Point(selection.X + selection.Width, selection.Y));
            graphics.DrawLine(_pen, selection.Location, new Point(selection.X, selection.Y + selection.Height));

            // Upper mid
            selection = PadHitArea(new Point(rectangle.Location.X + rectangle.Width / 2, rectangle.Location.Y));

            graphics.DrawLine(_pen, selection.Location, new Point(selection.X + selection.Width, selection.Y));
            graphics.DrawLine(_pen, new Point(selection.Location.X, selection.Y + selection.Height), new Point(selection.X + selection.Width, selection.Y + selection.Height));

            // Upper right
            selection = PadHitArea(new Point(rectangle.Location.X + rectangle.Width, rectangle.Location.Y));

            graphics.DrawLine(_pen, selection.Location, new Point(selection.X + selection.Width, selection.Y));
            graphics.DrawLine(_pen, new Point(selection.X + selection.Width, selection.Y), new Point(selection.X + selection.Width, selection.Y + selection.Height));


            // Right mid
            selection = PadHitArea(new Point(rectangle.Location.X + rectangle.Width, rectangle.Location.Y + rectangle.Height / 2));

            graphics.DrawLine(_pen, selection.Location, new Point(selection.X, selection.Y + selection.Height));
            graphics.DrawLine(_pen, new Point(selection.X + selection.Width, selection.Y), new Point(selection.X + selection.Width, selection.Y + selection.Height));

            // Bottom right
            selection = PadHitArea(new Point(rectangle.Location.X + rectangle.Width, rectangle.Location.Y + rectangle.Height));

            graphics.DrawLine(_pen, new Point(selection.Location.X + selection.Width, selection.Location.Y), new Point(selection.Location.X + selection.Width, selection.Y + selection.Height));
            graphics.DrawLine(_pen, new Point(selection.Location.X + selection.Width, selection.Y + selection.Height), new Point(selection.X, selection.Y + selection.Height));

            // Bottom mid
            selection = PadHitArea(new Point(rectangle.Location.X + rectangle.Width / 2, rectangle.Location.Y + rectangle.Height));

            graphics.DrawLine(_pen, selection.Location, new Point(selection.Location.X + selection.Width, selection.Y));
            graphics.DrawLine(_pen, new Point(selection.Location.X, selection.Y + selection.Height), new Point(selection.Location.X + selection.Width, selection.Y + selection.Height));

            // Lower left
            selection = PadHitArea(new Point(rectangle.Location.X, rectangle.Location.Y + rectangle.Height));

            graphics.DrawLine(_pen, selection.Location, new Point(selection.Location.X, selection.Y + selection.Height));
            graphics.DrawLine(_pen, new Point(selection.Location.X, selection.Y + selection.Height), new Point(selection.Location.X + selection.Width, selection.Y + selection.Height));

            // Left mid
            selection = PadHitArea(new Point(rectangle.Location.X, rectangle.Location.Y + rectangle.Height / 2));

            graphics.DrawLine(_pen, selection.Location, new Point(selection.Location.X, selection.Y + selection.Height));
            graphics.DrawLine(_pen, new Point(selection.Location.X + selection.Width, selection.Y), new Point(selection.Location.X + selection.Width, selection.Y + selection.Height));
        }

        private void DrawArea(MeasurementRectangle rectangle, Graphics graphics)
        {
            Rectangle rect = new Rectangle(rectangle.Location.X, rectangle.Location.Y, rectangle.Width, rectangle.Height);
            graphics.DrawRectangle(_pen, rect);

            DrawAreaSelection(rectangle, graphics);

            string str = rectangle.Min.Value.ToString("F01");
            str += " - ";
            str += rectangle.Max.Value.ToString("F01");
            graphics.DrawString(str, _textFont, _textBrush, rectangle.Location.X + 5, rectangle.Location.Y + 5);

            graphics.FillRectangle(_transparentBrush, rect);

            DrawHotSpot(graphics, rectangle.HotSpot);
        }

        private void DrawAdiposeArea(MeasurementRectangle adiposeRectangle, Graphics graphics)
        {
            Rectangle rect = new Rectangle(adiposeRectangle.Location.X, adiposeRectangle.Location.Y, adiposeRectangle.Width, adiposeRectangle.Height);
            graphics.DrawRectangle(_pen, rect);

            DrawAreaSelection(adiposeRectangle, graphics);
            //DrawAdiposeSelection(adiposeRectangle, graphics);

            string str = adiposeRectangle.Min.Value.ToString("F01");
            str += " - ";
            str += adiposeRectangle.Max.Value.ToString("F01");
            graphics.DrawString(str, _textFont, _textBrush, adiposeRectangle.Location.X + 5, adiposeRectangle.Location.Y + 5);

            graphics.FillRectangle(_transparentBrush, rect);

            DrawHotSpot(graphics, adiposeRectangle.HotSpot);
        }

        private void DrawLineSelection(MeasurementLine line, Graphics graphics)
        {
            // Left mid
            Rectangle selection = PadHitArea(line.Start);
            graphics.DrawRectangle(_pen, selection);

            selection = PadHitArea(line.End);
            graphics.DrawRectangle(_pen, selection);

            string str = line.Min.Value.ToString("F01");
            str += " - ";
            str += line.Max.Value.ToString("F01");

            graphics.DrawString(str, _textFont, _textBrush, line.Start.X + 5, line.Start.Y + 5);
        }

        private void DrawLine(MeasurementLine line, Graphics graphics)
        {
            graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            graphics.DrawLine(_pen, line.Start, line.End);
            DrawLineSelection(line, graphics);
        }

        private void DrawHotSpot(Graphics graphics, Point point)
        {
            Point point1 = point;
            point1.Offset(-6, 6);
            Point point2 = point;
            point2.Offset(6, 6);
            Point[] points = new Point[] { point, point1, point2 };
            graphics.FillPolygon(Brushes.Red, points);
            graphics.DrawPolygon(Pens.Black, points);
        }
        #endregion

        #region Private members

        private ThermalImageFile _image;
        protected Pen _pen = Pens.White;
        protected Brush _transparentBrush;
        protected Font _textFont;
        protected Brush _textBrush = Brushes.White;

        #endregion
    }
}
