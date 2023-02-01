#region Using Statements

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Threading;
using System.Windows.Forms;
using Flir.Atlas.Image;
using System.Drawing;
using System.IO;
using System.Collections;
using Flir.Atlas.Image.Alarms;
using Flir.Atlas.Image.Fusion;
using Flir.Atlas.Image.Isotherms;
using Flir.Atlas.Image.Measurements;
using Flir.Atlas.Image.Palettes;
using Appearance = Flir.Atlas.Image.Isotherms.Appearance;

#endregion

namespace IRImageReaderDemo
{
    public partial class MainForm : Form
    {
        #region Constructor

        public MainForm()
        {
            InitializeComponent();

            _image.TemperatureUnit = TemperatureUnit.Fahrenheit;
            _image.DistanceUnit = DistanceUnit.Feet;

            propertyGrid1.SelectedObject = _image;
            pictureBox1.Image = Image();
            rangeSliderControl1.ValuesUpdated += new EventHandler<RangeSliderEventArgs>(rangeSliderControl1_ValuesUpdated);
            RegisterMeasurementEvent();
            UpdateScale();
            UpdateRangeSliderControl();
            _image.Changed += new EventHandler<ImageChangedEventArgs>(imageChanged);
            _image.Scale.Changed += new EventHandler<ScaleChangedEventArgs>(Scale_Changed);
            EnableVoiceAnnotation();
            FillTextAnnotation();
            FillAlarm();
            UpdateObjectParameters();
            FillIsotherms();

            // add the default palettes
            foreach (var pal in PaletteManager.Palettes)
            {
                paletteToolStripComboBox.Items.Add(pal.Name);
            }
            // add Custom palette saved in the image.
            paletteToolStripComboBox.Items.Add("Custom");
            // add open... palette from disk.
            paletteToolStripComboBox.Items.Add("Open...");
            paletteToolStripComboBox.SelectedIndex = 3;
            SetPalette(paletteToolStripComboBox.SelectedItem as string);

            paletteToolStripButton.Checked = _image.Palette.IsInverted;

            isoThermToolStripComboBox.Items.Add(IsothermType.Above);
            isoThermToolStripComboBox.Items.Add(IsothermType.Below);
            isoThermToolStripComboBox.Items.Add(IsothermType.Interval);
            isoThermToolStripComboBox.SelectedIndex = 0;

            isoThermToolStripButton.Checked = false;
            isoThermToolStripComboBox.Enabled = false;

            _tooltip.ShowAlways = true;

            guiIsUpdating = false;

            buttonPause.Enabled = false;

            toolStripComboBoxColorDist.Items.Add(ColorDistribution.HistogramEqualization.ToString());
            toolStripComboBoxColorDist.Items.Add(ColorDistribution.TemperatureLinear.ToString());
            toolStripComboBoxColorDist.Items.Add(ColorDistribution.SignalLinear.ToString());
            toolStripComboBoxColorDist.Items.Add(ColorDistribution.DigitalDetailEnhancement.ToString());
            toolStripComboBoxColorDist.Items.Add(ColorDistribution.Ade.ToString());
            toolStripComboBoxColorDist.Items.Add(ColorDistribution.Entropy.ToString());
            toolStripComboBoxColorDist.Items.Add(ColorDistribution.PlateauHistogramEq.ToString());
            toolStripComboBoxColorDist.Items.Add(ColorDistribution.GuidedFilterDDE.ToString());
            SelectColorDistributionMode();
            toolStripComboBoxColorDist.SelectedIndexChanged += toolStripComboBoxColorDist_SelectedIndexChanged;
            toolStripComboBoxFusionMode.Items.Add("Msx");
            toolStripComboBoxFusionMode.Items.Add("ThermalOnly");
            toolStripComboBoxFusionMode.Items.Add("Blending");
            toolStripComboBoxFusionMode.Items.Add("PictureInPicture");
            toolStripComboBoxFusionMode.Items.Add("ThermalFusionAbove");
            toolStripComboBoxFusionMode.Items.Add("ThermalFusionBelow");
            toolStripComboBoxFusionMode.Items.Add("ThermalFusionInterval");
            toolStripComboBoxFusionMode.Items.Add("VisualOnly");
            toolStripComboBoxFusionMode.SelectedIndexChanged += toolStripComboBoxFusionMode_SelectedIndexChanged;
            toolStripComboBoxFusionMode.Enabled = false;
            UltraMaxtoolStripButton2.Visible = false;
            UltraMaxtoolStripButton2.MouseDown += CreateUltraMaxButton_MouseDown;

            Text = "Thermal Image Reader Sample, running Atlas version: " + ImageBase.Version;

            trackBarThermalFusion.Enabled = false;
            trackBarThermalFusion.ValueChanged += TrackBar1_ValueChanged;

        }

        private void TrackBar1_ValueChanged(object sender, EventArgs e)
        {
            var value = trackBarThermalFusion.Value / 1000.0;
            if (_image.Fusion.Mode == _image.Fusion.ThermalFusionAbove)
            {
                _image.Fusion.ThermalFusionAbove.Threshold = value;
            }
            else if (_image.Fusion.Mode == _image.Fusion.ThermalFusionBelow)
            {
                _image.Fusion.ThermalFusionBelow.Threshold = value;
            }
            else if (_image.Fusion.Mode == _image.Fusion.ThermalFusionInterval)
            {
                _image.Fusion.ThermalFusionInterval.Range = new Range<double>(_image.Scale.Range.Minimum, value);
            }
        }

        private void SelectFusionMode()
        {
            if (_image.Fusion == null)
            {
                toolStripComboBoxFusionMode.Enabled = false;
                return;
            }
            toolStripComboBoxFusionMode.Enabled = true;
            switch (_image.Fusion.Mode.ToString())
            {
                case "Flir.Atlas.Image.Fusion.Msx":
                    toolStripComboBoxFusionMode.SelectedIndex = 0;
                    break;
                case "Flir.Atlas.Image.Fusion.ThermalOnly":
                    toolStripComboBoxFusionMode.SelectedIndex = 1;
                    break;
                case "Flir.Atlas.Image.Fusion.Blending":
                    toolStripComboBoxFusionMode.SelectedIndex = 2;
                    break;
                case "Flir.Atlas.Image.Fusion.PictureInPicture":
                    toolStripComboBoxFusionMode.SelectedIndex = 3;
                    break;
                case "Flir.Atlas.Image.Fusion.ThermalFusionAbove":
                    toolStripComboBoxFusionMode.SelectedIndex = 4;
                    break;
                case "Flir.Atlas.Image.Fusion.ThermalFusionBelow":
                    toolStripComboBoxFusionMode.SelectedIndex = 5;
                    break;
                case "Flir.Atlas.Image.Fusion.ThermalFusionInterval":
                    toolStripComboBoxFusionMode.SelectedIndex = 6;
                    break;
                case "Flir.Atlas.Image.Fusion.VisualOnly":
                    toolStripComboBoxFusionMode.SelectedIndex = 7;
                    break;
                default:
                    throw new ArgumentOutOfRangeException();
            }
        }

        private void SelectColorDistributionMode()
        {
            switch (_image.ColorDistribution)
            {
                case ColorDistribution.HistogramEqualization:
                    toolStripComboBoxColorDist.SelectedIndex = 0;
                    break;
                case ColorDistribution.TemperatureLinear:
                    toolStripComboBoxColorDist.SelectedIndex = 1;
                    break;
                case ColorDistribution.SignalLinear:
                    toolStripComboBoxColorDist.SelectedIndex = 2;
                    break;
                case ColorDistribution.DigitalDetailEnhancement:
                    toolStripComboBoxColorDist.SelectedIndex = 3;
                    break;
                case ColorDistribution.Ade:
                    toolStripComboBoxColorDist.SelectedIndex = 4;
                    break;
                case ColorDistribution.Entropy:
                    toolStripComboBoxColorDist.SelectedIndex = 5;
                    break;
                case ColorDistribution.PlateauHistogramEq:
                    toolStripComboBoxColorDist.SelectedIndex = 6;
                    break;
                case ColorDistribution.GuidedFilterDDE:
                    toolStripComboBoxColorDist.SelectedIndex = 7;
                    break;

                default:
                    throw new ArgumentOutOfRangeException();
            }
        }

