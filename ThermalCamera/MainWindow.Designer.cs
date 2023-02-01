namespace Thermal_Camera
{
    partial class MainWindow
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
            this.cameraToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.discoveryToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.disconnectToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.toolStripStatusLabel1 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripConnectionStatus = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabel2 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripFps = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabel4 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripFrameCounter = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabel6 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripLostImages = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabel3 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabelErrorMessage = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabel5 = new System.Windows.Forms.ToolStripStatusLabel();
            this.pictureBoxThermal = new System.Windows.Forms.PictureBox();
            this.listBoxLogger = new System.Windows.Forms.ListBox();
            this.pictureBoxVisualImage = new System.Windows.Forms.PictureBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.labelSystemRunning = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.labelSystemMemory = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.labelSystemCpu = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.labelSystemStarted = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.labelCamInfoName = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.labelCamInfoIp = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.labelCamInfoSize = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.imageToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.frameRateToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.highestToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.halfToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem2 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem3 = new System.Windows.Forms.ToolStripMenuItem();
            this.disableToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cameraControl1 = new Thermal_Camera.CameraControl();
            this.measurementsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.addCenterRectangleToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip1.SuspendLayout();
            this.statusStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxThermal)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxVisualImage)).BeginInit();
            this.groupBox2.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.ImageScalingSize = new System.Drawing.Size(24, 24);
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.cameraToolStripMenuItem,
            this.imageToolStripMenuItem,
            this.measurementsToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(980, 24);
            this.menuStrip1.TabIndex = 1;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // cameraToolStripMenuItem
            // 
            this.cameraToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.discoveryToolStripMenuItem,
            this.disconnectToolStripMenuItem});
            this.cameraToolStripMenuItem.Name = "cameraToolStripMenuItem";
            this.cameraToolStripMenuItem.Size = new System.Drawing.Size(60, 20);
            this.cameraToolStripMenuItem.Text = "Camera";
            // 
            // discoveryToolStripMenuItem
            // 
            this.discoveryToolStripMenuItem.Name = "discoveryToolStripMenuItem";
            this.discoveryToolStripMenuItem.Size = new System.Drawing.Size(133, 22);
            this.discoveryToolStripMenuItem.Text = "Connect...";
            this.discoveryToolStripMenuItem.Click += new System.EventHandler(this.discoveryToolStripMenuItem_Click);
            // 
            // disconnectToolStripMenuItem
            // 
            this.disconnectToolStripMenuItem.Name = "disconnectToolStripMenuItem";
            this.disconnectToolStripMenuItem.Size = new System.Drawing.Size(133, 22);
            this.disconnectToolStripMenuItem.Text = "Disconnect";
            this.disconnectToolStripMenuItem.Click += new System.EventHandler(this.disconnectToolStripMenuItem_Click);
            // 
            // statusStrip1
            // 
            this.statusStrip1.ImageScalingSize = new System.Drawing.Size(24, 24);
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripStatusLabel1,
            this.toolStripConnectionStatus,
            this.toolStripStatusLabel2,
            this.toolStripFps,
            this.toolStripStatusLabel4,
            this.toolStripFrameCounter,
            this.toolStripStatusLabel6,
            this.toolStripLostImages,
            this.toolStripStatusLabel3,
            this.toolStripStatusLabelErrorMessage,
            this.toolStripStatusLabel5});
            this.statusStrip1.Location = new System.Drawing.Point(0, 538);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(980, 24);
            this.statusStrip1.TabIndex = 7;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // toolStripStatusLabel1
            // 
            this.toolStripStatusLabel1.Name = "toolStripStatusLabel1";
            this.toolStripStatusLabel1.Size = new System.Drawing.Size(39, 19);
            this.toolStripStatusLabel1.Text = "Status";
            // 
            // toolStripConnectionStatus
            // 
            this.toolStripConnectionStatus.BorderSides = ((System.Windows.Forms.ToolStripStatusLabelBorderSides)((((System.Windows.Forms.ToolStripStatusLabelBorderSides.Left | System.Windows.Forms.ToolStripStatusLabelBorderSides.Top) 
            | System.Windows.Forms.ToolStripStatusLabelBorderSides.Right) 
            | System.Windows.Forms.ToolStripStatusLabelBorderSides.Bottom)));
            this.toolStripConnectionStatus.BorderStyle = System.Windows.Forms.Border3DStyle.RaisedOuter;
            this.toolStripConnectionStatus.Name = "toolStripConnectionStatus";
            this.toolStripConnectionStatus.Size = new System.Drawing.Size(83, 19);
            this.toolStripConnectionStatus.Text = "Disconnected";
            // 
            // toolStripStatusLabel2
            // 
            this.toolStripStatusLabel2.Name = "toolStripStatusLabel2";
            this.toolStripStatusLabel2.Size = new System.Drawing.Size(25, 19);
            this.toolStripStatusLabel2.Text = "Fps";
            // 
            // toolStripFps
            // 
            this.toolStripFps.BorderSides = ((System.Windows.Forms.ToolStripStatusLabelBorderSides)((((System.Windows.Forms.ToolStripStatusLabelBorderSides.Left | System.Windows.Forms.ToolStripStatusLabelBorderSides.Top) 
            | System.Windows.Forms.ToolStripStatusLabelBorderSides.Right) 
            | System.Windows.Forms.ToolStripStatusLabelBorderSides.Bottom)));
            this.toolStripFps.BorderStyle = System.Windows.Forms.Border3DStyle.RaisedOuter;
            this.toolStripFps.Name = "toolStripFps";
            this.toolStripFps.Size = new System.Drawing.Size(26, 19);
            this.toolStripFps.Text = "0.0";
            // 
            // toolStripStatusLabel4
            // 
            this.toolStripStatusLabel4.Name = "toolStripStatusLabel4";
            this.toolStripStatusLabel4.Size = new System.Drawing.Size(84, 19);
            this.toolStripStatusLabel4.Text = "Frame counter";
            // 
            // toolStripFrameCounter
            // 
            this.toolStripFrameCounter.BorderSides = ((System.Windows.Forms.ToolStripStatusLabelBorderSides)((((System.Windows.Forms.ToolStripStatusLabelBorderSides.Left | System.Windows.Forms.ToolStripStatusLabelBorderSides.Top) 
            | System.Windows.Forms.ToolStripStatusLabelBorderSides.Right) 
            | System.Windows.Forms.ToolStripStatusLabelBorderSides.Bottom)));
            this.toolStripFrameCounter.BorderStyle = System.Windows.Forms.Border3DStyle.RaisedOuter;
            this.toolStripFrameCounter.Name = "toolStripFrameCounter";
            this.toolStripFrameCounter.Size = new System.Drawing.Size(35, 19);
            this.toolStripFrameCounter.Text = "0000";
            // 
            // toolStripStatusLabel6
            // 
            this.toolStripStatusLabel6.Name = "toolStripStatusLabel6";
            this.toolStripStatusLabel6.Size = new System.Drawing.Size(70, 19);
            this.toolStripStatusLabel6.Text = "Lost images";
            // 
            // toolStripLostImages
            // 
            this.toolStripLostImages.BorderSides = ((System.Windows.Forms.ToolStripStatusLabelBorderSides)((((System.Windows.Forms.ToolStripStatusLabelBorderSides.Left | System.Windows.Forms.ToolStripStatusLabelBorderSides.Top) 
            | System.Windows.Forms.ToolStripStatusLabelBorderSides.Right) 
            | System.Windows.Forms.ToolStripStatusLabelBorderSides.Bottom)));
            this.toolStripLostImages.BorderStyle = System.Windows.Forms.Border3DStyle.RaisedOuter;
            this.toolStripLostImages.Name = "toolStripLostImages";
            this.toolStripLostImages.Size = new System.Drawing.Size(35, 19);
            this.toolStripLostImages.Text = "0000";
            // 
            // toolStripStatusLabel3
            // 
            this.toolStripStatusLabel3.Name = "toolStripStatusLabel3";
            this.toolStripStatusLabel3.Size = new System.Drawing.Size(58, 19);
            this.toolStripStatusLabel3.Text = "Error Msg";
            // 
            // toolStripStatusLabelErrorMessage
            // 
            this.toolStripStatusLabelErrorMessage.Name = "toolStripStatusLabelErrorMessage";
            this.toolStripStatusLabelErrorMessage.Size = new System.Drawing.Size(0, 19);
            // 
            // toolStripStatusLabel5
            // 
            this.toolStripStatusLabel5.Name = "toolStripStatusLabel5";
            this.toolStripStatusLabel5.Size = new System.Drawing.Size(23, 19);
            this.toolStripStatusLabel5.Text = "OK";
            // 
            // pictureBoxThermal
            // 
            this.pictureBoxThermal.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBoxThermal.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBoxThermal.Location = new System.Drawing.Point(12, 27);
            this.pictureBoxThermal.Name = "pictureBoxThermal";
            this.pictureBoxThermal.Size = new System.Drawing.Size(616, 366);
            this.pictureBoxThermal.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBoxThermal.TabIndex = 8;
            this.pictureBoxThermal.TabStop = false;
            // 
            // listBoxLogger
            // 
            this.listBoxLogger.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.listBoxLogger.FormattingEnabled = true;
            this.listBoxLogger.Location = new System.Drawing.Point(9, 399);
            this.listBoxLogger.Name = "listBoxLogger";
            this.listBoxLogger.ScrollAlwaysVisible = true;
            this.listBoxLogger.Size = new System.Drawing.Size(620, 134);
            this.listBoxLogger.TabIndex = 9;
            // 
            // pictureBoxVisualImage
            // 
            this.pictureBoxVisualImage.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBoxVisualImage.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.pictureBoxVisualImage.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBoxVisualImage.Location = new System.Drawing.Point(638, 27);
            this.pictureBoxVisualImage.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.pictureBoxVisualImage.Name = "pictureBoxVisualImage";
            this.pictureBoxVisualImage.Size = new System.Drawing.Size(336, 205);
            this.pictureBoxVisualImage.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBoxVisualImage.TabIndex = 10;
            this.pictureBoxVisualImage.TabStop = false;
            // 
            // groupBox2
            // 
            this.groupBox2.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBox2.Controls.Add(this.labelSystemRunning);
            this.groupBox2.Controls.Add(this.label5);
            this.groupBox2.Controls.Add(this.labelSystemMemory);
            this.groupBox2.Controls.Add(this.label10);
            this.groupBox2.Controls.Add(this.labelSystemCpu);
            this.groupBox2.Controls.Add(this.label6);
            this.groupBox2.Controls.Add(this.labelSystemStarted);
            this.groupBox2.Controls.Add(this.label4);
            this.groupBox2.Location = new System.Drawing.Point(638, 463);
            this.groupBox2.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Padding = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.groupBox2.Size = new System.Drawing.Size(335, 75);
            this.groupBox2.TabIndex = 11;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "System";
            // 
            // labelSystemRunning
            // 
            this.labelSystemRunning.AutoSize = true;
            this.labelSystemRunning.Location = new System.Drawing.Point(71, 47);
            this.labelSystemRunning.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelSystemRunning.Name = "labelSystemRunning";
            this.labelSystemRunning.Size = new System.Drawing.Size(27, 13);
            this.labelSystemRunning.TabIndex = 1;
            this.labelSystemRunning.Text = "N/A";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(11, 47);
            this.label5.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(47, 13);
            this.label5.TabIndex = 0;
            this.label5.Text = "Running";
            // 
            // labelSystemMemory
            // 
            this.labelSystemMemory.AutoSize = true;
            this.labelSystemMemory.Location = new System.Drawing.Point(262, 47);
            this.labelSystemMemory.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelSystemMemory.Name = "labelSystemMemory";
            this.labelSystemMemory.Size = new System.Drawing.Size(27, 13);
            this.labelSystemMemory.TabIndex = 1;
            this.labelSystemMemory.Text = "N/A";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(215, 47);
            this.label10.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(44, 13);
            this.label10.TabIndex = 0;
            this.label10.Text = "Memory";
            // 
            // labelSystemCpu
            // 
            this.labelSystemCpu.AutoSize = true;
            this.labelSystemCpu.Location = new System.Drawing.Point(262, 23);
            this.labelSystemCpu.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelSystemCpu.Name = "labelSystemCpu";
            this.labelSystemCpu.Size = new System.Drawing.Size(27, 13);
            this.labelSystemCpu.TabIndex = 1;
            this.labelSystemCpu.Text = "N/A";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(215, 23);
            this.label6.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(26, 13);
            this.label6.TabIndex = 0;
            this.label6.Text = "Cpu";
            // 
            // labelSystemStarted
            // 
            this.labelSystemStarted.AutoSize = true;
            this.labelSystemStarted.Location = new System.Drawing.Point(71, 23);
            this.labelSystemStarted.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelSystemStarted.Name = "labelSystemStarted";
            this.labelSystemStarted.Size = new System.Drawing.Size(27, 13);
            this.labelSystemStarted.TabIndex = 1;
            this.labelSystemStarted.Text = "N/A";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(11, 23);
            this.label4.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(41, 13);
            this.label4.TabIndex = 0;
            this.label4.Text = "Started";
            // 
            // groupBox1
            // 
            this.groupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBox1.Controls.Add(this.labelCamInfoName);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.labelCamInfoIp);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.labelCamInfoSize);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(639, 385);
            this.groupBox1.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Padding = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.groupBox1.Size = new System.Drawing.Size(334, 75);
            this.groupBox1.TabIndex = 13;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Camera information";
            // 
            // labelCamInfoName
            // 
            this.labelCamInfoName.AutoSize = true;
            this.labelCamInfoName.Location = new System.Drawing.Point(70, 26);
            this.labelCamInfoName.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelCamInfoName.Name = "labelCamInfoName";
            this.labelCamInfoName.Size = new System.Drawing.Size(27, 13);
            this.labelCamInfoName.TabIndex = 2;
            this.labelCamInfoName.Text = "N/A";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(9, 26);
            this.label3.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(35, 13);
            this.label3.TabIndex = 0;
            this.label3.Text = "Name";
            // 
            // labelCamInfoIp
            // 
            this.labelCamInfoIp.AutoSize = true;
            this.labelCamInfoIp.Location = new System.Drawing.Point(70, 46);
            this.labelCamInfoIp.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelCamInfoIp.Name = "labelCamInfoIp";
            this.labelCamInfoIp.Size = new System.Drawing.Size(27, 13);
            this.labelCamInfoIp.TabIndex = 2;
            this.labelCamInfoIp.Text = "N/A";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(9, 46);
            this.label2.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(17, 13);
            this.label2.TabIndex = 0;
            this.label2.Text = "IP";
            // 
            // labelCamInfoSize
            // 
            this.labelCamInfoSize.AutoSize = true;
            this.labelCamInfoSize.Location = new System.Drawing.Point(261, 26);
            this.labelCamInfoSize.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelCamInfoSize.Name = "labelCamInfoSize";
            this.labelCamInfoSize.Size = new System.Drawing.Size(27, 13);
            this.labelCamInfoSize.TabIndex = 2;
            this.labelCamInfoSize.Text = "N/A";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(213, 26);
            this.label1.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(27, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Size";
            // 
            // imageToolStripMenuItem
            // 
            this.imageToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.frameRateToolStripMenuItem});
            this.imageToolStripMenuItem.Name = "imageToolStripMenuItem";
            this.imageToolStripMenuItem.Size = new System.Drawing.Size(52, 20);
            this.imageToolStripMenuItem.Text = "Image";
            // 
            // frameRateToolStripMenuItem
            // 
            this.frameRateToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.highestToolStripMenuItem,
            this.halfToolStripMenuItem,
            this.toolStripMenuItem2,
            this.toolStripMenuItem3,
            this.disableToolStripMenuItem});
            this.frameRateToolStripMenuItem.Name = "frameRateToolStripMenuItem";
            this.frameRateToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.frameRateToolStripMenuItem.Text = "Skip frames";
            // 
            // highestToolStripMenuItem
            // 
            this.highestToolStripMenuItem.Name = "highestToolStripMenuItem";
            this.highestToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.highestToolStripMenuItem.Text = "1/1 (full speed)";
            this.highestToolStripMenuItem.Click += new System.EventHandler(this.highestToolStripMenuItem_Click);
            // 
            // halfToolStripMenuItem
            // 
            this.halfToolStripMenuItem.Name = "halfToolStripMenuItem";
            this.halfToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.halfToolStripMenuItem.Text = "1/2";
            this.halfToolStripMenuItem.Click += new System.EventHandler(this.halfToolStripMenuItem_Click);
            // 
            // toolStripMenuItem2
            // 
            this.toolStripMenuItem2.Name = "toolStripMenuItem2";
            this.toolStripMenuItem2.Size = new System.Drawing.Size(180, 22);
            this.toolStripMenuItem2.Text = "1/3";
            this.toolStripMenuItem2.Click += new System.EventHandler(this.toolStripMenuItem2_Click);
            // 
            // toolStripMenuItem3
            // 
            this.toolStripMenuItem3.Name = "toolStripMenuItem3";
            this.toolStripMenuItem3.Size = new System.Drawing.Size(180, 22);
            this.toolStripMenuItem3.Text = "1/4";
            this.toolStripMenuItem3.Click += new System.EventHandler(this.toolStripMenuItem3_Click);
            // 
            // disableToolStripMenuItem
            // 
            this.disableToolStripMenuItem.Name = "disableToolStripMenuItem";
            this.disableToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.disableToolStripMenuItem.Text = "Disable";
            this.disableToolStripMenuItem.Click += new System.EventHandler(this.disableToolStripMenuItem_Click);
            // 
            // cameraControl1
            // 
            this.cameraControl1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.cameraControl1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.cameraControl1.Location = new System.Drawing.Point(638, 235);
            this.cameraControl1.Margin = new System.Windows.Forms.Padding(1);
            this.cameraControl1.Name = "cameraControl1";
            this.cameraControl1.Size = new System.Drawing.Size(336, 114);
            this.cameraControl1.TabIndex = 12;
            // 
            // measurementsToolStripMenuItem
            // 
            this.measurementsToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.addCenterRectangleToolStripMenuItem});
            this.measurementsToolStripMenuItem.Name = "measurementsToolStripMenuItem";
            this.measurementsToolStripMenuItem.Size = new System.Drawing.Size(97, 20);
            this.measurementsToolStripMenuItem.Text = "Measurements";
            // 
            // addCenterRectangleToolStripMenuItem
            // 
            this.addCenterRectangleToolStripMenuItem.Name = "addCenterRectangleToolStripMenuItem";
            this.addCenterRectangleToolStripMenuItem.Size = new System.Drawing.Size(184, 22);
            this.addCenterRectangleToolStripMenuItem.Text = "Add center rectangle";
            this.addCenterRectangleToolStripMenuItem.Click += new System.EventHandler(this.addCenterRectangleToolStripMenuItem_Click);
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(980, 562);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.cameraControl1);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.pictureBoxVisualImage);
            this.Controls.Add(this.listBoxLogger);
            this.Controls.Add(this.pictureBoxThermal);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.menuStrip1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "MainWindow";
            this.Text = "Thermal Camera";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MainWindow_FormClosing);
            this.Load += new System.EventHandler(this.MainWindow_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxThermal)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxVisualImage)).EndInit();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem cameraToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem discoveryToolStripMenuItem;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel1;
        private System.Windows.Forms.ToolStripStatusLabel toolStripConnectionStatus;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel2;
        private System.Windows.Forms.ToolStripStatusLabel toolStripFps;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel4;
        private System.Windows.Forms.ToolStripStatusLabel toolStripFrameCounter;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel6;
        private System.Windows.Forms.ToolStripStatusLabel toolStripLostImages;
        private System.Windows.Forms.PictureBox pictureBoxThermal;
        private System.Windows.Forms.ToolStripMenuItem disconnectToolStripMenuItem;
        private System.Windows.Forms.ListBox listBoxLogger;
        private System.Windows.Forms.PictureBox pictureBoxVisualImage;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Label labelSystemRunning;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label labelSystemStarted;
        private System.Windows.Forms.Label label4;
        private CameraControl cameraControl1;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel3;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabelErrorMessage;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel5;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label labelCamInfoSize;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label labelCamInfoIp;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label labelCamInfoName;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label labelSystemCpu;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label labelSystemMemory;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.ToolStripMenuItem imageToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem frameRateToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem highestToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem halfToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem2;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem3;
        private System.Windows.Forms.ToolStripMenuItem disableToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem measurementsToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem addCenterRectangleToolStripMenuItem;
    }
}

