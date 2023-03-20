using Flir.Atlas.Image.Measurements;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace IRImageApplication
{
    internal class SeededRegionGrowing
    {
        private double[][] _image;  // grayscale image
        private int _width;  // image width
        private int _height;  // image height
        private bool[][] _visited;  // flag for visited pixels
        private double[][] _region;  // region being grown
        private int _regionSize;  // current size of the region
        private double _threshold;  // threshold for similarity
        private Point _location;
        private List<Point> _adiposePoints;
        private double _runningMean;
        private double _regionMean;

        public int RegionSize { get => _regionSize; }
        public double Threshold { get; set; }
        public double[][] Visited { get; }
        public double[][] Region { get; }
        public List<Point> AdiposePoints { get => _adiposePoints; }
        public double RegionMean { get => _regionMean; }

        public SeededRegionGrowing(MeasurementAdiposeRectangle measurementAdiposeRectangle)
        {
            if (measurementAdiposeRectangle.RectangleImage != null && measurementAdiposeRectangle.Width > 1 && measurementAdiposeRectangle.Height > 1)
            {
                _image = measurementAdiposeRectangle.RectangleImage;
                _width = measurementAdiposeRectangle.Width;
                _height = measurementAdiposeRectangle.Height;
                _location = measurementAdiposeRectangle.Location;

                _threshold = 0.1f;
                
                _visited = new bool[_height][];
                _region = new double[_height][];

               _adiposePoints = new List<Point>();


                for (int i = 0; i < _height; i++)
                {
                    _visited[i] = new bool[_width];
                    _region[i] = new double[_width];
                }

                GrowFromSeed(measurementAdiposeRectangle.Hotspot);
            } 
            else
            {
                _visited = null;
                _region = null;
                _adiposePoints = null;
                _regionMean = 0.0;
            }
        }

        private void GrowFromSeed(Point seed)
        {
            // translate global seed to local seed 
            Point localSeed = new Point(seed.Y - _location.Y, seed.X - _location.X);

            if (_visited == null)
                return;

            if (!IsInImage(localSeed))
            {
                throw new ArgumentOutOfRangeException("Seed is outside image boundary.");
            }

            List<Point> regionPoints = new List<Point>();
            _regionSize = 0;
            ClearRegion();
           
            _region[localSeed.X][localSeed.Y] = _image[localSeed.X][localSeed.Y];
            _runningMean = _image[localSeed.X][localSeed.Y];
            _regionSize++;
            regionPoints.Add(localSeed);

            while (regionPoints.Count > 0)
            {
                Point p = regionPoints[0];
                regionPoints.RemoveAt(0);

                if (!_visited[p.X][p.Y])
                {
                    _visited[p.X][p.Y] = true;

                    // Check neighbors
                    for (int x = -1; x <= 1; x++)
                    {
                        for (int y = -1; y <= 1; y++)
                        {
                            if (x == 0 && y == 0)
                            {
                                continue;
                            }

                            Point neighbor = new Point(p.X + x, p.Y + y);

                            if (IsInImage(neighbor) && IsSimilar(neighbor, p))
                            {
                                // Add to region
                                _region[neighbor.X][neighbor.Y] = _image[neighbor.X][neighbor.Y];
                                _regionSize++;
                                regionPoints.Add(neighbor);
                                // update seeded region mean temp
                                _runningMean = UpdateMean(regionPoints);
                            }
                        }
                    }
                }
            }
            _regionSize = 0;
            _regionMean = _region[0][0];

            for (int i = 0; i < _height; i++)
            {
                for (int j = 0; j < _width; j++)
                {
                    if (_region[i][j] != 0)
                    {
                        _regionSize++;
                        _adiposePoints.Add(new Point(i, j));
                        _regionMean += _region[i][j];
                    }

                }
            }
            _regionMean = _regionMean / (double)_regionSize;
        }

        private double UpdateMean(List<Point> regionPoints)
        {
            double runningMean = 0f;
            foreach (Point regionPoint in regionPoints)
            {
                runningMean += _region[regionPoint.X][regionPoint.Y];
            }
            return runningMean / regionPoints.Count;
        }

        private bool IsInImage(Point p)
        {
            return p.X >= 0 && p.X < _height && p.Y >= 0 && p.Y < _width;
        }

        private bool IsSimilar(Point neighborPoint, Point regionPoint)
        {
            // todo neighbor point - running mean of seeded region
            return Math.Abs(_image[neighborPoint.X][neighborPoint.Y] - _runningMean) <= _threshold;
        }

        private void ClearRegion()
        {
            for (int i = 0; i < _height; i++)
            {
                for (int j = 0; j < _width; j++)
                {
                    _region[i][j] = 0;
                    _visited[i][j] = false;
                }
            }
        }

        public double GetThresholdAsPercentage(double percentage)
        {
            // Find the minimum and maximum pixel values in the image
            double min = double.MaxValue;
            double max = double.MinValue;

            for (int i = 0; i < _width; i++)
            {
                for (int j = 0; j < _height; j++)
                {
                    if (_image[i][j] < min)
                    {
                        min = _image[i][j];
                    }
                    if (_image[i][j] > max)
                    {
                        max = _image[i][j];
                    }
                }
            }

            // Calculate the threshold as a percentage of the dynamic range
            double range = max - min;
            int threshold = (int)(percentage * range);

            return threshold;
        }

        public void PrintVisited()
        {
            if (_visited is null)
                return;

            Console.WriteLine();
            Console.Write($"Width: {_width} Height: {_height}");
            Console.WriteLine();

            for (int i = 0; i < _height; i++)
            {
                for (int j = 0; j < _width; j++)
                {
                    if (_visited[i][j])
                        Console.Write("1 ");
                    else
                        Console.Write("0 ");
                }
                Console.WriteLine();
            }
        }

        public void PrintRegion()
        {
            if (_visited is null)
                return;

            Console.WriteLine();
            Console.Write($"Width: {_width} Height: {_height}");
            Console.WriteLine();

            for (int i = 0; i < _height; i++)
            {
                for (int j = 0; j < _width; j++)
                {
                    if (_region[i][j] > 0f)
                        Console.Write("1 ");
                    else
                        Console.Write("0 ");
                }
                Console.WriteLine();
            }
        }
    }

}
