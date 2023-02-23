using Flir.Atlas.Image;
using Flir.Atlas.Image.Measurements;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace IRImageApplication
{
    public class MeasurementAdiposeRectangle
    {
        private readonly MeasurementRectangle _rectangle;

        public MeasurementAdiposeRectangle(MeasurementRectangle rectangle)
        {
            this._rectangle = rectangle;
        }

        public ThermalValue Max 
        { 
            get
            {
                return _rectangle.Max;
            } 
        }

        public ThermalValue Min
        {
            get
            {
                return _rectangle.Min;
            }
        }

        public ThermalValue Average
        {
            get
            {
                return _rectangle.Average;
            }
        }

        public Point Location
        {
            get
            {
                return _rectangle.Location;
            }
        }

        public int Height
        {
            get
            {
                return _rectangle.Height;
            }
        }

        public int Width
        {
            get
            {
                return _rectangle.Width;
            }
        }

        public String Name
        { 
            get 
            {
                return _rectangle.Name; 
            } 
        }

    }
}
