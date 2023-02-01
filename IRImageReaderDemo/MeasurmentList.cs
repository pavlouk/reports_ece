using System.Drawing;
using System.Windows.Forms;
using Flir.Atlas.Image;
using Flir.Atlas.Image.Measurements;

namespace IRImageReaderDemo
{
    public class MeasurmentList : ListView
    {


        #region Construction

        public MeasurmentList()
        {
        }
        #endregion

        #region Private methods

        private ListViewItem FindMeasurementShape(MeasurementShape shape)
        {
            foreach (ListViewItem item in Items)
            {
                if (shape == item.Tag)
                    return item;
            }
            return null;
        }
        
        private ListViewItem CreateSpotListViewItem(MeasurementSpot spot)
        {
            if (spot == null)
                return null;
            ListViewItem item = new ListViewItem(spot.Name);
            item.SubItems.Add(spot.Value.Value.ToString("F2"));            
            item.SubItems.Add("---");
            item.SubItems.Add("---");
            item.SubItems.Add("---");
            item.SubItems.Add(spot.X.ToString());
            item.SubItems.Add(spot.Y.ToString());
            item.SubItems.Add("---");
            item.SubItems.Add("---");
            
            item.Tag = spot;
        
            return item;
        }

        private void UpdateSpotListViewItem(MeasurementSpot spot, ListViewItem item)
        {
            if (spot == null)
                return;
            item.Text = spot.Name;
            item.SubItems[1].Text = spot.Value.Value.ToString("F2");
            item.SubItems[5].Text =  spot.X.ToString();
            item.SubItems[6].Text = spot.Y.ToString();
            item.Tag = spot;
        }       

        private ListViewItem CreateAreaListViewItem(MeasurementRectangle rectangle)
        {
           if (rectangle == null)
                return null;
             ListViewItem item = new ListViewItem(rectangle.Name);
            item.SubItems.Add("---");
            item.SubItems.Add(rectangle.Min.Value.ToString("F2"));
            item.SubItems.Add(rectangle.Max.Value.ToString("F2"));
            item.SubItems.Add(rectangle.Average.Value.ToString("F2"));
            item.SubItems.Add(rectangle.Location.X.ToString());
            item.SubItems.Add(rectangle.Location.Y.ToString());
            item.SubItems.Add(rectangle.Width.ToString());
            item.SubItems.Add(rectangle.Height.ToString());
            item.Tag = rectangle;
        
            return item;
        }

       private void UpdateAreaListViewItem(MeasurementRectangle rectangle, ListViewItem item)
        {
            if (rectangle == null)
                return;
            item.Text = rectangle.Name;
            int index = 1;
            item.SubItems[index++].Text = "---";                        
            item.SubItems[index++].Text = rectangle.Min.Value.ToString("F2");
            item.SubItems[index++].Text = rectangle.Max.Value.ToString("F2");
            item.SubItems[index++].Text = rectangle.Average.Value.ToString("F2");
            item.SubItems[index++].Text = rectangle.Location.X.ToString();
            item.SubItems[index++].Text = rectangle.Location.Y.ToString();
            item.SubItems[index++].Text = rectangle.Width.ToString();
            item.SubItems[index++].Text = rectangle.Height.ToString();
            item.Tag = rectangle;
        }

        private ListViewItem CreateLineListViewItem(MeasurementLine line)
        {
            if (line == null)
                return null;
            ListViewItem item = new ListViewItem(line.Name);
            item.SubItems.Add("---");            
            item.SubItems.Add(line.Min.Value.ToString("F2"));
            item.SubItems.Add(line.Max.Value.ToString("F2"));
            item.SubItems.Add(line.Average.Value.ToString("F2"));
            item.SubItems.Add(line.Start.X.ToString());
            item.SubItems.Add(line.Start.Y.ToString());
            item.SubItems.Add(System.Math.Abs(line.End.X - line.Start.X).ToString());
            item.SubItems.Add(System.Math.Abs(line.End.Y - line.Start.Y).ToString());
            item.Tag = line;
        
            return item;
        }

        private void UpdateLineListViewItem(MeasurementLine line, ListViewItem item)
        {
            if (line == null)
                return;
            item.Text = line.Name;
            int index = 1;
            item.SubItems[index++].Text = "---";            
            item.SubItems[index++].Text = line.Min.Value.ToString("F2");
            item.SubItems[index++].Text = line.Max.Value.ToString("F2");
            item.SubItems[index++].Text = line.Average.Value.ToString("F2");
            item.SubItems[index++].Text = line.Start.X.ToString();
            item.SubItems[index++].Text = line.Start.Y.ToString();
            item.SubItems[index++].Text = System.Math.Abs(line.End.X - line.Start.X).ToString();
            item.SubItems[index++].Text = System.Math.Abs(line.End.Y - line.Start.Y).ToString();
            item.Tag = line;
        }

        
        #endregion

        #region Public methods

        public void AddSpot(MeasurementSpot spot)
        {
            if (spot == null)
                return;
            Items.Add(CreateSpotListViewItem(spot));
        }

        public void RemoveShape(MeasurementShape shape)
        {
            ListViewItem item = FindMeasurementShape(shape);
            if (item != null)
            {
                BeginUpdate();
                item.Remove();
                EndUpdate();
            }
        }

        public void UpdateSpot(MeasurementShape shape)
        {
            ListViewItem item = FindMeasurementShape(shape);
            if (item != null)
            {
                BeginUpdate();
                UpdateSpotListViewItem(item.Tag as MeasurementSpot, item);
                EndUpdate();
            }
        }

        public void AddArea(MeasurementRectangle rectangle)
        {
            if (rectangle == null)
                return;
            Items.Add(CreateAreaListViewItem(rectangle));
        }

        public void UpdateArea(MeasurementShape shape)
        {
            ListViewItem item = FindMeasurementShape(shape);
            if (item != null)
            {
                BeginUpdate();
                UpdateAreaListViewItem(item.Tag as MeasurementRectangle, item);
                EndUpdate();
            }
        }

        public void AddLine(MeasurementLine line)
        {
            if (line == null)
                return;
            Items.Add(CreateLineListViewItem(line));
        }

        public void UpdateLine(MeasurementShape shape)
        {
            ListViewItem item = FindMeasurementShape(shape);
            if (item != null)
            {
                BeginUpdate();
                UpdateLineListViewItem(item.Tag as MeasurementLine, item);
                EndUpdate();
            }
        }

        
        #endregion

        #region Protected override

        protected override void OnKeyDown(KeyEventArgs e)
        {
            if (e.Shift && SelectedItems.Count == 1)
            {
                MeasurementShape shape = SelectedItems[0].Tag as MeasurementShape;
                
                if (e.KeyCode == Keys.Left)
                {
                    shape.Offset(new Point(-1, 0));
                }
                else if (e.KeyCode == Keys.Right)
                {
                    shape.Offset(new Point(1, 0));
                }
                else if (e.KeyCode == Keys.Up)
                {
                    shape.Offset(new Point(0, -1));
                }
                else if (e.KeyCode == Keys.Down)
                {
                    shape.Offset(new Point(0, 1));
                }
                e.Handled = true;
                e.SuppressKeyPress = true;
            }
            else
                base.OnKeyDown(e);
        }
        #endregion
    }
}