        void toolStripComboBoxColorDist_SelectedIndexChanged(object sender, EventArgs e)
        {
            string sel = toolStripComboBoxColorDist.SelectedItem.ToString();
            ColorDistribution mode;

            if (ColorDistribution.TryParse(sel, true, out mode))
            {
                if (mode == ColorDistribution.SignalLinear)
                {
                    _image.ColorDistribution = ColorDistribution.SignalLinear;
                }
                else if (mode == ColorDistribution.HistogramEqualization)
                {
                    _image.ColorDistribution = ColorDistribution.HistogramEqualization;
                }
                else if (mode == ColorDistribution.TemperatureLinear)
                {
                    _image.ColorDistribution = ColorDistribution.TemperatureLinear;
                }
                else if (mode == ColorDistribution.Ade)
                {
                    _image.ColorDistribution = ColorDistribution.Ade;
                }
                else if (mode == ColorDistribution.Entropy)
                {
                    _image.ColorDistribution = ColorDistribution.Entropy;
                }
                else if (mode == ColorDistribution.PlateauHistogramEq)
                {
                    _image.ColorDistribution = ColorDistribution.PlateauHistogramEq;
                }
                else if (mode == ColorDistribution.DigitalDetailEnhancement)
                {
                    _image.ColorDistribution = ColorDistribution.DigitalDetailEnhancement;
                }
                else if (mode == ColorDistribution.GuidedFilterDDE)
                {
                    _image.ColorDistribution = ColorDistribution.GuidedFilterDDE;
                }
            }
        }

        private void bw_DoWork(object sender, DoWorkEventArgs e)
        {
            BackgroundWorker worker = sender as BackgroundWorker;

            _image.ConvertToUltraMax();
        }

        private void CreateUltraMaxButton_MouseDown(object sender, EventArgs e)
        {
            BackgroundWorker bw = new BackgroundWorker();
            bw.WorkerSupportsCancellation = true;
            bw.WorkerReportsProgress = true;
            bw.DoWork += new DoWorkEventHandler(bw_DoWork);
           
            if (bw.IsBusy != true)
            {
                bw.RunWorkerAsync();
            }
        }
    

        void toolStripComboBoxFusionMode_SelectedIndexChanged(object sender, EventArgs e)
        {
            string sel = toolStripComboBoxFusionMode.SelectedItem.ToString();
            trackBarThermalFusion.Enabled = false;
            switch (sel)
            {
                case "Msx":
                    _image.Fusion.Mode = _image.Fusion.Msx;
                    break;
                case "ThermalOnly":
                    _image.Fusion.Mode = _image.Fusion.ThermalOnly;
                    break;
                case "VisualOnly":
                    _image.Fusion.Mode = _image.Fusion.VisualOnly;
                    break;
                case "ThermalFusionAbove":
                    if (_image.Fusion.ThermalFusionAbove.Threshold >= _image.Scale.Range.Maximum || _image.Fusion.ThermalFusionAbove.Threshold <= _image.Scale.Range.Minimum)
                    {
                        _image.Fusion.ThermalFusionAbove.Threshold = _image.Scale.Level;
                    }
                    _image.Fusion.Mode = _image.Fusion.ThermalFusionAbove;
                    trackBarThermalFusion.SetRange((int)(_image.Scale.Range.Minimum * 1000), (int)(_image.Scale.Range.Maximum * 1000));
                    trackBarThermalFusion.Value = (int)(_image.Fusion.ThermalFusionAbove.Threshold * 1000);
                    trackBarThermalFusion.Enabled = true;
                    break;
                case "ThermalFusionBelow":
                    if (_image.Fusion.ThermalFusionBelow.Threshold >= _image.Scale.Range.Maximum || _image.Fusion.ThermalFusionBelow.Threshold <= _image.Scale.Range.Minimum)
                    {
                        _image.Fusion.ThermalFusionBelow.Threshold = _image.Scale.Level;
                    }
                    _image.Fusion.Mode = _image.Fusion.ThermalFusionBelow;
                    trackBarThermalFusion.SetRange((int)(_image.Scale.Range.Minimum * 1000), (int)(_image.Scale.Range.Maximum * 1000));
                    trackBarThermalFusion.Value = (int)(_image.Fusion.ThermalFusionBelow.Threshold * 1000);
                    trackBarThermalFusion.Enabled = true;
                    break;
                case "ThermalFusionInterval":
                    if (_image.Fusion.ThermalFusionInterval.Range.Maximum >= _image.Scale.Range.Maximum || _image.Fusion.ThermalFusionInterval.Range.Maximum <= _image.Scale.Range.Minimum)
                    {
                        _image.Fusion.ThermalFusionInterval.Range = new Range<double>(_image.Scale.Range.Minimum, _image.Scale.Level);
                    }
                    _image.Fusion.Mode = _image.Fusion.ThermalFusionInterval;
                    trackBarThermalFusion.SetRange((int)(_image.Scale.Range.Minimum * 1000), (int)(_image.Scale.Range.Maximum * 1000));
                    trackBarThermalFusion.Value = (int)(_image.Fusion.ThermalFusionInterval.Range.Maximum * 1000);
                    trackBarThermalFusion.Enabled = true;
                    break;
                case "Blending":
                    _image.Fusion.Mode = _image.Fusion.Blending;
                    break;
                case "PictureInPicture":
                    _image.Fusion.Mode = _image.Fusion.PictureInPicture;
                    break;
                default:
                    throw new NotImplementedException("Unknown fusion mode");
            }
        }
        

        #endregion

        #region Event Handlers

        private void RegisterMeasurementEvent()
        {
            _image.Measurements.Added += MeasurementCollection_Added;
            _image.Measurements.Changed += MeasurementCollection_Changed;
            _image.Measurements.Removed += MeasurementCollection_Removed;
        }

        private void MeasurementCollection_Removed(object sender, MeasurementEventArgs e)
        {
            pictureBox1.Image = Image();
            listViewMeasurements.RemoveShape(e.MeasurementShape);
        }

        private void MeasurementCollection_Added(object sender, MeasurementEventArgs e)
        {
            pictureBox1.Image = Image();

            if (e.MeasurementShape as MeasurementSpot != null)
                listViewMeasurements.AddSpot(e.MeasurementShape as MeasurementSpot);
            else if (e.MeasurementShape as MeasurementRectangle != null)
                listViewMeasurements.AddArea(e.MeasurementShape as MeasurementRectangle);
            else if (e.MeasurementShape as MeasurementLine != null)
                listViewMeasurements.AddLine(e.MeasurementShape as MeasurementLine);
        }

        private void MeasurementCollection_Changed(object sender, MeasurementEventArgs e)
        {
            pictureBox1.Image = Image();
            if (e.MeasurementShape as MeasurementSpot != null)
                listViewMeasurements.UpdateSpot(e.MeasurementShape as MeasurementSpot);
            else if (e.MeasurementShape as MeasurementRectangle != null)
                listViewMeasurements.UpdateArea(e.MeasurementShape as MeasurementRectangle);
            else if (e.MeasurementShape as MeasurementLine != null)
                listViewMeasurements.UpdateLine(e.MeasurementShape as MeasurementLine);
        }

        private void UnRegisterMeasurementEvent()
        {
            _image.Measurements.Added -= MeasurementCollection_Added;
            _image.Measurements.Changed -= MeasurementCollection_Changed;
            _image.Measurements.Removed -= MeasurementCollection_Removed;

            
        }

        private void DisplayErrorMessage(string message, Exception ex)
        {
            if (ex.Data != null)
            {
                if (ex.Data.Count > 0)
                    message += ", Extra details: ";
                foreach (DictionaryEntry de in ex.Data)
                    message += string.Format(" key='{0}' - value='{1}'", de.Key, de.Value);
            }
            if (ex.InnerException != null)
            {
                if (ex.InnerException.Data.Count > 0)
                    message += ", Extra inner details: ";
                foreach (DictionaryEntry de in ex.InnerException.Data)
                    message += string.Format(" key='{0}' - value='{1}'", de.Key, de.Value);
            }
            MessageBox.Show(message, this.Text, MessageBoxButtons.OK, MessageBoxIcon.Error);
        }

