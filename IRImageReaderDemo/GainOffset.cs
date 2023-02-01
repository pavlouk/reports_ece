using System;
using System.Collections.Generic;
using System.Text;
using System.Drawing;
using Flir.Atlas.Image;

namespace IRImageReaderDemo
{
    class GainOffset
    {
        #region Construction

        public GainOffset(Rectangle rect, ThermalImageFile image)
        {
            _image = image;
            _rectangle = rect;
            CalculateGainOffset();
        }
        #endregion

        #region public Methods

        public Point ImageToLogical(Point point)
        {
            point.X = (int)((double)point.X * _xGain + _xOffset);
            point.Y = (int)((double)point.Y * _yGain + _yOffset);
            return point;
        }

        public Point LogicalToImage(Point point)
        {
            point.X = (int)((((double)point.X - _xOffset)) / _xGain + 0.5);
            point.Y = (int)((((double)point.Y - _yOffset)) / _yGain + 0.5);
            return point;
        }

        public void CalculateGainOffset()
        {
            Rectangle rc = _rectangle;
            Rectangle rcImage = new Rectangle(0, 0, _image.Width, _image.Height);

            double curRatio = (double)rc.Width / (double)rc.Height;
            double newRatio = (double)rcImage.Width / (double)rcImage.Height;

            if (curRatio > newRatio)
            {
                int nHeight = rc.Height;
                rc.Width = (int)(nHeight * newRatio);
            }
            else
            {
                rc.Height = (int)(rc.Right / newRatio + 0.5);
            }
            
            _xGain = (double)(rc.Right - rc.Left) / (double)(rcImage.Width);
            _yGain = (double)(rc.Bottom - rc.Top) / (double)(rcImage.Height);

            if (curRatio > newRatio)
            {
                double aspectRatio = (double)rcImage.Width / (double)rcImage.Height;
                double width = aspectRatio * (double)_rectangle.Height;
                _xOffset = (_rectangle.Width - width) / 2.0;
                _yOffset = (double)(rc.Top + _yGain) / 2.0;
            }
            else
            {
                double aspectRatio = (double)rcImage.Height / (double)rcImage.Width;
                double height = aspectRatio * (double)_rectangle.Width;
                _yOffset = (_rectangle.Height - height) / 2.0;
                _xOffset = (double)(rc.Left + _xGain) / 2.0;
            }            
        }
        #endregion

        #region Private fields

        private double _xGain;
        private double _xOffset;
        private double _yGain;
        private double _yOffset;
        private Rectangle _rectangle;
        private ThermalImageFile _image;

        #endregion
    }
}
