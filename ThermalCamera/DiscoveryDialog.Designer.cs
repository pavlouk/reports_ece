namespace DualCamera
{
    partial class DiscoveryDialog
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.staticIPToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.networkCameraToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.gigeVisionCameraToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.listViewDevices = new System.Windows.Forms.ListView();
            this.columnHeader1 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader2 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader3 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.checkBoxScanGige = new System.Windows.Forms.CheckBox();
            this.checkBoxEbus = new System.Windows.Forms.CheckBox();
            this.checkBoxAuthenticate = new System.Windows.Forms.CheckBox();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.ImageScalingSize = new System.Drawing.Size(24, 24);
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.staticIPToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Padding = new System.Windows.Forms.Padding(4, 1, 0, 1);
            this.menuStrip1.Size = new System.Drawing.Size(644, 24);
            this.menuStrip1.TabIndex = 2;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // staticIPToolStripMenuItem
            // 
            this.staticIPToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.networkCameraToolStripMenuItem,
            this.gigeVisionCameraToolStripMenuItem});
            this.staticIPToolStripMenuItem.Name = "staticIPToolStripMenuItem";
            this.staticIPToolStripMenuItem.Size = new System.Drawing.Size(61, 22);
            this.staticIPToolStripMenuItem.Text = "Static IP";
            // 
            // networkCameraToolStripMenuItem
            // 
            this.networkCameraToolStripMenuItem.Name = "networkCameraToolStripMenuItem";
            this.networkCameraToolStripMenuItem.Size = new System.Drawing.Size(181, 22);
            this.networkCameraToolStripMenuItem.Text = "Network camera...";
            this.networkCameraToolStripMenuItem.Click += new System.EventHandler(this.networkCameraToolStripMenuItem_Click);
            // 
            // gigeVisionCameraToolStripMenuItem
            // 
            this.gigeVisionCameraToolStripMenuItem.Name = "gigeVisionCameraToolStripMenuItem";
            this.gigeVisionCameraToolStripMenuItem.Size = new System.Drawing.Size(181, 22);
            this.gigeVisionCameraToolStripMenuItem.Text = "GigeVision camera...";
            this.gigeVisionCameraToolStripMenuItem.Click += new System.EventHandler(this.gigeVisionCameraToolStripMenuItem_Click);
            // 
            // listViewDevices
            // 
            this.listViewDevices.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.listViewDevices.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeader1,
            this.columnHeader2,
            this.columnHeader3});
            this.listViewDevices.HideSelection = false;
            this.listViewDevices.Location = new System.Drawing.Point(12, 40);
            this.listViewDevices.Name = "listViewDevices";
            this.listViewDevices.Size = new System.Drawing.Size(620, 217);
            this.listViewDevices.TabIndex = 3;
            this.listViewDevices.UseCompatibleStateImageBehavior = false;
            this.listViewDevices.View = System.Windows.Forms.View.Details;
            this.listViewDevices.MouseDoubleClick += new System.Windows.Forms.MouseEventHandler(this.listViewDevices_MouseDoubleClick);
            // 
            // columnHeader1
            // 
            this.columnHeader1.Text = "Name";
            this.columnHeader1.Width = 227;
            // 
            // columnHeader2
            // 
            this.columnHeader2.Text = "Device ID";
            this.columnHeader2.Width = 239;
            // 
            // columnHeader3
            // 
            this.columnHeader3.Text = "Interface";
            this.columnHeader3.Width = 120;
            // 
            // checkBoxScanGige
            // 
            this.checkBoxScanGige.AutoSize = true;
            this.checkBoxScanGige.Location = new System.Drawing.Point(12, 263);
            this.checkBoxScanGige.Name = "checkBoxScanGige";
            this.checkBoxScanGige.Size = new System.Drawing.Size(102, 17);
            this.checkBoxScanGige.TabIndex = 4;
            this.checkBoxScanGige.Text = "Scan Spinnaker";
            this.checkBoxScanGige.UseVisualStyleBackColor = true;
            this.checkBoxScanGige.CheckedChanged += new System.EventHandler(this.checkBoxScanGige_CheckedChanged);
            // 
            // checkBoxEbus
            // 
            this.checkBoxEbus.AutoSize = true;
            this.checkBoxEbus.Location = new System.Drawing.Point(12, 287);
            this.checkBoxEbus.Name = "checkBoxEbus";
            this.checkBoxEbus.Size = new System.Drawing.Size(83, 17);
            this.checkBoxEbus.TabIndex = 5;
            this.checkBoxEbus.Text = "Scan EBUS";
            this.checkBoxEbus.UseVisualStyleBackColor = true;
            this.checkBoxEbus.CheckedChanged += new System.EventHandler(this.checkBoxEbus_CheckedChanged);
            // 
            // checkBoxAuthenticate
            // 
            this.checkBoxAuthenticate.AutoSize = true;
            this.checkBoxAuthenticate.Checked = true;
            this.checkBoxAuthenticate.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBoxAuthenticate.Location = new System.Drawing.Point(120, 263);
            this.checkBoxAuthenticate.Name = "checkBoxAuthenticate";
            this.checkBoxAuthenticate.Size = new System.Drawing.Size(86, 17);
            this.checkBoxAuthenticate.TabIndex = 6;
            this.checkBoxAuthenticate.Text = "Authenticate";
            this.checkBoxAuthenticate.UseVisualStyleBackColor = true;
            // 
            // DiscoveryDialog
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(644, 307);
            this.Controls.Add(this.checkBoxAuthenticate);
            this.Controls.Add(this.checkBoxEbus);
            this.Controls.Add(this.checkBoxScanGige);
            this.Controls.Add(this.listViewDevices);
            this.Controls.Add(this.menuStrip1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "DiscoveryDialog";
            this.Text = "Discovery";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.DiscoveryDialog_FormClosing);
            this.Load += new System.EventHandler(this.DiscoveryDialog_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem staticIPToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem networkCameraToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem gigeVisionCameraToolStripMenuItem;
        private System.Windows.Forms.ListView listViewDevices;
        private System.Windows.Forms.ColumnHeader columnHeader1;
        private System.Windows.Forms.ColumnHeader columnHeader2;
        private System.Windows.Forms.ColumnHeader columnHeader3;
        private System.Windows.Forms.CheckBox checkBoxScanGige;
        private System.Windows.Forms.CheckBox checkBoxEbus;
        private System.Windows.Forms.CheckBox checkBoxAuthenticate;
    }
}