        private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {
            using (OpenFileDialog dialog = new OpenFileDialog())
            {
                dialog.Filter = "IR Image Files(*.jpg;*.tif;*.img)|*.jpg;*.tif;*.img|All files (*.*)|*.*";
                if (dialog.ShowDialog() == DialogResult.OK)
                {
                    try
                    {
                        _image.Open(dialog.FileName);

                        SelectColorDistributionMode();
                        SelectFusionMode();
                        
                        propertyGrid1.Refresh();
                        listViewEXIF.RefreshEXIF(dialog.FileName);
                        pictureBox1.Image = Image();
                        UpdateScale();
                        UpdateRangeSliderControl();
                        EnableVoiceAnnotation();
                        CleanUpVoiceAnnotation();
                        FillTextAnnotation();
                        FillAlarm();
                        ApplyIsothermAndUpdateImage();

                        
                        if (_image.ContainsUltraMaxData)
                        {
                            UltraMaxtoolStripButton2.Visible = true;
                        }
                        else
                        {
                            UltraMaxtoolStripButton2.Visible = false;
                        }

                        UpdateObjectParameters();

                        Palette pal = _image.Palette;
                        bool customPalette = true;
                        for (int i = 0; i < PaletteManager.Palettes.Count; i++)
                        {
                            if (pal.Name == PaletteManager.Palettes[i].Name)
                            {
                                paletteToolStripComboBox.SelectedIndex = i;
                                customPalette = false;
                                break;
                            }
                        }
                        if (customPalette)
                        {
                            paletteToolStripComboBox.SelectedItem = "Custom";
                        }
                    }
                    catch (Exception ex)
                    {
                        DisplayErrorMessage(String.Format("An error occurred when trying to open the selected file\n\n{0}", ex.ToString()), ex);
                    }
                }
            }
        }

        private void saveToolStripMenuItem_Click(object sender, EventArgs e)
        {
            try
            {
                _image.Save(Image());
            }
            catch (Exception ex)
            {
                DisplayErrorMessage(String.Format("An error occurred when trying to save the selected file\n\n{0}", ex.ToString()), ex);
            }
        }

        private void saveAsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            using (SaveFileDialog dialog = new SaveFileDialog())
            {
                if (dialog.ShowDialog() == DialogResult.OK)
                {
                    try
                    {
                        _image.Save(dialog.FileName, Image());
                    }
                    catch (Exception ex)
                    {
                        DisplayErrorMessage(String.Format("An error occurred when trying to save the selected file\n\n{0}", ex.ToString()), ex);
                    }
                }
            }
        }

        private void autoAdjustButton_Click(object sender, EventArgs e)
        {
            _image.Scale.IsAutoAdjustEnabled = true;

            UpdateRangeSliderControl();

            pictureBox1.Image = Image();
            UpdateScale();
        }

        void rangeSliderControl1_ValuesUpdated(object sender, RangeSliderEventArgs e)
        {
            _image.Scale.Range = new Range<double>(rangeSliderControl1.ValueMin, rangeSliderControl1.ValueMax);
            UpdateScale();
        }

        
        #endregion

        #region Measurement Handling

        private void listViewMeasurments_KeyUp(object sender, KeyEventArgs e)
        {
            if (listViewMeasurements.SelectedItems.Count != 1)
                return;
            MeasurementShape shape = listViewMeasurements.SelectedItems[0].Tag as MeasurementShape;
            if (shape == null)
                return;

            if (e.KeyCode == Keys.Delete)
            {
                if (listViewMeasurements.SelectedItems.Count == 1)
                {
                    _image.Measurements.Remove(shape);
                }
            }
        }

        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {

        }

        private void toolStripButtonArea_Click(object sender, EventArgs e)
        {
            _currentTool = MeasurmentTool.Area;
            toolStripButtonSpot.Checked = false;
            toolStripButtonLine.Checked = false;
            toolStripButtonPolyLine.Checked = false;
            markerToolStripButton.Checked = false;
            toolStripButtonFlyingSpot.Checked = false;
            toolStripButton1.Checked = false;

            toolStripButtonSelect.Checked = false;
            _adding = true;
            _delete = false;
        }

        private void toolStripButtonSpot_Click(object sender, EventArgs e)
        {
            _currentTool = MeasurmentTool.Spot;
            toolStripButtonArea.Checked = false;
            toolStripButtonLine.Checked = false;
            toolStripButtonPolyLine.Checked = false;
            markerToolStripButton.Checked = false;
            toolStripButtonFlyingSpot.Checked = false;
            toolStripButton1.Checked = false;

            toolStripButtonSelect.Checked = false;
            _adding = true;
            _delete = false;
        }

        private void toolStripButtonLine_Click(object sender, EventArgs e)
        {
            _currentTool = MeasurmentTool.Line;
            toolStripButtonArea.Checked = false;
            toolStripButtonSpot.Checked = false;
            toolStripButtonPolyLine.Checked = false;
            markerToolStripButton.Checked = false;
            toolStripButtonFlyingSpot.Checked = false;
            toolStripButton1.Checked = false;
            toolStripButtonSelect.Checked = false;
            _adding = true;
            _delete = false;
        }

        private void toolStripButtonPolyLine_Click(object sender, EventArgs e)
        {
            _currentTool = MeasurmentTool.PolyLine;
            toolStripButtonArea.Checked = false;
            toolStripButtonSpot.Checked = false;
            toolStripButtonLine.Checked = false;
            markerToolStripButton.Checked = false;
            toolStripButtonFlyingSpot.Checked = false;
            toolStripButton1.Checked = false;
            toolStripButtonSelect.Checked = false;
            _adding = true;
            _delete = false;
        }

        private void toolStripButtonFlyingSpot_Click(object sender, EventArgs e)
        {
            _currentTool = MeasurmentTool.FlyingSpot;
            toolStripButtonSpot.Checked = false;
            toolStripButtonLine.Checked = false;
            toolStripButtonPolyLine.Checked = false;
            markerToolStripButton.Checked = false;
            toolStripButtonFlyingSpot.Checked = false;
            toolStripButton1.Checked = false;
            toolStripButtonSelect.Checked = false;
            _adding = true;
            _delete = false;
        }

        private void markerToolStripButton_Click(object sender, EventArgs e)
        {
            _currentTool = MeasurmentTool.Marker;
            toolStripButtonSpot.Checked = false;
            toolStripButtonArea.Checked = false;
            toolStripButtonLine.Checked = false;
            toolStripButtonPolyLine.Checked = false;
            toolStripButtonFlyingSpot.Checked = false;
            toolStripButton1.Checked = false;
            toolStripButtonSelect.Checked = false;
            _adding = true;
            _delete = false;
        }

        private void toolStripButton1_Click(object sender, EventArgs e)
        {
            _currentTool = MeasurmentTool.Area;
            toolStripButtonSpot.Checked = false;
            toolStripButtonLine.Checked = false;
            toolStripButtonPolyLine.Checked = false;
            markerToolStripButton.Checked = false;
            toolStripButtonFlyingSpot.Checked = false;
            toolStripButton1.Checked = true;
            toolStripButtonSelect.Checked = false;
            _adding = false;
            _delete = true;
        }

        private void toolStripButtonSelect_Click(object sender, EventArgs e)
        {
            _currentTool = MeasurmentTool.None;
            toolStripButtonSpot.Checked = false;
            toolStripButtonArea.Checked = false;
            toolStripButtonLine.Checked = false;
            toolStripButtonPolyLine.Checked = false;
            toolStripButtonFlyingSpot.Checked = false;
            toolStripButton1.Checked = false;
            toolStripButtonSelect.Checked = true;
            _adding = false;
            _delete = false;

            this.Cursor = Cursors.Arrow;
        }

        private void toolStripButtonSave_Click(object sender, EventArgs e)
        {
            try
            {
                _image.Save(Image());
            }
            catch (Exception ex)
            {
                DisplayErrorMessage(String.Format("An error occurred when trying to save the selected file\n\n{0}", ex.ToString()), ex);
            }
        }

        private static bool IsInsideRect(Rectangle rect, Point pt)
        {
            bool isInside = false;

            if (pt.X >= rect.X &&
                pt.X < (rect.X + rect.Width) &&
                pt.Y >= rect.Y &&
                pt.Y < (rect.Y + rect.Height))
            {
                isInside = true;
            }

            return isInside;
        }

        private static Rectangle PadHitArea(Point pt)
        {
            return new Rectangle(pt.X - 3, pt.Y - 3, 6, 6);
        }

        private static float GetDistanceFromLine(Point start, Point end, Point pt)
        {
            if (start.X != end.X)
            {
                float m = (float)(end.Y - start.Y) / (float)(end.X - start.X);
                float b = -1.0f;
                float c = (float)start.Y - m * (float)start.X;

                float x = m * (float)pt.X + b * (float)pt.Y + c;
                float y = (float)(Math.Sqrt(m * m + b * b));

                return x / y;
            }
            else
            {
                return (float)(pt.X - start.X);
            }
        }

