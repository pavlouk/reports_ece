using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IRImageApplication
{
    internal class SeededRegionGrowing
    {
        private int[][] _image;  // grayscale image
        private int _width;  // image width
        private int _height;  // image height
        private bool[][] _visited;  // flag for visited pixels
        private int[][] _region;  // region being grown
        private int _regionSize;  // current size of the region
        private int _threshold;  // threshold for similarity

        public SeededRegionGrowing(int[][] image, int threshold)
        {
            _image = image;
            _width = image.Length;
            _height = image[0].Length;
            _visited = new bool[_width][];
            _region = new int[_width][];
            _threshold = threshold;

            for (int i = 0; i < _width; i++)
            {
                _visited[i] = new bool[_height];
                _region[i] = new int[_height];
            }
        }

        public List<Point> GrowFromSeed(Point seed)
        {
            if (!IsInImage(seed))
            {
                throw new ArgumentOutOfRangeException("Seed is outside image boundary.");
            }

            List<Point> regionPoints = new List<Point>();

            // Initialize region
            _regionSize = 0;
            ClearRegion();
            _region[seed.X][seed.Y] = _image[seed.X][seed.Y];
            _regionSize++;

            // Grow region
            regionPoints.Add(seed);
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
                            }
                        }
                    }
                }
            }

            // Return region
            List<Point> result = new List<Point>();
            for (int i = 0; i < _width; i++)
            {
                for (int j = 0; j < _height; j++)
                {
                    if (_region[i][j] != 0)
                    {
                        result.Add(new Point(i, j));
                    }
                }
            }

            return result;
        }

        private bool IsInImage(Point p)
        {
            return p.X >= 0 && p.X < _width && p.Y >= 0 && p.Y < _height;
        }

        private bool IsSimilar(Point p1, Point p2)
        {
            return Math.Abs(_image[p1.X][p1.Y] - _image[p2.X][p2.Y]) <= _threshold;
        }

        private void ClearRegion()
        {
            for (int i = 0; i < _width; i++)
            {
                for (int j = 0; j < _height; j++)
                {
                    _region[i][j] = 0;
                    _visited[i][j] = false;
                }
            }
        }

        public int GetThresholdAsPercentage(double percentage)
        {
            // Find the minimum and maximum pixel values in the image
            int min = int.MaxValue;
            int max = int.MinValue;
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
            int range = max - min;
            int threshold = (int)(percentage * range);

            return threshold;
        }

    }
}
