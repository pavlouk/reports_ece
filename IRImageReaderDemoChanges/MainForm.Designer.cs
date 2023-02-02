namespace IRImageReaderDemoChanges
{
    partial class MainForm
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
            if (disposing && (_image != null))
            {
                UnRegisterMeasurementEvent();
                _image.Dispose();
            }

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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.mainMenuStrip = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.openToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator5 = new System.Windows.Forms.ToolStripSeparator();
            this.saveToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveAsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.rotateToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.pictureBoxScale = new System.Windows.Forms.PictureBox();
            this.labelMax = new System.Windows.Forms.Label();
            this.labelMin = new System.Windows.Forms.Label();
            this.autoAdjustButton = new System.Windows.Forms.Button();
            this.toolStrip1 = new System.Windows.Forms.ToolStrip();
            this.toolStripButtonSave = new System.Windows.Forms.ToolStripButton();
            this.toolStripSeparator4 = new System.Windows.Forms.ToolStripSeparator();
            this.toolStripButtonSelect = new System.Windows.Forms.ToolStripButton();
            this.toolStripButtonSpot = new System.Windows.Forms.ToolStripButton();
            this.toolStripButtonFlyingSpot = new System.Windows.Forms.ToolStripButton();
            this.toolStripButtonArea = new System.Windows.Forms.ToolStripButton();
            this.toolStripButtonLine = new System.Windows.Forms.ToolStripButton();
            this.toolStripButton1 = new System.Windows.Forms.ToolStripButton();
            this.toolStripButtonPolyLine = new System.Windows.Forms.ToolStripButton();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.markerToolStripButton = new System.Windows.Forms.ToolStripButton();
            this.toolStripLabel1 = new System.Windows.Forms.ToolStripLabel();
            this.paletteToolStripComboBox = new System.Windows.Forms.ToolStripComboBox();
            this.paletteToolStripButton = new System.Windows.Forms.ToolStripButton();
            this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.isoThermToolStripButton = new System.Windows.Forms.ToolStripButton();
            this.isoThermToolStripComboBox = new System.Windows.Forms.ToolStripComboBox();
            this.toolStripSeparator3 = new System.Windows.Forms.ToolStripSeparator();
            this.toolStripLabel2 = new System.Windows.Forms.ToolStripLabel();
            this.toolStripComboBoxColorDist = new System.Windows.Forms.ToolStripComboBox();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage4 = new System.Windows.Forms.TabPage();
            this.label6 = new System.Windows.Forms.Label();
            this.labelAtmTemp = new System.Windows.Forms.Label();
            this.labelDist = new System.Windows.Forms.Label();
            this.labelReflTemp = new System.Windows.Forms.Label();
            this.numericUpDownRelHum = new System.Windows.Forms.NumericUpDown();
            this.numericUpDownAtmTemp = new System.Windows.Forms.NumericUpDown();
            this.numericUpDownDistance = new System.Windows.Forms.NumericUpDown();
            this.numericUpDownReflTemp = new System.Windows.Forms.NumericUpDown();
            this.numericUpDownEmis = new System.Windows.Forms.NumericUpDown();
            this.label5 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.propertyGrid1 = new System.Windows.Forms.PropertyGrid();
            this.tabPage5 = new System.Windows.Forms.TabPage();
            this.labelwidth = new System.Windows.Forms.Label();
            this.labelLevel = new System.Windows.Forms.Label();
            this.numericUpDownWidth = new System.Windows.Forms.NumericUpDown();
            this.numericUpDownLevel = new System.Windows.Forms.NumericUpDown();
            this.label10 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.propertyGridIsotherms = new System.Windows.Forms.PropertyGrid();
            this.buttonPause = new System.Windows.Forms.Button();
            this.buttonStop = new System.Windows.Forms.Button();
            this.buttonPlay = new System.Windows.Forms.Button();
            this.columnHeader10 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader11 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.listViewMeasurements = new IRImageReaderDemoChanges.MeasurmentList();
            this.columnHeader1 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader2 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader4 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader5 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader9 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader3 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader6 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader7 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader8 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.rangeSliderControl1 = new IRImageReaderDemoChanges.RangeSliderControl();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.mainMenuStrip.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxScale)).BeginInit();
            this.toolStrip1.SuspendLayout();
            this.tabControl1.SuspendLayout();
            this.tabPage4.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownRelHum)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownAtmTemp)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownDistance)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownReflTemp)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownEmis)).BeginInit();
            this.tabPage1.SuspendLayout();
            this.tabPage5.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownWidth)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownLevel)).BeginInit();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.SystemColors.Window;
            this.pictureBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBox1.Location = new System.Drawing.Point(12, 65);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(726, 502);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.MouseClick += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseClick);
            this.pictureBox1.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseDown);
            this.pictureBox1.MouseLeave += new System.EventHandler(this.pictureBox1_MouseLeave);
            this.pictureBox1.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseMove);
            this.pictureBox1.MouseUp += new System.Windows.Forms.MouseEventHandler(this.pictureBox1_MouseUp);
            // 
            // mainMenuStrip
            // 
            this.mainMenuStrip.ImageScalingSize = new System.Drawing.Size(24, 24);
            this.mainMenuStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.rotateToolStripMenuItem});
            this.mainMenuStrip.Location = new System.Drawing.Point(0, 0);
            this.mainMenuStrip.Name = "mainMenuStrip";
            this.mainMenuStrip.Size = new System.Drawing.Size(1130, 24);
            this.mainMenuStrip.TabIndex = 0;
            this.mainMenuStrip.Text = "mainMenuStrip";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.openToolStripMenuItem,
            this.toolStripSeparator5,
            this.saveToolStripMenuItem,
            this.saveAsToolStripMenuItem});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
            this.fileToolStripMenuItem.Text = "File";
            // 
            // openToolStripMenuItem
            // 
            this.openToolStripMenuItem.Name = "openToolStripMenuItem";
            this.openToolStripMenuItem.Size = new System.Drawing.Size(123, 22);
            this.openToolStripMenuItem.Text = "Open...";
            this.openToolStripMenuItem.Click += new System.EventHandler(this.openToolStripMenuItem_Click);
            // 
            // toolStripSeparator5
            // 
            this.toolStripSeparator5.Name = "toolStripSeparator5";
            this.toolStripSeparator5.Size = new System.Drawing.Size(120, 6);
            // 
            // saveToolStripMenuItem
            // 
            this.saveToolStripMenuItem.Name = "saveToolStripMenuItem";
            this.saveToolStripMenuItem.Size = new System.Drawing.Size(123, 22);
            this.saveToolStripMenuItem.Text = "Save...";
            this.saveToolStripMenuItem.Click += new System.EventHandler(this.saveToolStripMenuItem_Click);
            // 
            // saveAsToolStripMenuItem
            // 
            this.saveAsToolStripMenuItem.Name = "saveAsToolStripMenuItem";
            this.saveAsToolStripMenuItem.Size = new System.Drawing.Size(123, 22);
            this.saveAsToolStripMenuItem.Text = "Save As...";
            this.saveAsToolStripMenuItem.Click += new System.EventHandler(this.saveAsToolStripMenuItem_Click);
            // 
            // rotateToolStripMenuItem
            // 
            this.rotateToolStripMenuItem.Name = "rotateToolStripMenuItem";
            this.rotateToolStripMenuItem.Size = new System.Drawing.Size(53, 20);
            this.rotateToolStripMenuItem.Text = "Rotate";
            this.rotateToolStripMenuItem.Click += new System.EventHandler(this.rotateToolStripMenuItem_Click);
            // 
            // pictureBoxScale
            // 
            this.pictureBoxScale.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBoxScale.BackColor = System.Drawing.Color.White;
            this.pictureBoxScale.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBoxScale.Location = new System.Drawing.Point(751, 148);
            this.pictureBoxScale.Margin = new System.Windows.Forms.Padding(0);
            this.pictureBoxScale.Name = "pictureBoxScale";
            this.pictureBoxScale.Size = new System.Drawing.Size(30, 317);
            this.pictureBoxScale.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBoxScale.TabIndex = 4;
            this.pictureBoxScale.TabStop = false;
            // 
            // labelMax
            // 
            this.labelMax.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.labelMax.AutoSize = true;
            this.labelMax.Location = new System.Drawing.Point(743, 123);
            this.labelMax.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelMax.Name = "labelMax";
            this.labelMax.Size = new System.Drawing.Size(43, 13);
            this.labelMax.TabIndex = 5;
            this.labelMax.Text = "777777";
            this.labelMax.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // labelMin
            // 
            this.labelMin.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.labelMin.AutoSize = true;
            this.labelMin.Location = new System.Drawing.Point(743, 475);
            this.labelMin.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelMin.Name = "labelMin";
            this.labelMin.Size = new System.Drawing.Size(43, 13);
            this.labelMin.TabIndex = 6;
            this.labelMin.Text = "777777";
            this.labelMin.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // autoAdjustButton
            // 
            this.autoAdjustButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.autoAdjustButton.Location = new System.Drawing.Point(743, 573);
            this.autoAdjustButton.Name = "autoAdjustButton";
            this.autoAdjustButton.Size = new System.Drawing.Size(38, 30);
            this.autoAdjustButton.TabIndex = 8;
            this.autoAdjustButton.Text = "Auto";
            this.autoAdjustButton.UseVisualStyleBackColor = true;
            this.autoAdjustButton.Click += new System.EventHandler(this.autoAdjustButton_Click);
            // 
            // toolStrip1
            // 
            this.toolStrip1.ImageScalingSize = new System.Drawing.Size(24, 24);
            this.toolStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripButtonSave,
            this.toolStripSeparator4,
            this.toolStripButtonSelect,
            this.toolStripButtonSpot,
            this.toolStripButtonFlyingSpot,
            this.toolStripButtonArea,
            this.toolStripButtonLine,
            this.toolStripButton1,
            this.toolStripButtonPolyLine,
            this.toolStripSeparator1,
            this.markerToolStripButton,
            this.toolStripLabel1,
            this.paletteToolStripComboBox,
            this.paletteToolStripButton,
            this.toolStripSeparator2,
            this.isoThermToolStripButton,
            this.isoThermToolStripComboBox,
            this.toolStripSeparator3,
            this.toolStripLabel2,
            this.toolStripComboBoxColorDist});
            this.toolStrip1.Location = new System.Drawing.Point(0, 24);
            this.toolStrip1.Name = "toolStrip1";
            this.toolStrip1.Size = new System.Drawing.Size(1130, 31);
            this.toolStrip1.TabIndex = 9;
            this.toolStrip1.Text = "toolStrip1";
            // 
            // toolStripButtonSave
            // 
            this.toolStripButtonSave.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripButtonSave.Image = ((System.Drawing.Image)(resources.GetObject("toolStripButtonSave.Image")));
            this.toolStripButtonSave.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripButtonSave.Name = "toolStripButtonSave";
            this.toolStripButtonSave.Size = new System.Drawing.Size(28, 28);
            this.toolStripButtonSave.Text = "Save image";
            this.toolStripButtonSave.Click += new System.EventHandler(this.toolStripButtonSave_Click);
            // 
            // toolStripSeparator4
            // 
            this.toolStripSeparator4.Name = "toolStripSeparator4";
            this.toolStripSeparator4.Size = new System.Drawing.Size(6, 31);
            // 
            // toolStripButtonSelect
            // 
            this.toolStripButtonSelect.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripButtonSelect.Image = ((System.Drawing.Image)(resources.GetObject("toolStripButtonSelect.Image")));
            this.toolStripButtonSelect.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripButtonSelect.Name = "toolStripButtonSelect";
            this.toolStripButtonSelect.Size = new System.Drawing.Size(28, 28);
            this.toolStripButtonSelect.Text = "Select Tool";
            this.toolStripButtonSelect.Click += new System.EventHandler(this.toolStripButtonSelect_Click);
            // 
            // toolStripButtonSpot
            // 
            this.toolStripButtonSpot.CheckOnClick = true;
            this.toolStripButtonSpot.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripButtonSpot.Image = ((System.Drawing.Image)(resources.GetObject("toolStripButtonSpot.Image")));
            this.toolStripButtonSpot.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripButtonSpot.Name = "toolStripButtonSpot";
            this.toolStripButtonSpot.Size = new System.Drawing.Size(28, 28);
            this.toolStripButtonSpot.Text = "Spotmeter Tool";
            this.toolStripButtonSpot.Click += new System.EventHandler(this.toolStripButtonSpot_Click);
            // 
            // toolStripButtonFlyingSpot
            // 
            this.toolStripButtonFlyingSpot.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripButtonFlyingSpot.Image = ((System.Drawing.Image)(resources.GetObject("toolStripButtonFlyingSpot.Image")));
            this.toolStripButtonFlyingSpot.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripButtonFlyingSpot.Name = "toolStripButtonFlyingSpot";
            this.toolStripButtonFlyingSpot.Size = new System.Drawing.Size(28, 28);
            this.toolStripButtonFlyingSpot.Text = "Flying Spot Tool";
            this.toolStripButtonFlyingSpot.Click += new System.EventHandler(this.toolStripButtonFlyingSpot_Click);
            // 
            // toolStripButtonArea
            // 
            this.toolStripButtonArea.CheckOnClick = true;
            this.toolStripButtonArea.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripButtonArea.Image = ((System.Drawing.Image)(resources.GetObject("toolStripButtonArea.Image")));
            this.toolStripButtonArea.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripButtonArea.Name = "toolStripButtonArea";
            this.toolStripButtonArea.Size = new System.Drawing.Size(28, 28);
            this.toolStripButtonArea.Text = "Area Tool";
            this.toolStripButtonArea.Click += new System.EventHandler(this.toolStripButtonArea_Click);
            // 
            // toolStripButtonLine
            // 
            this.toolStripButtonLine.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripButtonLine.Image = ((System.Drawing.Image)(resources.GetObject("toolStripButtonLine.Image")));
            this.toolStripButtonLine.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripButtonLine.Name = "toolStripButtonLine";
            this.toolStripButtonLine.Size = new System.Drawing.Size(28, 28);
            this.toolStripButtonLine.Text = "Line Tool";
            this.toolStripButtonLine.Click += new System.EventHandler(this.toolStripButtonLine_Click);
            // 
            // toolStripButton1
            // 
            this.toolStripButton1.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripButton1.Image = ((System.Drawing.Image)(resources.GetObject("toolStripButton1.Image")));
            this.toolStripButton1.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripButton1.Name = "toolStripButton1";
            this.toolStripButton1.Size = new System.Drawing.Size(28, 28);
            this.toolStripButton1.Text = "Delete Tool";
            this.toolStripButton1.ToolTipText = "Delete Tool";
            this.toolStripButton1.Click += new System.EventHandler(this.toolStripButton1_Click);
            // 
            // toolStripButtonPolyLine
            // 
            this.toolStripButtonPolyLine.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripButtonPolyLine.Image = ((System.Drawing.Image)(resources.GetObject("toolStripButtonPolyLine.Image")));
            this.toolStripButtonPolyLine.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripButtonPolyLine.Name = "toolStripButtonPolyLine";
            this.toolStripButtonPolyLine.Size = new System.Drawing.Size(28, 28);
            this.toolStripButtonPolyLine.Text = "toolStripButtonPolyLine";
            this.toolStripButtonPolyLine.ToolTipText = "Add PolyLine";
            this.toolStripButtonPolyLine.Visible = false;
            this.toolStripButtonPolyLine.Click += new System.EventHandler(this.toolStripButtonPolyLine_Click);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(6, 31);
            // 
            // markerToolStripButton
            // 
            this.markerToolStripButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.markerToolStripButton.Image = ((System.Drawing.Image)(resources.GetObject("markerToolStripButton.Image")));
            this.markerToolStripButton.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.markerToolStripButton.Name = "markerToolStripButton";
            this.markerToolStripButton.Size = new System.Drawing.Size(28, 28);
            this.markerToolStripButton.Text = "markerToolStripButton";
            this.markerToolStripButton.ToolTipText = "Add Marker";
            this.markerToolStripButton.Visible = false;
            this.markerToolStripButton.Click += new System.EventHandler(this.markerToolStripButton_Click);
            // 
            // toolStripLabel1
            // 
            this.toolStripLabel1.Name = "toolStripLabel1";
            this.toolStripLabel1.Size = new System.Drawing.Size(43, 28);
            this.toolStripLabel1.Text = "Palette";
            // 
            // paletteToolStripComboBox
            // 
            this.paletteToolStripComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.paletteToolStripComboBox.Name = "paletteToolStripComboBox";
            this.paletteToolStripComboBox.Size = new System.Drawing.Size(121, 31);
            this.paletteToolStripComboBox.SelectedIndexChanged += new System.EventHandler(this.paletteToolStripComboBox_SelectedIndexChanged);
            // 
            // paletteToolStripButton
            // 
            this.paletteToolStripButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.paletteToolStripButton.Image = ((System.Drawing.Image)(resources.GetObject("paletteToolStripButton.Image")));
            this.paletteToolStripButton.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.paletteToolStripButton.Name = "paletteToolStripButton";
            this.paletteToolStripButton.Size = new System.Drawing.Size(54, 28);
            this.paletteToolStripButton.Text = "Inverted";
            this.paletteToolStripButton.Click += new System.EventHandler(this.paletteToolStripButton_Click);
            // 
            // toolStripSeparator2
            // 
            this.toolStripSeparator2.Name = "toolStripSeparator2";
            this.toolStripSeparator2.Size = new System.Drawing.Size(6, 31);
            // 
            // isoThermToolStripButton
            // 
            this.isoThermToolStripButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.isoThermToolStripButton.Image = ((System.Drawing.Image)(resources.GetObject("isoThermToolStripButton.Image")));
            this.isoThermToolStripButton.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.isoThermToolStripButton.Name = "isoThermToolStripButton";
            this.isoThermToolStripButton.Size = new System.Drawing.Size(58, 28);
            this.isoThermToolStripButton.Text = "Isotherm";
            this.isoThermToolStripButton.Click += new System.EventHandler(this.isoThermToolStripButton_Click);
            // 
            // isoThermToolStripComboBox
            // 
            this.isoThermToolStripComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.isoThermToolStripComboBox.Name = "isoThermToolStripComboBox";
            this.isoThermToolStripComboBox.Size = new System.Drawing.Size(121, 31);
            this.isoThermToolStripComboBox.SelectedIndexChanged += new System.EventHandler(this.isoThermToolStripComboBox_SelectedIndexChanged);
            // 
            // toolStripSeparator3
            // 
            this.toolStripSeparator3.Name = "toolStripSeparator3";
            this.toolStripSeparator3.Size = new System.Drawing.Size(6, 31);
            // 
            // toolStripLabel2
            // 
            this.toolStripLabel2.Name = "toolStripLabel2";
            this.toolStripLabel2.Size = new System.Drawing.Size(70, 28);
            this.toolStripLabel2.Text = "Color mode";
            // 
            // toolStripComboBoxColorDist
            // 
            this.toolStripComboBoxColorDist.AutoSize = false;
            this.toolStripComboBoxColorDist.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.toolStripComboBoxColorDist.DropDownWidth = 140;
            this.toolStripComboBoxColorDist.Name = "toolStripComboBoxColorDist";
            this.toolStripComboBoxColorDist.Size = new System.Drawing.Size(121, 23);
            // 
            // tabControl1
            // 
            this.tabControl1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tabControl1.Controls.Add(this.tabPage4);
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage5);
            this.tabControl1.Location = new System.Drawing.Point(802, 52);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(328, 677);
            this.tabControl1.TabIndex = 11;
            // 
            // tabPage4
            // 
            this.tabPage4.Controls.Add(this.label6);
            this.tabPage4.Controls.Add(this.labelAtmTemp);
            this.tabPage4.Controls.Add(this.labelDist);
            this.tabPage4.Controls.Add(this.labelReflTemp);
            this.tabPage4.Controls.Add(this.numericUpDownRelHum);
            this.tabPage4.Controls.Add(this.numericUpDownAtmTemp);
            this.tabPage4.Controls.Add(this.numericUpDownDistance);
            this.tabPage4.Controls.Add(this.numericUpDownReflTemp);
            this.tabPage4.Controls.Add(this.numericUpDownEmis);
            this.tabPage4.Controls.Add(this.label5);
            this.tabPage4.Controls.Add(this.label4);
            this.tabPage4.Controls.Add(this.label3);
            this.tabPage4.Controls.Add(this.label2);
            this.tabPage4.Controls.Add(this.label1);
            this.tabPage4.Location = new System.Drawing.Point(4, 22);
            this.tabPage4.Name = "tabPage4";
            this.tabPage4.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage4.Size = new System.Drawing.Size(320, 624);
            this.tabPage4.TabIndex = 3;
            this.tabPage4.Text = "Object Parameters";
            this.tabPage4.UseVisualStyleBackColor = true;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(184, 132);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(15, 13);
            this.label6.TabIndex = 13;
            this.label6.Text = "%";
            // 
            // labelAtmTemp
            // 
            this.labelAtmTemp.AutoSize = true;
            this.labelAtmTemp.Location = new System.Drawing.Point(184, 106);
            this.labelAtmTemp.Name = "labelAtmTemp";
            this.labelAtmTemp.Size = new System.Drawing.Size(18, 13);
            this.labelAtmTemp.TabIndex = 12;
            this.labelAtmTemp.Text = "°C";
            // 
            // labelDist
            // 
            this.labelDist.AutoSize = true;
            this.labelDist.Location = new System.Drawing.Point(184, 79);
            this.labelDist.Name = "labelDist";
            this.labelDist.Size = new System.Drawing.Size(15, 13);
            this.labelDist.TabIndex = 11;
            this.labelDist.Text = "m";
            // 
            // labelReflTemp
            // 
            this.labelReflTemp.AutoSize = true;
            this.labelReflTemp.Location = new System.Drawing.Point(184, 50);
            this.labelReflTemp.Name = "labelReflTemp";
            this.labelReflTemp.Size = new System.Drawing.Size(18, 13);
            this.labelReflTemp.TabIndex = 10;
            this.labelReflTemp.Text = "°C";
            // 
            // numericUpDownRelHum
            // 
            this.numericUpDownRelHum.DecimalPlaces = 1;
            this.numericUpDownRelHum.Location = new System.Drawing.Point(74, 129);
            this.numericUpDownRelHum.Name = "numericUpDownRelHum";
            this.numericUpDownRelHum.Size = new System.Drawing.Size(104, 20);
            this.numericUpDownRelHum.TabIndex = 9;
            this.numericUpDownRelHum.ValueChanged += new System.EventHandler(this.numericUpDownRelHum_ValueChanged);
            // 
            // numericUpDownAtmTemp
            // 
            this.numericUpDownAtmTemp.DecimalPlaces = 1;
            this.numericUpDownAtmTemp.Location = new System.Drawing.Point(74, 103);
            this.numericUpDownAtmTemp.Maximum = new decimal(new int[] {
            200,
            0,
            0,
            0});
            this.numericUpDownAtmTemp.Minimum = new decimal(new int[] {
            300,
            0,
            0,
            -2147483648});
            this.numericUpDownAtmTemp.Name = "numericUpDownAtmTemp";
            this.numericUpDownAtmTemp.Size = new System.Drawing.Size(104, 20);
            this.numericUpDownAtmTemp.TabIndex = 8;
            this.numericUpDownAtmTemp.ValueChanged += new System.EventHandler(this.numericUpDownAtmTemp_ValueChanged);
            // 
            // numericUpDownDistance
            // 
            this.numericUpDownDistance.DecimalPlaces = 1;
            this.numericUpDownDistance.Increment = new decimal(new int[] {
            5,
            0,
            0,
            65536});
            this.numericUpDownDistance.Location = new System.Drawing.Point(74, 75);
            this.numericUpDownDistance.Minimum = new decimal(new int[] {
            100,
            0,
            0,
            -2147483648});
            this.numericUpDownDistance.Name = "numericUpDownDistance";
            this.numericUpDownDistance.Size = new System.Drawing.Size(104, 20);
            this.numericUpDownDistance.TabIndex = 7;
            this.numericUpDownDistance.ValueChanged += new System.EventHandler(this.numericUpDownDistance_ValueChanged);
            // 
            // numericUpDownReflTemp
            // 
            this.numericUpDownReflTemp.DecimalPlaces = 1;
            this.numericUpDownReflTemp.Location = new System.Drawing.Point(74, 46);
            this.numericUpDownReflTemp.Maximum = new decimal(new int[] {
            200,
            0,
            0,
            0});
            this.numericUpDownReflTemp.Minimum = new decimal(new int[] {
            300,
            0,
            0,
            -2147483648});
            this.numericUpDownReflTemp.Name = "numericUpDownReflTemp";
            this.numericUpDownReflTemp.Size = new System.Drawing.Size(104, 20);
            this.numericUpDownReflTemp.TabIndex = 6;
            this.numericUpDownReflTemp.ValueChanged += new System.EventHandler(this.numericUpDownReflTemp_ValueChanged);
            // 
            // numericUpDownEmis
            // 
            this.numericUpDownEmis.DecimalPlaces = 2;
            this.numericUpDownEmis.Increment = new decimal(new int[] {
            1,
            0,
            0,
            65536});
            this.numericUpDownEmis.Location = new System.Drawing.Point(74, 18);
            this.numericUpDownEmis.Maximum = new decimal(new int[] {
            10,
            0,
            0,
            65536});
            this.numericUpDownEmis.Name = "numericUpDownEmis";
            this.numericUpDownEmis.Size = new System.Drawing.Size(104, 20);
            this.numericUpDownEmis.TabIndex = 5;
            this.numericUpDownEmis.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.numericUpDownEmis.ValueChanged += new System.EventHandler(this.numericUpDownEmis_ValueChanged);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(9, 78);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(49, 13);
            this.label5.TabIndex = 4;
            this.label5.Text = "Distance";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(8, 133);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(52, 13);
            this.label4.TabIndex = 3;
            this.label4.Text = "Rel. hum.";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(7, 106);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(57, 13);
            this.label3.TabIndex = 2;
            this.label3.Text = "Atm. temp.";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(6, 49);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(58, 13);
            this.label2.TabIndex = 1;
            this.label2.Text = "Refl. temp.";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 20);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(52, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Emissivity";
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.propertyGrid1);
            this.tabPage1.Location = new System.Drawing.Point(4, 22);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1.Size = new System.Drawing.Size(320, 651);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "Properties";
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // propertyGrid1
            // 
            this.propertyGrid1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.propertyGrid1.LineColor = System.Drawing.SystemColors.ControlDark;
            this.propertyGrid1.Location = new System.Drawing.Point(3, 6);
            this.propertyGrid1.Name = "propertyGrid1";
            this.propertyGrid1.Size = new System.Drawing.Size(310, 642);
            this.propertyGrid1.TabIndex = 4;
            // 
            // tabPage5
            // 
            this.tabPage5.Controls.Add(this.labelwidth);
            this.tabPage5.Controls.Add(this.labelLevel);
            this.tabPage5.Controls.Add(this.numericUpDownWidth);
            this.tabPage5.Controls.Add(this.numericUpDownLevel);
            this.tabPage5.Controls.Add(this.label10);
            this.tabPage5.Controls.Add(this.label9);
            this.tabPage5.Controls.Add(this.groupBox2);
            this.tabPage5.Location = new System.Drawing.Point(4, 22);
            this.tabPage5.Name = "tabPage5";
            this.tabPage5.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage5.Size = new System.Drawing.Size(320, 624);
            this.tabPage5.TabIndex = 4;
            this.tabPage5.Text = "Isotherms";
            this.tabPage5.UseVisualStyleBackColor = true;
            // 
            // labelwidth
            // 
            this.labelwidth.AutoSize = true;
            this.labelwidth.Location = new System.Drawing.Point(199, 159);
            this.labelwidth.Name = "labelwidth";
            this.labelwidth.Size = new System.Drawing.Size(18, 13);
            this.labelwidth.TabIndex = 7;
            this.labelwidth.Text = "°C";
            // 
            // labelLevel
            // 
            this.labelLevel.AutoSize = true;
            this.labelLevel.Location = new System.Drawing.Point(199, 133);
            this.labelLevel.Name = "labelLevel";
            this.labelLevel.Size = new System.Drawing.Size(18, 13);
            this.labelLevel.TabIndex = 6;
            this.labelLevel.Text = "°C";
            // 
            // numericUpDownWidth
            // 
            this.numericUpDownWidth.DecimalPlaces = 1;
            this.numericUpDownWidth.Location = new System.Drawing.Point(98, 156);
            this.numericUpDownWidth.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.numericUpDownWidth.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.numericUpDownWidth.Name = "numericUpDownWidth";
            this.numericUpDownWidth.Size = new System.Drawing.Size(94, 20);
            this.numericUpDownWidth.TabIndex = 5;
            this.numericUpDownWidth.Value = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.numericUpDownWidth.ValueChanged += new System.EventHandler(this.numericUpDownWidth_ValueChanged);
            // 
            // numericUpDownLevel
            // 
            this.numericUpDownLevel.DecimalPlaces = 1;
            this.numericUpDownLevel.Location = new System.Drawing.Point(98, 129);
            this.numericUpDownLevel.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.numericUpDownLevel.Minimum = new decimal(new int[] {
            273,
            0,
            0,
            -2147483648});
            this.numericUpDownLevel.Name = "numericUpDownLevel";
            this.numericUpDownLevel.Size = new System.Drawing.Size(94, 20);
            this.numericUpDownLevel.TabIndex = 4;
            this.numericUpDownLevel.ValueChanged += new System.EventHandler(this.numericUpDownLevel_ValueChanged);
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(15, 160);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(35, 13);
            this.label10.TabIndex = 3;
            this.label10.Text = "Width";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(15, 133);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(33, 13);
            this.label9.TabIndex = 2;
            this.label9.Text = "Level";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.propertyGridIsotherms);
            this.groupBox2.Location = new System.Drawing.Point(7, 6);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(305, 182);
            this.groupBox2.TabIndex = 9;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Isotherms";
            // 
            // propertyGridIsotherms
            // 
            this.propertyGridIsotherms.HelpVisible = false;
            this.propertyGridIsotherms.LineColor = System.Drawing.SystemColors.ControlDark;
            this.propertyGridIsotherms.Location = new System.Drawing.Point(6, 19);
            this.propertyGridIsotherms.Name = "propertyGridIsotherms";
            this.propertyGridIsotherms.Size = new System.Drawing.Size(293, 95);
            this.propertyGridIsotherms.TabIndex = 8;
            this.propertyGridIsotherms.ToolbarVisible = false;
            this.propertyGridIsotherms.PropertyValueChanged += new System.Windows.Forms.PropertyValueChangedEventHandler(this.propertyGridIsotherms_PropertyValueChanged);
            // 
            // buttonPause
            // 
            this.buttonPause.Location = new System.Drawing.Point(0, 0);
            this.buttonPause.Name = "buttonPause";
            this.buttonPause.Size = new System.Drawing.Size(75, 23);
            this.buttonPause.TabIndex = 0;
            // 
            // buttonStop
            // 
            this.buttonStop.Location = new System.Drawing.Point(0, 0);
            this.buttonStop.Name = "buttonStop";
            this.buttonStop.Size = new System.Drawing.Size(75, 23);
            this.buttonStop.TabIndex = 0;
            // 
            // buttonPlay
            // 
            this.buttonPlay.Location = new System.Drawing.Point(0, 0);
            this.buttonPlay.Name = "buttonPlay";
            this.buttonPlay.Size = new System.Drawing.Size(75, 23);
            this.buttonPlay.TabIndex = 0;
            // 
            // columnHeader10
            // 
            this.columnHeader10.Text = "Label";
            this.columnHeader10.Width = 66;
            // 
            // columnHeader11
            // 
            this.columnHeader11.Text = "Value";
            this.columnHeader11.Width = 220;
            // 
            // listViewMeasurements
            // 
            this.listViewMeasurements.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.listViewMeasurements.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeader1,
            this.columnHeader2,
            this.columnHeader4,
            this.columnHeader5,
            this.columnHeader9,
            this.columnHeader3,
            this.columnHeader6,
            this.columnHeader7,
            this.columnHeader8});
            this.listViewMeasurements.FullRowSelect = true;
            this.listViewMeasurements.HideSelection = false;
            this.listViewMeasurements.Location = new System.Drawing.Point(12, 609);
            this.listViewMeasurements.MultiSelect = false;
            this.listViewMeasurements.Name = "listViewMeasurements";
            this.listViewMeasurements.Size = new System.Drawing.Size(762, 123);
            this.listViewMeasurements.TabIndex = 10;
            this.listViewMeasurements.UseCompatibleStateImageBehavior = false;
            this.listViewMeasurements.View = System.Windows.Forms.View.Details;
            this.listViewMeasurements.KeyUp += new System.Windows.Forms.KeyEventHandler(this.listViewMeasurments_KeyUp);
            // 
            // columnHeader1
            // 
            this.columnHeader1.Text = "Name";
            // 
            // columnHeader2
            // 
            this.columnHeader2.Text = "Value";
            // 
            // columnHeader4
            // 
            this.columnHeader4.Text = "Min";
            // 
            // columnHeader5
            // 
            this.columnHeader5.Text = "Max";
            // 
            // columnHeader9
            // 
            this.columnHeader9.Text = "Average";
            // 
            // columnHeader3
            // 
            this.columnHeader3.Text = "X";
            this.columnHeader3.Width = 29;
            // 
            // columnHeader6
            // 
            this.columnHeader6.Text = "Y";
            this.columnHeader6.Width = 35;
            // 
            // columnHeader7
            // 
            this.columnHeader7.Text = "Width";
            // 
            // columnHeader8
            // 
            this.columnHeader8.Text = "Height";
            // 
            // rangeSliderControl1
            // 
            this.rangeSliderControl1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.rangeSliderControl1.BackColor = System.Drawing.Color.Transparent;
            this.rangeSliderControl1.Location = new System.Drawing.Point(12, 573);
            this.rangeSliderControl1.Name = "rangeSliderControl1";
            this.rangeSliderControl1.Size = new System.Drawing.Size(726, 30);
            this.rangeSliderControl1.TabIndex = 7;
            this.rangeSliderControl1.Text = "rangeSliderControl1";
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1130, 741);
            this.Controls.Add(this.listViewMeasurements);
            this.Controls.Add(this.toolStrip1);
            this.Controls.Add(this.autoAdjustButton);
            this.Controls.Add(this.rangeSliderControl1);
            this.Controls.Add(this.labelMin);
            this.Controls.Add(this.labelMax);
            this.Controls.Add(this.pictureBoxScale);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.mainMenuStrip);
            this.Controls.Add(this.tabControl1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MainMenuStrip = this.mainMenuStrip;
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Demo IRImageReader";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.mainMenuStrip.ResumeLayout(false);
            this.mainMenuStrip.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxScale)).EndInit();
            this.toolStrip1.ResumeLayout(false);
            this.toolStrip1.PerformLayout();
            this.tabControl1.ResumeLayout(false);
            this.tabPage4.ResumeLayout(false);
            this.tabPage4.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownRelHum)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownAtmTemp)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownDistance)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownReflTemp)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownEmis)).EndInit();
            this.tabPage1.ResumeLayout(false);
            this.tabPage5.ResumeLayout(false);
            this.tabPage5.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownWidth)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownLevel)).EndInit();
            this.groupBox2.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.MenuStrip mainMenuStrip;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem openToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem saveToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem saveAsToolStripMenuItem;
        private System.Windows.Forms.PictureBox pictureBoxScale;
        private System.Windows.Forms.Label labelMax;
        private System.Windows.Forms.Label labelMin;
        private RangeSliderControl rangeSliderControl1;
        private System.Windows.Forms.Button autoAdjustButton;
        private System.Windows.Forms.ToolStrip toolStrip1;
        private System.Windows.Forms.ToolStripButton toolStripButtonSpot;
        private System.Windows.Forms.ToolStripButton toolStripButtonArea;
        private System.Windows.Forms.ToolStripButton toolStripButtonLine;
        //private System.Windows.Forms.ListView listViewMeasurements;
        private MeasurmentList listViewMeasurements;
        private System.Windows.Forms.ColumnHeader columnHeader1;
        private System.Windows.Forms.ColumnHeader columnHeader2;
        private System.Windows.Forms.ColumnHeader columnHeader4;
        private System.Windows.Forms.ColumnHeader columnHeader5;
        private System.Windows.Forms.ColumnHeader columnHeader3;
        private System.Windows.Forms.ColumnHeader columnHeader6;
        private System.Windows.Forms.ColumnHeader columnHeader7;
        private System.Windows.Forms.ColumnHeader columnHeader8;
        private System.Windows.Forms.ColumnHeader columnHeader9;
        private System.Windows.Forms.ToolStripButton toolStripButtonPolyLine;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.PropertyGrid propertyGrid1;
        private System.Windows.Forms.Button buttonStop;
        private System.Windows.Forms.Button buttonPlay;
        private System.Windows.Forms.ColumnHeader columnHeader10;
        private System.Windows.Forms.ColumnHeader columnHeader11;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.ToolStripLabel toolStripLabel1;
        private System.Windows.Forms.ToolStripComboBox paletteToolStripComboBox;
        private System.Windows.Forms.ToolStripButton paletteToolStripButton;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
        private System.Windows.Forms.ToolStripButton markerToolStripButton;
        private System.Windows.Forms.ToolStripComboBox isoThermToolStripComboBox;
        private System.Windows.Forms.ToolStripButton isoThermToolStripButton;
        private System.Windows.Forms.ToolStripButton toolStripButtonFlyingSpot;
        private System.Windows.Forms.ToolStripButton toolStripButton1;
        private System.Windows.Forms.ToolStripButton toolStripButtonSave;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator4;
        private System.Windows.Forms.ToolStripButton toolStripButtonSelect;
        private System.Windows.Forms.TabPage tabPage4;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.NumericUpDown numericUpDownEmis;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label labelAtmTemp;
        private System.Windows.Forms.Label labelDist;
        private System.Windows.Forms.Label labelReflTemp;
        private System.Windows.Forms.NumericUpDown numericUpDownRelHum;
        private System.Windows.Forms.NumericUpDown numericUpDownAtmTemp;
        private System.Windows.Forms.NumericUpDown numericUpDownDistance;
        private System.Windows.Forms.NumericUpDown numericUpDownReflTemp;
        private System.Windows.Forms.Button buttonPause;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator5;
        private System.Windows.Forms.TabPage tabPage5;
        private System.Windows.Forms.NumericUpDown numericUpDownLevel;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label labelwidth;
        private System.Windows.Forms.Label labelLevel;
        private System.Windows.Forms.NumericUpDown numericUpDownWidth;
        private System.Windows.Forms.PropertyGrid propertyGridIsotherms;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator3;
        private System.Windows.Forms.ToolStripLabel toolStripLabel2;
        private System.Windows.Forms.ToolStripComboBox toolStripComboBoxColorDist;
        private System.Windows.Forms.ToolStripMenuItem rotateToolStripMenuItem;
    }
}