        private bool HitTest(Point point, ref int index, ref MeasurmentTool tool, ref TrackerHit hit)
        {
            int i = 0;

            //////////////////////////////////////////////////////////////////////////
            // Check spotmeter
            //////////////////////////////////////////////////////////////////////////
            foreach (MeasurementSpot spot in _image.Measurements.MeasurementSpots)
            {
                Rectangle rect = new Rectangle(spot.X - 5, spot.Y - 5, 10, 10);
                if (IsInsideRect(rect, point))
                {
                    this.Cursor = Cursors.SizeAll;

                    index = i;
                    tool = MeasurmentTool.Spot;
                    hit = TrackerHit.hitMiddle;

                    return true;
                }
                i++;
            }

            i = 0;

            //////////////////////////////////////////////////////////////////////////
            // Check lines
            //////////////////////////////////////////////////////////////////////////
            foreach (MeasurementLine line in _image.Measurements.MeasurementLines)
            {
                // Check first point
                Rectangle hitArea = PadHitArea(line.Start);
                if (IsInsideRect(hitArea, point))
                {
                    this.Cursor = Cursors.SizeAll;

                    index = i;
                    tool = MeasurmentTool.Line;
                    hit = TrackerHit.hitStart;

                    return true;
                }

                // Check last point
                hitArea = PadHitArea(line.End);
                if (IsInsideRect(hitArea, point))
                {
                    this.Cursor = Cursors.SizeAll;

                    index = i;
                    tool = MeasurmentTool.Line;
                    hit = TrackerHit.hitEnd;

                    return true;
                }

                // Check if we hit the actual line
                Rectangle rc = new Rectangle(new Point(Math.Min(line.Start.X, line.End.X), Math.Min(line.Start.Y, line.End.Y)), new Size(Math.Abs(line.Start.X - line.End.X), Math.Abs(line.Start.Y - line.End.Y)));
                if (IsInsideRect(rc, point))
                {
                    float dist = GetDistanceFromLine(line.Start, line.End, point);
                    if (dist < 5.0f && dist > -5.0f)
                    {
                        this.Cursor = Cursors.SizeAll;

                        index = i;
                        tool = MeasurmentTool.Line;
                        hit = TrackerHit.hitEdge;

                        return true;
                    }
                }

                i++;
            }

            i = 0;

            //////////////////////////////////////////////////////////////////////////
            // Check rectangles
            //////////////////////////////////////////////////////////////////////////
            foreach (MeasurementRectangle rect in _image.Measurements.MeasurementRectangles)
            {
                // Check upper left corner
                Rectangle hitArea = PadHitArea(rect.Location);
                if (IsInsideRect(hitArea, point))
                {
                    this.Cursor = Cursors.SizeNWSE;

                    index = i;
                    tool = MeasurmentTool.Area;
                    hit = TrackerHit.hitTopLeft;

                    return true;
                }

                // Check upper mid
                hitArea = PadHitArea(new Point(rect.Location.X + rect.Width / 2, rect.Location.Y));
                if (IsInsideRect(hitArea, point))
                {
                    this.Cursor = Cursors.SizeNS;

                    index = i;
                    tool = MeasurmentTool.Area;
                    hit = TrackerHit.hitTop;

                    return true;
                }

                // Check upper right
                hitArea = PadHitArea(new Point(rect.Location.X + rect.Width, rect.Location.Y));
                if (IsInsideRect(hitArea, point))
                {
                    this.Cursor = Cursors.SizeNESW;

                    index = i;
                    tool = MeasurmentTool.Area;
                    hit = TrackerHit.hitTopRight;

                    return true;
                }

                // Check mid right
                hitArea = PadHitArea(new Point(rect.Location.X + rect.Width, rect.Location.Y + rect.Height / 2));
                if (IsInsideRect(hitArea, point))
                {
                    this.Cursor = Cursors.SizeWE;

                    index = i;
                    tool = MeasurmentTool.Area;
                    hit = TrackerHit.hitRight;

                    return true;
                }

                // Check lower right
                hitArea = PadHitArea(new Point(rect.Location.X + rect.Width, rect.Location.Y + rect.Height));
                if (IsInsideRect(hitArea, point))
                {
                    this.Cursor = Cursors.SizeNWSE;

                    index = i;
                    tool = MeasurmentTool.Area;
                    hit = TrackerHit.hitBottomRight;

                    return true;
                }

                // Check lower mid
                hitArea = PadHitArea(new Point(rect.Location.X + rect.Width / 2, rect.Location.Y + rect.Height));
                if (IsInsideRect(hitArea, point))
                {
                    this.Cursor = Cursors.SizeNS;

                    index = i;
                    tool = MeasurmentTool.Area;
                    hit = TrackerHit.hitBottom;

                    return true;
                }

                // Check lower left
                hitArea = PadHitArea(new Point(rect.Location.X, rect.Location.Y + rect.Height));
                if (IsInsideRect(hitArea, point))
                {
                    this.Cursor = Cursors.SizeNESW;

                    index = i;
                    tool = MeasurmentTool.Area;
                    hit = TrackerHit.hitBottomLeft;

                    return true;
                }

                // Check left mid
                hitArea = PadHitArea(new Point(rect.Location.X, rect.Location.Y + rect.Height / 2));
                if (IsInsideRect(hitArea, point))
                {
                    this.Cursor = Cursors.SizeWE;

                    index = i;
                    tool = MeasurmentTool.Area;
                    hit = TrackerHit.hitLeft;

                    return true;
                }

                // Check mid
                if (IsInsideRect(new Rectangle(rect.Location, new Size(rect.Width, rect.Height)), point))
                {
                    this.Cursor = Cursors.SizeAll;

                    index = i;
                    tool = MeasurmentTool.Area;
                    hit = TrackerHit.hitMiddle;

                    return true;
                }
                i++;
            }

            this.Cursor = Cursors.Arrow;

            index = -1;
            tool = MeasurmentTool.None;
            hit = TrackerHit.hitNothing;

            return false;
        }

        /// <summary>
        /// Clip points against image boundaries.
        /// </summary>
        /// <param name="pos">Source point.</param>
        /// <returns>Clipped point.</returns>
        Point ClipPoint(Point pos)
        {
            return new Point(Math.Min(Math.Max(pos.X, 0), _image.Width - 1), Math.Min(Math.Max(pos.Y, 0), _image.Height - 1));
        }

        static Point AddPoints(Point pt1, Point pt2)
        {
            return new Point(pt1.X + pt2.X, pt1.Y + pt2.Y);
        }

        static Point SubPoints(Point pt1, Point pt2)
        {
            return new Point(pt1.X - pt2.X, pt1.Y - pt2.Y);
        }

        bool IsPassingMoveBoundaryX(Point pos)
        {
            if (pos.X > _tracker.prevPos.X)
            {
                // Moving right
                if (pos.X > _tracker.hitPos.X)
                {
                    return true;
                }
            }
            else
            {
                // Moving left
                if (pos.X < _tracker.hitPos.X)
                {
                    return true;
                }
            }
            return false;
        }

        bool IsPassingMoveBoundaryY(Point pos)
        {
            if (pos.Y < _tracker.prevPos.Y)
            {
                // Moving up
                if (pos.Y < _tracker.hitPos.Y)
                {
                    return true;
                }
            }
            else
            {
                // Moving down
                if (pos.Y > _tracker.hitPos.Y)
                {
                    return true;
                }
            }

            return false;
        }

