using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace IRImageReaderDemo
{
    public partial class RangeSliderControl : Control
    {
        #region Constructor

        public RangeSliderControl()
        {
            InitializeComponent();

            SetStyle(ControlStyles.SupportsTransparentBackColor, true);
            this.BackColor = Color.Transparent;

            this.Resize += new EventHandler(RangeSliderControl_Resize);

            this.DoubleBuffered = true;
            Set(-20,100, -10,70, 25, 75);
        }
	    #endregion

        #region Public Methods
        public void Set(double min, double max, double referenceMin, double referenceMax, double valueMin, double valueMax)
        {
            _min = min;
            _max = max;
            _referenceMin = referenceMin;
            _referenceMax = referenceMax;
            _valueMin = valueMin;
            _valueMax = valueMax;


            if (_referenceMin < _min)
            {
                _referenceMin = _min;
            }

            if (_valueMin < _min)
            {
                _valueMin = _min;
            }

            if (_max < _min)
            {
                _max = _min;
            }

            if (_referenceMax > _max)
            {
                _referenceMax = _max;
            }

            if (_valueMax > _max)
            {
                _valueMax = _max;
            }
        }
        #endregion

        #region Properties


        public double Min 
        {
            get { return _min; } 
             
        }
        public double Max
        { 
            get { return _max; } 
             
        }
        public double ReferenceMin
        {
            get { return _referenceMin; }             
        }
        public double ReferenceMax
        {
            get { return _referenceMax; }            
        }
        public double ValueMin
        {
            get { return _valueMin; }
            
        }
        public double ValueMax
        {
            get { return _valueMax; }             
        }
    	#endregion        
        
        #region Events

        public event EventHandler<RangeSliderEventArgs> ValuesUpdated;

        #endregion

        #region Protected Methods

        protected override Size DefaultSize
        {
            get {   return new Size(100, 30);   }
        }

        protected override void OnPaint(PaintEventArgs pe)
        {
            base.OnPaint(pe);

            DrawAxis(pe.Graphics);
        }

        protected override void OnMouseDown(MouseEventArgs e)
        {
            base.OnMouseDown(e);

            if (e.Location.X > PixelValueMin && e.Location.X < PixelValueMax)
            {
                if (Capture)
                {
                    _capturedLocation = e.Location;
                    _captureState = CaptureState.MinAndMax;
                }
            }
            else if (e.Location.X <= PixelValueMin && e.Location.X > (PixelValueMin - _handleWidth))
            {
                if (Capture)
                {
                    _capturedLocation = e.Location;
                    _captureState = CaptureState.Min;
                }
            }
            else if (e.Location.X >= PixelValueMax && e.Location.X < (PixelValueMax + _handleWidth))
            {
                if (Capture)
                {
                    _capturedLocation = e.Location;
                    _captureState = CaptureState.Max;
                }
            }
            else
            {
                _captureState = CaptureState.None;
            }
        }

        protected override void OnMouseUp(MouseEventArgs e)
        {
            base.OnMouseUp(e);

            _captureState = CaptureState.None;
        }

        protected override void OnMouseMove(MouseEventArgs e)
        {
            base.OnMouseMove(e);

            if (e.Location.X > PixelValueMin && e.Location.X < PixelValueMax)
            {
                Cursor = Cursors.Hand;
            }
            else if (e.Location.X <= PixelValueMin && e.Location.X > (PixelValueMin - _handleWidth))
            {
                Cursor = Cursors.SizeWE;
            }
            else if (e.Location.X >= PixelValueMax && e.Location.X < (PixelValueMax + _handleWidth))
            {
                Cursor = Cursors.SizeWE;
            }
            else
            {
                Cursor = Cursors.Default;
            }

            if (Capture)
            {
                int diff = e.Location.X - _capturedLocation.X;
                _capturedLocation = e.Location;
                if (diff == 0)
	            {
                    return;
	            }
                double change = diff / PixelPerUnit;

                switch (_captureState)
                {
                    case CaptureState.None:
                        break;
                    case CaptureState.Min:
                        _valueMin += change;
                        Invalidate();
                        OnValuesUpdated(RangeSliderEventArgs.Empty);
                        break;
                    case CaptureState.MinAndMax:
                        double newValueMin = ValueMin + change;
                        double newValueMax = ValueMax + change;
                        if (newValueMin >= Min && newValueMax <= Max)
                        {
                            _valueMin = newValueMin;
                            _valueMax = newValueMax;
                            Invalidate();
                            OnValuesUpdated(RangeSliderEventArgs.Empty);
                        }
                        break;
                    case CaptureState.Max:
                        _valueMax += change;
                        Invalidate();
                        OnValuesUpdated(RangeSliderEventArgs.Empty);
                        break;
                    default:
                        break;
                }
            }
        }

        protected override void OnMouseLeave(EventArgs e)
        {
            base.OnMouseLeave(e);

            Cursor = Cursors.Default;
        }
	    #endregion    

        #region Private properties
        private double PixelPerUnit
        {
            get
            {
                int startX = _handleWidth + Margin.Left;
                int width = ClientRectangle.Width - startX - Margin.Right - _handleWidth;
                double range = Max - Min;
                double pixelPerUnit = width / range;
                return pixelPerUnit;
            }
        }


        public int PixelValueMin
        {
            get
            {
                int startX = _handleWidth + Margin.Left;
                return (int)((ValueMin - Min) * PixelPerUnit) + startX;
            }
        }
        private int PixelValueMax
        {
            get
            {
                int startX = _handleWidth + Margin.Left;
                return (int)((ValueMax - Min) * PixelPerUnit) + startX;
            }
        }
        #endregion

        #region Private Methods

        private void RangeSliderControl_Resize(object sender, EventArgs e)
        {
            Invalidate();
        }

        private void DrawAxis(Graphics graphics)
        {
            int startX = _handleWidth + Margin.Left;
            int width = ClientRectangle.Width - startX - Margin.Right - _handleWidth;

            double range = Max - Min;
            
            int referenceMin = (int)((ReferenceMin-Min) * PixelPerUnit) + startX;
            int referenceMax = (int)((ReferenceMax-Min) * PixelPerUnit) + startX;
            int referenceWidth = referenceMax - referenceMin;
            
            Rectangle sliderRect = new Rectangle(startX, Margin.Top, width, _height);
            Rectangle referenceRect = new Rectangle(referenceMin, Margin.Top, referenceWidth, _height);

            DrawInterior(graphics, sliderRect);

            DrawReference(graphics, referenceRect);

            DrawOutline(graphics, sliderRect);
            graphics.Flush();

            DrawHandleConnector(graphics, PixelValueMin, PixelValueMax);

            DrawMinHandle(graphics, PixelValueMin);
            DrawMaxHandle(graphics, PixelValueMax);

            graphics.Flush();
        }

        private void DrawInterior(Graphics graphics, Rectangle rect)
        {
            graphics.FillRectangle(Brushes.White, rect);
        }

        private void DrawReference(Graphics graphics, Rectangle rect)
        {
            graphics.FillRectangle(Brushes.LightGreen, rect);
        }

        private void DrawOutline(Graphics graphics, Rectangle rect)
        {
            graphics.DrawRectangle(Pens.Black, rect);
        }

        private void DrawMinHandle(Graphics graphics, int position)
        {
            int startX = position - _handleWidth;
            int baseY = _height + Margin.Top;
            int top = Margin.Top + 1;

            Rectangle bottomRect = new Rectangle(startX, baseY, _handleWidth, _connectorHeight);
            graphics.FillRectangle(Brushes.LightGray, bottomRect);
            graphics.DrawRectangle(Pens.Gray, bottomRect);
            graphics.DrawLine(Pens.White, startX + 1, baseY + 1, position - 1, baseY + 1);
            graphics.DrawLine(Pens.White, startX + 1, baseY + 1, startX + 1, baseY + _connectorHeight - 1);

            GraphicsPath path = new GraphicsPath();
            path.AddLine(startX, baseY, position, baseY);
            path.AddLine(position, baseY, position, top);
            path.AddLine(position, top, startX, baseY - 2);
            path.AddLine(startX, baseY - 2, startX, baseY);
            graphics.FillPath(Brushes.LightGray, path);
            graphics.DrawPath(Pens.Gray, path);
            graphics.DrawLine(Pens.White, position - 1, top + 2, startX + 1, baseY - 2);
            graphics.DrawLine(Pens.White, startX + 1, baseY - 2, startX + 1, baseY - 1);
        }

        private void DrawMaxHandle(Graphics graphics, int position)
        {
            int stopX = position + _handleWidth;
            int baseY = _height + Margin.Top;
            int top = Margin.Top + 1;

            Rectangle bottomRect = new Rectangle(position, baseY, _handleWidth, _connectorHeight);
            graphics.FillRectangle(Brushes.LightGray, bottomRect);
            graphics.DrawRectangle(Pens.Gray, bottomRect);
            graphics.DrawLine(Pens.White, position + 1, baseY + 1, stopX - 1, baseY + 1);
            graphics.DrawLine(Pens.White, position + 1, baseY + 1, position + 1, baseY + _connectorHeight - 1);

            GraphicsPath path = new GraphicsPath();
            path.AddLine(position, baseY, stopX, baseY);
            path.AddLine(stopX, baseY, stopX, baseY - 2);
            path.AddLine(stopX, baseY - 2, position, top);
            path.AddLine(position, top, position, baseY);

            graphics.FillPath(Brushes.LightGray, path);
            graphics.DrawPath(Pens.Gray, path);
            graphics.DrawLine(Pens.White, position + 1, top + 2, position + 1, baseY - 1);
        }

        private void DrawHandleConnector(Graphics graphics, int valueMin, int valueMax)
        {
            int baseY = _height + Margin.Top;

            Rectangle rect = new Rectangle(valueMin, baseY, valueMax - valueMin, _connectorHeight);
            graphics.FillRectangle(Brushes.LightGray, rect);
            graphics.DrawRectangle(Pens.Gray, rect);
            graphics.DrawLine(Pens.White, valueMin + 1, baseY + 1, valueMax - 1, baseY + 1);
            graphics.DrawLine(Pens.White, valueMin + 1, baseY + 1, valueMin + 1, baseY + _connectorHeight - 1);
        }

        private void OnValuesUpdated(RangeSliderEventArgs e)
        {
            EventHandler<RangeSliderEventArgs> handler = ValuesUpdated;
            if (handler != null)
            {
                handler(this, e);
            }
        }
        #endregion

        #region Private Fields
        
        private readonly int _height = 12;
        private readonly int _connectorHeight = 12;
        private readonly int _handleWidth = 9;

        private double _min;
        private double _max;
        private double _referenceMin;
        private double _referenceMax;
        private double _valueMin;
        private double _valueMax;        

        private Point _capturedLocation;
        private CaptureState _captureState = CaptureState.None;

        private enum CaptureState
        {
            None,
            Min,
            MinAndMax,
            Max
        };

        #endregion
    }
}
