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

            //_imageValues = rectangle.GetValues();

            double[] imageValues = rectangle.GetValues();

            // print the values to the console
            for (int i = 0; i < imageValues.Length; i++)
            {
                Console.WriteLine($"Value {i}: {imageValues[i]}");
            }

            
            int index = 0;
            _rectangleImage = new double[_width][];
            for (int i = 0; i < _width; i++)
            {
                _rectangleImage[i] = new double[_height];
                for (int j = 0; j < _height; j++)
                {
                    _rectangleImage[i][j]  = imageValues[index++];
                }
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

    }
}