        private Point ComputeDelta(Point upperLeft, Point lowerRight, Point pos)
        {
            Point delta = new Point();

            Rectangle imageRect = new Rectangle(0, 0, _image.Width, _image.Height);

            if (IsInsideRect(imageRect, pos))
            {
                // Cursor point is inside of the image 
                delta = SubPoints(pos, _tracker.prevPos);

                // Need to check against image boundaries and possibly re-calculate delta
                if (!IsInsideRect(imageRect, AddPoints(upperLeft, delta)) || !IsInsideRect(imageRect, AddPoints(lowerRight, delta)))
                {
                    Point imgTopLeft = new Point(0, 0);
                    Point imgBottomRight = new Point(_image.Width - 1, _image.Height - 1);

                    // Check the upper left coordinates and re-calculate the delta if needed
                    if (imgTopLeft.X > (upperLeft.X + delta.X))
                    {
                        delta.X = Math.Max(imgTopLeft.X, (upperLeft.X + delta.X));
                    }

                    if (imgTopLeft.Y > (upperLeft.Y + delta.Y))
                    {
                        delta.Y = Math.Max(imgTopLeft.Y, (upperLeft.Y + delta.Y));
                    }


                    // Check the lower left coordinates and re-calculate the delta if needed
                    if (imgBottomRight.X < (lowerRight.X + delta.X))
                    {
                        delta.X = Math.Min(0, (lowerRight.X + delta.X));
                    }

                    if (imgBottomRight.Y < (lowerRight.Y + delta.Y))
                    {
                        delta.Y = Math.Min(0, (lowerRight.Y + delta.Y));
                    }
                }
            }
            else
            {
                // Cursor point is outside of image

                Point imgTopLeft = new Point(0, 0);
                Point imgBottomRight = new Point(_image.Width - 1, _image.Height - 1);

                // Check the upper left coordinates and re-calculate the delta if needed


                if ((pos.X < imgTopLeft.X) && (pos.Y < imgTopLeft.Y))
                {
                    // Top left
                    delta = SubPoints(imgTopLeft, upperLeft);
                }
                else if ((pos.X > imgTopLeft.X) && (pos.X < imgBottomRight.X) && (pos.Y < imgTopLeft.Y))
                {
                    // Top
                    delta = SubPoints(pos, _tracker.prevPos);

                    if ((upperLeft.X + delta.X) < imgTopLeft.X)
                    {
                        delta.X = imgTopLeft.X - upperLeft.X;
                    }

                    if ((lowerRight.X + delta.X) > imgBottomRight.X)
                    {
                        delta.X = imgBottomRight.X - lowerRight.X;
                    }

                    delta.Y = imgTopLeft.Y - upperLeft.Y;
                }
                else if ((pos.X > imgBottomRight.X) && (pos.Y < imgTopLeft.Y))
                {
                    // Top right

                    delta.X = imgBottomRight.X - lowerRight.X;
                    delta.Y = imgTopLeft.Y - upperLeft.Y;
                }
                else if ((pos.X > imgBottomRight.X) && (pos.Y > imgTopLeft.Y) && (pos.Y < imgBottomRight.Y))
                {
                    // Right
                    delta = SubPoints(pos, _tracker.prevPos);

                    if ((upperLeft.Y + delta.Y) < imgTopLeft.Y)
                    {
                        delta.Y = imgTopLeft.Y - upperLeft.Y;
                    }

                    if ((lowerRight.Y + delta.Y) > imgBottomRight.Y)
                    {
                        delta.Y = imgBottomRight.Y - lowerRight.Y;
                    }

                    delta.X = imgBottomRight.X - lowerRight.X;
                }
                else if ((pos.X > imgBottomRight.X) && (pos.Y > imgBottomRight.Y))
                {
                    // Down right
                    delta = SubPoints(imgBottomRight, lowerRight);
                }
                else if ((pos.X > imgTopLeft.X) && (pos.X < imgBottomRight.X) && (pos.Y > imgBottomRight.Y))
                {
                    // Down
                    delta = SubPoints(pos, _tracker.prevPos);

                    if ((upperLeft.X + delta.X) < imgTopLeft.X)
                    {
                        delta.X = imgTopLeft.X - upperLeft.X;
                    }

                    if ((lowerRight.X + delta.X) > imgBottomRight.X)
                    {
                        delta.X = imgBottomRight.X - lowerRight.X;
                    }

                    delta.Y = imgBottomRight.Y - lowerRight.Y;
                }
                else if ((pos.X < imgTopLeft.X) && (pos.Y > imgBottomRight.Y))
                {
                    // Down left

                    delta.X = imgTopLeft.X - upperLeft.X;
                    delta.Y = imgBottomRight.Y - lowerRight.Y;
                }
                else if ((pos.X < imgTopLeft.X) && (pos.Y > imgTopLeft.Y) && (pos.Y < imgBottomRight.Y))
                {
                    // Left 

                    delta = SubPoints(pos, _tracker.prevPos);

                    if ((upperLeft.Y + delta.Y) < imgTopLeft.Y)
                    {
                        delta.Y = imgTopLeft.Y - upperLeft.Y;
                    }

                    if ((lowerRight.Y + delta.Y) > imgBottomRight.Y)
                    {
                        delta.Y = imgBottomRight.Y - lowerRight.Y;
                    }

                    delta.X = imgTopLeft.X - upperLeft.X;
                }
            }

            // Check if we're allowed to move
            if (!IsPassingMoveBoundaryX(pos))
            {
                delta.X = 0;
            }

            if (!IsPassingMoveBoundaryY(pos))
            {
                delta.Y = 0;
            }

            return delta;
        }

        private void TrackSymbol(Point point)
        {
            if (_tracker.prevPos.X == point.X && _tracker.prevPos.Y == point.Y)
            {
                return;
            }

            Rectangle imageRect = new Rectangle(0, 0, _image.Width, _image.Height);

            if (_tracker.tool == MeasurmentTool.Spot)
            {
                MeasurementSpot spot = _image.Measurements.MeasurementSpots[_tracker.index];

                if (IsInsideRect(imageRect, point))
                {
                    spot.X = point.X;
                    spot.Y = point.Y;
                }
                else
                {
                    // Clip against boundaries
                    Point pt = ClipPoint(point);
                    spot.X = pt.X;
                    spot.Y = pt.Y;
                }
            }
            else if (_tracker.tool == MeasurmentTool.Area)
            {
                MeasurementRectangle rect = _image.Measurements.MeasurementRectangles[_tracker.index];
                Point delta = ComputeDelta(rect.Location, new Point(rect.Location.X + rect.Width - 1, rect.Location.Y + rect.Height - 1), point);

                if (_tracker.tracker == TrackerHit.hitTopLeft)
                {
                    rect.Location = new Point(rect.Location.X + delta.X, rect.Location.Y + delta.Y);

                    rect.Width -= delta.X;
                    rect.Height -= delta.Y;

                    if (rect.Width < 0 && rect.Height < 0)
                    {
                        rect.Width = Math.Abs(rect.Width);
                        rect.Height = Math.Abs(rect.Height);

                        _tracker.tracker = TrackerHit.hitBottomRight;
                    }
                    else if (rect.Width < 0)
                    {
                        rect.Width = Math.Abs(rect.Width);
                        _tracker.tracker = TrackerHit.hitTopRight;
                    }
                    else if (rect.Height < 0)
                    {
                        rect.Height = Math.Abs(rect.Height);
                        _tracker.tracker = TrackerHit.hitBottomLeft;
                    }
                }
                else if (_tracker.tracker == TrackerHit.hitTop)
                {
                    rect.Location = new Point(rect.Location.X, rect.Location.Y + delta.Y);
                    rect.Height -= delta.Y;

                    if (rect.Height < 0)
                    {
                        rect.Height = Math.Abs(rect.Height);
                        _tracker.tracker = TrackerHit.hitBottom;
                    }
                }
                else if (_tracker.tracker == TrackerHit.hitTopRight)
                {
                    rect.Location = new Point(rect.Location.X, rect.Location.Y + delta.Y);
                    rect.Width += delta.X;
                    rect.Height -= delta.Y;

                    if (rect.Width < 0 && rect.Height < 0)
                    {
                        rect.Width = Math.Abs(rect.Width);
                        rect.Height = Math.Abs(rect.Height);

                        _tracker.tracker = TrackerHit.hitBottomLeft;
                    }
                    else if (rect.Width < 0)
                    {
                        rect.Width = Math.Abs(rect.Width);
                        _tracker.tracker = TrackerHit.hitTopLeft;
                    }
                    else if (rect.Height < 0)
                    {
                        rect.Height = Math.Abs(rect.Height);
                        _tracker.tracker = TrackerHit.hitBottomRight;
                    }
                }
                else if (_tracker.tracker == TrackerHit.hitRight)
                {
                    rect.Width += delta.X;

                    if (rect.Width < 0)
                    {
                        rect.Width = Math.Abs(rect.Width);
                        _tracker.tracker = TrackerHit.hitLeft;
                    }
                }
                else if (_tracker.tracker == TrackerHit.hitBottomRight)
                {
                    rect.Width += delta.X;
                    rect.Height += delta.Y;

                    if (rect.Width < 0 && rect.Height < 0)
                    {
                        rect.Width = Math.Abs(rect.Width);
                        rect.Height = Math.Abs(rect.Height);

                        _tracker.tracker = TrackerHit.hitTopLeft;
                    }
                    else if (rect.Width < 0)
                    {
                        rect.Width = Math.Abs(rect.Width);
                        _tracker.tracker = TrackerHit.hitBottomLeft;
                    }
                    else if (rect.Height < 0)
                    {
                        rect.Height = Math.Abs(rect.Height);
                        _tracker.tracker = TrackerHit.hitTopRight;
                    }
                }
                else if (_tracker.tracker == TrackerHit.hitBottom)
                {
                    rect.Height += delta.Y;

                    if (rect.Height < 0)
                    {
                        rect.Height = Math.Abs(rect.Height);
                        _tracker.tracker = TrackerHit.hitTop;
                    }
                }
                else if (_tracker.tracker == TrackerHit.hitBottomLeft)
                {
                    rect.Location = new Point(rect.Location.X + delta.X, rect.Location.Y);
                    rect.Width -= delta.X;
                    rect.Height += delta.Y;

                    if (rect.Width < 0 && rect.Height < 0)
                    {
                        rect.Width = Math.Abs(rect.Width);
                        rect.Height = Math.Abs(rect.Height);

                        _tracker.tracker = TrackerHit.hitTopRight;
                    }
                    else if (rect.Width < 0)
                    {
                        rect.Width = Math.Abs(rect.Width);
                        _tracker.tracker = TrackerHit.hitBottomRight;
                    }
                    else if (rect.Height < 0)
                    {
                        rect.Height = Math.Abs(rect.Height);
                        _tracker.tracker = TrackerHit.hitTopLeft;
                    }
                }
                else if (_tracker.tracker == TrackerHit.hitLeft)
                {
                    rect.Location = new Point(rect.Location.X + delta.X, rect.Location.Y);
                    rect.Width -= delta.X;

                    if (rect.Width < 0)
                    {
                        rect.Width = Math.Abs(rect.Width);
                        _tracker.tracker = TrackerHit.hitRight;
                    }
                }
                else if (_tracker.tracker == TrackerHit.hitMiddle)
                {
                    rect.Location = new Point(rect.Location.X + delta.X, rect.Location.Y + delta.Y);
                }

                _tracker.hitPos = AddPoints(_tracker.hitPos, delta);

            }
            else if (_tracker.tool == MeasurmentTool.Line)
            {
                MeasurementLine line = _image.Measurements.MeasurementLines[_tracker.index];

                if (_tracker.tracker == TrackerHit.hitStart)
                {
                    line.Start = ClipPoint(point);
                }
                else if (_tracker.tracker == TrackerHit.hitEnd)
                {
                    line.End = ClipPoint(point);
                }
                else
                {
                    Point upperLeft = new Point(Math.Min(line.Start.X, line.End.X), Math.Min(line.Start.Y, line.End.Y));
                    Point lowerRight = new Point(upperLeft.X + Math.Abs(line.Start.X - line.End.X), upperLeft.Y + Math.Abs(line.Start.Y - line.End.Y));

                    Point delta = ComputeDelta(upperLeft, lowerRight, point);

                    //Point delta = new Point(point.X - _tracker.prevPos.X, point.Y - _tracker.prevPos.Y);

                    Point start = new Point(line.Start.X + delta.X, line.Start.Y + delta.Y);
                    Point end = new Point(line.End.X + delta.X, line.End.Y + delta.Y);

                    line.Start = start;
                    line.End = end;

                    _tracker.hitPos = AddPoints(_tracker.hitPos, delta);
                }
            }

            _tracker.prevPos = point;

            Update();
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            Point location = e.Location;

            GainOffset gainOffset = new GainOffset(pictureBox1.ClientRectangle, _image);
            Point point = gainOffset.LogicalToImage(e.Location);

            if (_delete)
            {
                this.Cursor = Cursors.Cross;
            }
            else if (_currentTool == MeasurmentTool.FlyingSpot)
            {
                string output;
                var offsetX = 10;
                var offsetY = -20;
                location.Offset(new Point(offsetX, offsetY));
                if (point.X >= 0 && point.X < _image.Width && point.Y >= 0 && point.Y < _image.Height)
                {
                    ThermalValue value = _image.GetValueAt(point);

                    Cursor = Cursors.Cross;
                    output = string.Format("Value ={2}, X={0}, Y={1}", point.X, point.Y, value.Value);    
                }
                else
                {
                    output = string.Format("Value ={2}, X={0}, Y={1}", point.X, point.Y, "N/A");
                }
                _tooltip.Show(output, pictureBox1, location);
            }
            else
            {
                if (!_tracker.isTracking)
                {
                    int i = 0;
                    MeasurmentTool tool = MeasurmentTool.None;
                    TrackerHit hit = TrackerHit.hitNothing;
                    HitTest(point, ref i, ref tool, ref hit);

                    if (_currentTool == MeasurmentTool.None)
                    {
                        toolStripButtonSelect.Checked = true;
                    }
                }
                else
                {
                    TrackSymbol(point);
                    toolStripButtonSelect.Checked = true;
                }
            }
        }

