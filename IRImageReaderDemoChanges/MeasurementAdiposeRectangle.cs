using Flir.Atlas.Image;
using Flir.Atlas.Image.Measurements;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace IRImageApplication
{
    public class MeasurementAdiposeRectangle
    {
        private ThermalValue _max;
        private ThermalValue _min;
        private ThermalValue _average;
        private Point _location;
        private int _height;
        private int _width;
        private String _name;
        private double[] _imageValues;
        private double[][] _rectangleImage;

        public MeasurementAdiposeRectangle(MeasurementRectangle rectangle)
        {
            _max = rectangle.Max;
            _min = rectangle.Min;
            _average = rectangle.Average;
            _location = rectangle.Location;
            _height = rectangle.Height;
            _width = rectangle.Width;
            _name = rectangle.Name;
            
            if (_width > 0 && _height > 0)
            {
                _imageValues = rectangle.GetValues();

                _rectangleImage = new double[_height][];
                int index = 0;
                for (int i = 0; i < _height; i++)
                {
                    _rectangleImage[i] = new double[_width];
                    for (int j = 0; j < _width; j++)
                    {
                        _rectangleImage[i][j] = _imageValues[index++];
                    }
                }

            }
            else
            {
                _imageValues = null;
                _rectangleImage = null;
            }
        }

        public double[][] RectangleImage { get => _rectangleImage; }

        public ThermalValue Max { get => _max; }

        public ThermalValue Min { get => _min; }

        public ThermalValue Average { get => _average; }

        public Point Location { get => _location; }

        public int Height { get => _height; }

        public int Width { get => _width; }

        public String Name { get => _name; }

        public void PrintSerialValues()
        {
            for (int i = 0; i < _imageValues.Length; i++)
            {
                Console.Write("{0:F2} ", _imageValues[i]);
            }
            Console.WriteLine();
        }

        public void PrintImageValues()
        {
            Console.WriteLine();
            Console.Write($"Width: {_width} Height: {_height}");
            Console.WriteLine();

            for (int i = 0; i < _height; i++)
            {
                for (int j = 0; j < _width; j++)
                {
                    if (_rectangleImage[i][j] > 10.0f)
                        Console.Write("{0:F2} ", _rectangleImage[i][j]);
                    else
                        Console.Write("0 ");
                }
                Console.WriteLine();
            }
        }
    }
}