        private void pictureBox1_MouseLeave(object sender, EventArgs e)
        {
            _tooltip.Hide(pictureBox1);
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Point location = e.Location;

            GainOffset gainOffset = new GainOffset(pictureBox1.ClientRectangle, _image);
            Point point = gainOffset.LogicalToImage(e.Location);

            int i = 0;
            MeasurmentTool tool = MeasurmentTool.None;
            TrackerHit hit = TrackerHit.hitNothing;

            if (_delete)
            {
                toolStripButtonArea.Checked = false;
                toolStripButtonLine.Checked = false;
                toolStripButtonPolyLine.Checked = false;
                toolStripButtonSpot.Checked = false;
                markerToolStripButton.Checked = false;
                toolStripButton1.Checked = false;

                if (HitTest(point, ref i, ref tool, ref hit))
                {
                    if (tool == MeasurmentTool.Spot)
                    {
                        _image.Measurements.Remove(_image.Measurements.MeasurementSpots[i]);
                    }
                    else if (tool == MeasurmentTool.Line)
                    {
                        _image.Measurements.Remove(_image.Measurements.MeasurementLines[i]);
                    }
                    else if (tool == MeasurmentTool.Area)
                    {
                        _image.Measurements.Remove(_image.Measurements.MeasurementRectangles[i]);
                    }
                }

                _currentTool = MeasurmentTool.None;
                _delete = false;
            }

            if (_adding)
            {
                toolStripButtonArea.Checked = false;
                toolStripButtonLine.Checked = false;
                toolStripButtonPolyLine.Checked = false;
                toolStripButtonSpot.Checked = false;
                markerToolStripButton.Checked = false;
                toolStripButton1.Checked = false;

                switch (_currentTool)
                {
                    case MeasurmentTool.None:
                        break;

                    case MeasurmentTool.Spot:
                        _image.Measurements.Add(point);
                        _adding = false;
                        break;

                    case MeasurmentTool.FlyingSpot:
                        _image.Measurements.Add(point);
                        _tooltip.Hide(pictureBox1);
                        _adding = false;
                        break;

                    case MeasurmentTool.Area:
                        Rectangle rect = new Rectangle(point, new Size(1, 1));
                        _image.Measurements.Add(rect);
                        _adding = false;
                        break;

                    case MeasurmentTool.Line:
                        Point p2 = point;
                        p2.Offset(1, 1);
                        _image.Measurements.Add(point, p2);
                        _adding = false;
                        break;
                    default:
                        break;
                }
                _currentTool = MeasurmentTool.None;
            }

            if (HitTest(point, ref i, ref tool, ref hit))
            {
                _tracker.isTracking = true;
                _tracker.index = i;
                _tracker.tool = tool;
                _tracker.tracker = hit;
                _tracker.prevPos = point;
                _tracker.hitPos = point;

                toolStripButtonSelect.Checked = false;
            }
            else
            {
                toolStripButtonSelect.Checked = true;
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            _tracker.Reset();
        }

        // Hit-Test codes
        private enum TrackerHit
        {
            hitNothing = -1,
            hitTopLeft = 0,
            hitTopRight = 1,
            hitBottomRight = 2,
            hitBottomLeft = 3,
            hitTop = 4,
            hitRight = 5,
            hitBottom = 6,
            hitLeft = 7,
            hitMiddle = 8,
            hitEdge = 9,
            hitStart = 10,
            hitEnd = 11
        };

        private bool _adding = false;
        private bool _delete = false;

        private enum MeasurmentTool
        {
            Spot,
            Area,
            Line,
            PolyLine,
            Marker,
            FlyingSpot,
            None
        }
        private MeasurmentTool _currentTool = MeasurmentTool.None;

        private class MeasTracker
        {
            public MeasTracker()
            {
                Reset();
            }

            public void Reset()
            {
                isTracking = false;
                index = -1;
                tool = MeasurmentTool.None;
                tracker = TrackerHit.hitNothing;
                prevPos = new Point(0, 0);
                hitPos = new Point(0, 0);
            }

            public bool isTracking;
            public int index;
            public MeasurmentTool tool;
            public TrackerHit tracker;
            public Point prevPos = new Point(0, 0);
            public Point hitPos = new Point(0, 0);
        }
        private MeasTracker _tracker = new MeasTracker();

        #endregion

        #region Palette

        private void paletteToolStripComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (guiIsUpdating)
            {
                return;
            }

            SetPalette(paletteToolStripComboBox.SelectedItem as string);
        }

        private void SetPalette(string palette)
        {
            if (palette == "Open...")
            {
                OpenFileDialog dlg = new OpenFileDialog();
                dlg.DefaultExt = "*.pal";
                if (dlg.ShowDialog() == DialogResult.OK)
                {
                    Palette pal = PaletteManager.Open(dlg.FileName);
                    _image.Palette = pal;
                    guiIsUpdating = true;
                    paletteToolStripComboBox.SelectedItem = "Custom";
                    guiIsUpdating = false;
                }
            }
            else if (palette == "Custom" && _image.PaletteManager.FromImage != null)
            {
                _image.Palette = _image.PaletteManager.FromImage;
            }
            else
            {
                for (int i = 0; i < PaletteManager.Palettes.Count; i++)
                {
                    if (palette == PaletteManager.Palettes[i].Name)
                    {
                        _image.Palette = PaletteManager.Palettes[i];
                        break;
                    }
                }
            }


            pictureBox1.Image = Image();
            UpdateScale();
        }

        private void paletteToolStripButton_Click(object sender, EventArgs e)
        {
            paletteToolStripButton.Checked = !paletteToolStripButton.Checked;
            _image.Palette.IsInverted = paletteToolStripButton.Checked;

            pictureBox1.Image = Image();
            UpdateScale();
        }



        #endregion

        #region Voice Annotations

        private void buttonPlay_Click(object sender, EventArgs e)
        {
            if (_image.VoiceAnnotation != null)
            {
                if (string.IsNullOrEmpty(_voiceAnnotationFileName))
                {
                    _voiceAnnotationFileName = Path.GetTempFileName();
                    FileStream fis = new FileStream(_voiceAnnotationFileName, FileMode.OpenOrCreate, FileAccess.Write);
                    fis.Write(_image.VoiceAnnotation.Data, 0, _image.VoiceAnnotation.Data.Length);
                    fis.Close();
                }
                _player.Play(_voiceAnnotationFileName, this);
                buttonPlay.Enabled = false;
                buttonStop.Enabled = true;
                buttonPause.Enabled = true;
            }
        }

        private void buttonPause_Click(object sender, EventArgs e)
        {
            _player.Pause();
            buttonPlay.Enabled = true;
            buttonStop.Enabled = true;
            buttonPause.Enabled = false;
        }

        private void buttonStop_Click(object sender, EventArgs e)
        {
            _player.Stop();
            buttonPlay.Enabled = true;
            buttonStop.Enabled = false;
            buttonPause.Enabled = false;
        }

        private void EnableVoiceAnnotation()
        {
            if (!_player.IsPlaying)
            {
                buttonPlay.Enabled = _image.VoiceAnnotation != null;
                buttonStop.Enabled = false;
                buttonPause.Enabled = false;
            }
        }

        private void CleanUpVoiceAnnotation()
        {
            if (string.IsNullOrEmpty(_voiceAnnotationFileName) == false)
            {
                try
                {
                    File.Delete(_voiceAnnotationFileName);
                }
                catch (Exception ex)
                {
                    DisplayErrorMessage(String.Format("An error occurred when trying to clean up voice annotations: \n\n{0}", ex.ToString()), ex);
                }
                _voiceAnnotationFileName = string.Empty;
            }
        }

        #endregion

        #region Alarms

        private void listViewAlarm_ItemSelectionChanged(object sender, ListViewItemSelectionChangedEventArgs e)
        {
            if (e.Item.Tag != null)
            {
                propertyGridAlarm.SelectedObject = e.Item.Tag;
            }
        }

        private void FillAlarm()
        {
            propertyGridAlarm.SelectedObject = null;
            listViewAlarm.Items.Clear();

            foreach (Alarm alarm in _image.Alarms)
            {
                AddAlarmToList(alarm);
            }

            if (listViewAlarm.Items.Count > 0)
            {
                propertyGridAlarm.SelectedObject = listViewAlarm.Items[0].Tag;
            }
        }
        private void AddAlarmToList(Alarm al)
        {
            ListViewItem item = new ListViewItem();
            item.Name = al.Name;
            item.Tag = al;
            item.Text = al.Name;
            item.SubItems.Add(al.GetType().ToString());
            listViewAlarm.Items.Add(item);
        }

        #endregion

        #region Methods

        void imageChanged(object sender, ImageChangedEventArgs e)
        {
            pictureBox1.Image = Image();
            UpdateScale();
        }

        void Scale_Changed(object sender, ScaleChangedEventArgs e)
        {
            UpdateScale();
            UpdateRangeSliderControl();
        }

        private void UpdateScale()
        {
            var bmp = new Bitmap(pictureBoxScale.ClientSize.Width, pictureBoxScale.ClientSize.Height);
            var scaleImage = _image.Scale.Image;
            using (var g = Graphics.FromImage(bmp))
            {
                //Use gdi+ to interpolate with nearest neighbor
                g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.NearestNeighbor;
                g.DrawImage(scaleImage, 0, 0, bmp.Width * 2, bmp.Height);
            }
            pictureBoxScale.Image = bmp;

            labelMax.Text = _image.Scale.Range.Maximum.ToString("F02");
            labelMin.Text = _image.Scale.Range.Minimum.ToString("F02");
        }

        private void UpdateRangeSliderControl()
        {
            ImageStatistics results = _image.Statistics;
            rangeSliderControl1.Set(results.Min.Value, results.Max.Value,
                _image.Scale.AutoAdjust.Minimum, _image.Scale.AutoAdjust.Maximum,
                _image.Scale.Range.Minimum, _image.Scale.Range.Maximum);
            rangeSliderControl1.Refresh();
        }

        private Bitmap Image()
        {
            Bitmap bitmap = null;
            
            bitmap = _image.Image;
            

            using (Graphics graphics = Graphics.FromImage(bitmap))
            {
                Overlay overlay = new Overlay(_image);
                overlay.Draw(graphics);
            }
            return bitmap;
        }

        #endregion

        #region Form override

        protected override void WndProc(ref Message m)
        {
            if (m.Msg == MediaPlayer.MM_MCINOTIFY)
            {
                EnableVoiceAnnotation();
            }
            base.WndProc(ref m);
        }
        protected override void OnFormClosing(FormClosingEventArgs e)
        {
            CleanUpVoiceAnnotation();
            CleanupIsotherms();
            base.OnFormClosing(e);
        }
        #endregion

        #region Object Parameters

        private void UpdateObjectParameters()
        {
            try
            {
                numericUpDownEmis.Value = (decimal)_image.ThermalParameters.Emissivity;

                numericUpDownReflTemp.Value = (decimal)_image.ThermalParameters.ReflectedTemperature;
                labelReflTemp.Text = _image.TemperatureUnit == TemperatureUnit.Celsius ? "°C" : "°F";

                numericUpDownDistance.Value = (decimal)_image.ThermalParameters.Distance;
                labelDist.Text = _image.DistanceUnit == DistanceUnit.Meter ? "m" : "ft";

                numericUpDownAtmTemp.Value = (decimal)_image.ThermalParameters.AtmosphericTemperature;
                labelAtmTemp.Text = _image.TemperatureUnit == TemperatureUnit.Celsius ? "°C" : "°F";

                numericUpDownRelHum.Value = (decimal)(_image.ThermalParameters.RelativeHumidity * 100);
            }
            catch (System.Exception)
            {

            }
        }

        private void numericUpDownEmis_ValueChanged(object sender, EventArgs e)
        {
            try
            {
                _image.ThermalParameters.Emissivity = (double)numericUpDownEmis.Value;
                Update();
            }
            catch (System.Exception)
            {

            }
        }

        private void numericUpDownReflTemp_ValueChanged(object sender, EventArgs e)
        {
            try
            {
                _image.ThermalParameters.ReflectedTemperature = (double)numericUpDownReflTemp.Value;
                Update();
            }
            catch (System.Exception)
            {

            }
        }

        private void numericUpDownDistance_ValueChanged(object sender, EventArgs e)
        {
            try
            {
                _image.ThermalParameters.Distance = (double)numericUpDownDistance.Value;
                Update();
            }
            catch (System.Exception)
            {

            }
        }

        private void numericUpDownAtmTemp_ValueChanged(object sender, EventArgs e)
        {
            try
            {
                _image.ThermalParameters.AtmosphericTemperature = (double)numericUpDownAtmTemp.Value;
                Update();
            }
            catch (System.Exception)
            {

            }
        }

        private void numericUpDownRelHum_ValueChanged(object sender, EventArgs e)
        {
            try
            {
                _image.ThermalParameters.RelativeHumidity = (double)numericUpDownRelHum.Value / 100.0;
                Update();
            }
            catch (System.Exception)
            {

            }
        }

        #endregion

        #region Isotherms

        private void CleanupIsotherms()
        {
            propertyGridIsotherms.SelectedObject = null;
            _image.Isotherms.Clear();
        }

        private void isoThermToolStripButton_Click(object sender, EventArgs e)
        {
            isoThermToolStripButton.Checked = !isoThermToolStripButton.Checked;
            isoThermToolStripComboBox.Enabled = isoThermToolStripButton.Checked;

            if (!isoThermToolStripButton.Checked)
            {
                _image.Isotherms.Clear();
            }

            ApplyIsothermAndUpdateImage();
        }

        private void isoThermToolStripComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (guiIsUpdating)
            {
                return;
            }

            ApplyIsothermAndUpdateImage();
        }

        private void ApplyIsothermAndUpdateImage()
        {
            if (isoThermToolStripButton.Checked)
            {
                _image.Isotherms.Clear();
                switch ((IsothermType)isoThermToolStripComboBox.SelectedItem)
                {
                    case IsothermType.Above:
                        _image.Isotherms.AddAbove();
                        break;
                    case IsothermType.Below:
                        _image.Isotherms.AddBelow();
                        break;
                    case IsothermType.Interval:
                        _image.Isotherms.AddInterval();
                        break;
                    default:
                        throw new ArgumentOutOfRangeException();
                }
            }

            FillIsotherms();
            DrawImageAndScale();
        }

        internal class IsothermTag
        {
            public IsothermTag(Isotherm iso)
            {
                _iso = iso;
            }

            public Appearance Appearance
            {
                get
                {
                    return _iso.Appearance;
                }

                set
                {
                    _iso.Appearance = value;
                }
            }

            public Color Color
            {
                get
                {
                    return _iso.Color;
                }

                set
                {
                    _iso.Color = value;
                }
            }

            public ContrastColor ContrastColor
            {
                get
                {
                    return _iso.ContrastColor;
                }

                set
                {
                    _iso.ContrastColor = value;
                }
            }

            public IsothermType Type
            {
                get
                {
                    return _iso.IsothermType;
                }
            }

            private Isotherm _iso;
        }

        private void DrawImageAndScale()
        {
            pictureBox1.Image = Image();
            UpdateScale();
        }

        private void FillIsotherms()
        {
            labelLevel.Text = _image.TemperatureUnit == TemperatureUnit.Celsius ? "°C" : "°F";
            labelwidth.Text = _image.TemperatureUnit == TemperatureUnit.Celsius ? "°C" : "°F";

            if (_image.Isotherms.Count > 0)
            {
                Isotherm iso = _image.Isotherms[0];

                propertyGridIsotherms.SelectedObject = new IsothermTag(iso);

                if (iso.IsothermType == IsothermType.Interval)
                {
                    IsothermInterval isothermInterval = (IsothermInterval) iso;
                    numericUpDownWidth.Enabled = true;
                    numericUpDownLevel.Enabled = true;

                    numericUpDownWidth.Value = (decimal)(Math.Abs(isothermInterval.Interval.Maximum - isothermInterval.Interval.Minimum));
                    numericUpDownLevel.Value = (decimal)(isothermInterval.Interval.Minimum);
                }
                else if (iso.IsothermType == IsothermType.Above)
                {
                    IsothermAbove isothermAbove = (IsothermAbove) iso;
                    var val = isothermAbove.Threshold;

                    numericUpDownLevel.Enabled = true;
                    numericUpDownWidth.Enabled = false;

                    numericUpDownLevel.Value = (decimal)val;
                }
                else // Below
                {
                    IsothermBelow isothermBelow = (IsothermBelow) iso;
                    var val = isothermBelow.Threshold;

                    numericUpDownLevel.Enabled = true;
                    numericUpDownWidth.Enabled = false;

                    numericUpDownLevel.Value = (decimal)val;
                }
            }
            else
            {
                propertyGridIsotherms.SelectedObject = null;
                numericUpDownWidth.Enabled = false;
                numericUpDownLevel.Enabled = false;
            }
        }

        private void numericUpDownLevel_ValueChanged(object sender, EventArgs e)
        {
            if (_image.Isotherms.Count > 0)
            {
                Isotherm iso = _image.Isotherms[0];

                double min = 0.0;
                double max = 0.0;

                if (iso.IsothermType == IsothermType.Interval)
                {
                    IsothermInterval isothermInterval = (IsothermInterval) iso;
                    isothermInterval.Interval = new Range<double>((double)numericUpDownLevel.Value, (double)numericUpDownLevel.Value + Math.Abs(max - min));
                }
                else if (iso.IsothermType == IsothermType.Above)
                {
                    IsothermAbove isothermAbove = (IsothermAbove) iso;
                    isothermAbove.Threshold = (double)numericUpDownLevel.Value;
                }
                else // Below
                {
                    IsothermBelow isothermBelow = (IsothermBelow)iso;
                    isothermBelow.Threshold = (double)numericUpDownLevel.Value;
                }

                DrawImageAndScale();
            }
        }

        private void numericUpDownWidth_ValueChanged(object sender, EventArgs e)
        {
            if (_image.Isotherms.Count > 0)
            {
                IsothermInterval iso = (IsothermInterval)_image.Isotherms[0];

                if (iso != null && iso.IsothermType == IsothermType.Interval)
                {
                    iso.Interval = new Range<double>(iso.Interval.Minimum, iso.Interval.Minimum + (double)numericUpDownWidth.Value);
                    DrawImageAndScale();
                }
            }
        }

        private void propertyGridIsotherms_PropertyValueChanged(object s, PropertyValueChangedEventArgs e)
        {
            FillIsotherms();
            DrawImageAndScale();
        }

        #endregion

        #region Text Annotations

        private void FillTextAnnotation()
        {
            if (_image.TextAnnotations == null)
            {
                // text annotations not supported
                return;
            }
            listViewTextAnnotations.Items.Clear();
            foreach (KeyValuePair<string,string> txt in _image.TextAnnotations)
            {
                ListViewItem item = new ListViewItem(txt.Key);
                item.Tag = txt;
                item.SubItems.Add(txt.Value);
                listViewTextAnnotations.Items.Add(item);
            }
        }

        private void listViewTextAnnotations_ItemSelectionChanged(object sender, ListViewItemSelectionChangedEventArgs e)
        {
            if (e.Item.Tag != null)
            {
                KeyValuePair<string,string> txt = (KeyValuePair<string,string>) e.Item.Tag;
                textBoxEditLabel.Text = txt.Key;
                textBoxEditValue.Text = txt.Value;
            }
            else
            {
                textBoxEditLabel.Text = "";
                textBoxEditValue.Text = "";
            }
        }

        private void buttonSetTextAnnotations_Click(object sender, EventArgs e)
        {
            if (textBoxEditValue.Text != "" && textBoxEditLabel.Text != "")
            {
                if (listViewTextAnnotations.SelectedItems.Count > 0)
                {
                    KeyValuePair<string, string> txt = (KeyValuePair<string, string>)listViewTextAnnotations.SelectedItems[0].Tag;

                    _image.TextAnnotations[txt.Key] = textBoxEditValue.Text;
                }
                
                FillTextAnnotation();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBoxLabel.Text != "")
            {
                _image.TextAnnotations.Add(textBoxLabel.Text, textBoxValue.Text);
                FillTextAnnotation();
            }
        }

        private void listViewTextAnnotations_KeyPress(object sender, KeyPressEventArgs e)
        {
        }

        private void listViewTextAnnotations_PreviewKeyDown(object sender, PreviewKeyDownEventArgs e)
        {
            if (e.KeyCode == Keys.Delete)
            {
                if (listViewTextAnnotations.SelectedIndices.Count > 0)
                {
                    ListView.SelectedListViewItemCollection items = listViewTextAnnotations.SelectedItems;
                    if (items.Count > 0)
                    {
                        ListViewItem item = items[0];
                        KeyValuePair<string, string> txt = (KeyValuePair<string, string>)item.Tag;
                        _image.TextAnnotations.Remove(txt.Key);
                        FillTextAnnotation();
                    }
                }
            }
        }

        #endregion

        #region Private Fields

        private bool guiIsUpdating = true;
        private ThermalImageFile _image = new ThermalImageFile();
        private ToolTip _tooltip = new ToolTip();

        private string _voiceAnnotationFileName = string.Empty;
        private MediaPlayer _player = new MediaPlayer();

        #endregion


        public object Measurement_Added { get; set; }

        private void rotateToolStripMenuItem_Click(object sender, EventArgs e)
        {
            _image.Rotate(90);
            pictureBox1.Image = Image();            
        }
    }
}
