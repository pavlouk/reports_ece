namespace GigeVisionSample
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
            this.connectToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.disconnectToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.comboBoxTempRanges = new System.Windows.Forms.ComboBox();
            this.label5 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.comboBoxNucMode = new System.Windows.Forms.ComboBox();
            this.groupBoxCameraControl = new System.Windows.Forms.GroupBox();
            this.buttonNuc = new System.Windows.Forms.Button();
            this.buttonFocusFar = new System.Windows.Forms.Button();
            this.buttonFocusAuto = new System.Windows.Forms.Button();
            this.buttonFocusNear = new System.Windows.Forms.Button();
            this.groupBoxFocusControls = new System.Windows.Forms.GroupBox();
            this.buttonFocusSpeed = new System.Windows.Forms.Button();
            this.textBoxFocusSpeed = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.buttonFocusDist = new System.Windows.Forms.Button();
            this.textBoxFocusDist = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.buttonFocusSet = new System.Windows.Forms.Button();
            this.textBoxFocusPos = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.toolStripStatusLabel1 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripConnectionStatus = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabel2 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripFps = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabel4 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripFrameCounter = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabel7 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabelSystemRunning = new System.Windows.Forms.ToolStripStatusLabel();
            this.pictureBoxThermal = new System.Windows.Forms.PictureBox();
            this.menuStrip1.SuspendLayout();
            this.groupBoxCameraControl.SuspendLayout();
            this.groupBoxFocusControls.SuspendLayout();
            this.statusStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxThermal)).BeginInit();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.cameraToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(908, 24);
            this.menuStrip1.TabIndex = 10;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // cameraToolStripMenuItem
            // 
            this.cameraToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.connectToolStripMenuItem,
            this.disconnectToolStripMenuItem});
            this.cameraToolStripMenuItem.Name = "cameraToolStripMenuItem";
            this.cameraToolStripMenuItem.Size = new System.Drawing.Size(60, 20);
            this.cameraToolStripMenuItem.Text = "Camera";
            // 
            // connectToolStripMenuItem
            // 
            this.connectToolStripMenuItem.Name = "connectToolStripMenuItem";
            this.connectToolStripMenuItem.Size = new System.Drawing.Size(133, 22);
            this.connectToolStripMenuItem.Text = "Connect...";
            this.connectToolStripMenuItem.Click += new System.EventHandler(this.connectToolStripMenuItem_Click);
            // 
            // disconnectToolStripMenuItem
            // 
            this.disconnectToolStripMenuItem.Name = "disconnectToolStripMenuItem";
            this.disconnectToolStripMenuItem.Size = new System.Drawing.Size(133, 22);
            this.disconnectToolStripMenuItem.Text = "Disconnect";
            this.disconnectToolStripMenuItem.Click += new System.EventHandler(this.disconnectToolStripMenuItem_Click);
            // 
            // comboBoxTempRanges
            // 
            this.comboBoxTempRanges.FormattingEnabled = true;
            this.comboBoxTempRanges.Location = new System.Drawing.Point(9, 94);
            this.comboBoxTempRanges.Margin = new System.Windows.Forms.Padding(2);
            this.comboBoxTempRanges.Name = "comboBoxTempRanges";
            this.comboBoxTempRanges.Size = new System.Drawing.Size(195, 21);
            this.comboBoxTempRanges.TabIndex = 8;
            this.comboBoxTempRanges.SelectedIndexChanged += new System.EventHandler(this.comboBoxTempRanges_SelectedIndexChanged);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(7, 79);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(102, 13);
            this.label5.TabIndex = 7;
            this.label5.Text = "Temperature ranges";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(6, 26);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(65, 13);
            this.label3.TabIndex = 6;
            this.label3.Text = "NUC Modes";
            // 
            // comboBoxNucMode
            // 
            this.comboBoxNucMode.FormattingEnabled = true;
            this.comboBoxNucMode.Items.AddRange(new object[] {
            "Off",
            "Automatic"});
            this.comboBoxNucMode.Location = new System.Drawing.Point(9, 42);
            this.comboBoxNucMode.Name = "comboBoxNucMode";
            this.comboBoxNucMode.Size = new System.Drawing.Size(121, 21);
            this.comboBoxNucMode.TabIndex = 0;
            this.comboBoxNucMode.SelectedIndexChanged += new System.EventHandler(this.comboBoxNucMode_SelectedIndexChanged);
            // 
            // groupBoxCameraControl
            // 
            this.groupBoxCameraControl.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBoxCameraControl.Controls.Add(this.comboBoxTempRanges);
            this.groupBoxCameraControl.Controls.Add(this.label5);
            this.groupBoxCameraControl.Controls.Add(this.label3);
            this.groupBoxCameraControl.Controls.Add(this.buttonNuc);
            this.groupBoxCameraControl.Controls.Add(this.comboBoxNucMode);
            this.groupBoxCameraControl.Location = new System.Drawing.Point(675, 159);
            this.groupBoxCameraControl.Name = "groupBoxCameraControl";
            this.groupBoxCameraControl.Size = new System.Drawing.Size(221, 146);
            this.groupBoxCameraControl.TabIndex = 21;
            this.groupBoxCameraControl.TabStop = false;
            this.groupBoxCameraControl.Text = "Camera Control";
            // 
            // buttonNuc
            // 
            this.buttonNuc.Location = new System.Drawing.Point(164, 42);
            this.buttonNuc.Name = "buttonNuc";
            this.buttonNuc.Size = new System.Drawing.Size(39, 21);
            this.buttonNuc.TabIndex = 1;
            this.buttonNuc.Text = "NUC";
            this.buttonNuc.UseVisualStyleBackColor = true;
            this.buttonNuc.Click += new System.EventHandler(this.buttonNuc_Click);
            // 
            // buttonFocusFar
            // 
            this.buttonFocusFar.Location = new System.Drawing.Point(141, 97);
            this.buttonFocusFar.Name = "buttonFocusFar";
            this.buttonFocusFar.Size = new System.Drawing.Size(43, 23);
            this.buttonFocusFar.TabIndex = 11;
            this.buttonFocusFar.Text = "Far";
            this.buttonFocusFar.UseVisualStyleBackColor = true;
            this.buttonFocusFar.MouseDown += new System.Windows.Forms.MouseEventHandler(this.buttonFocusFar_MouseDown);
            this.buttonFocusFar.MouseUp += new System.Windows.Forms.MouseEventHandler(this.buttonFocusFar_MouseUp);
            // 
            // buttonFocusAuto
            // 
            this.buttonFocusAuto.Location = new System.Drawing.Point(92, 97);
            this.buttonFocusAuto.Name = "buttonFocusAuto";
            this.buttonFocusAuto.Size = new System.Drawing.Size(43, 23);
            this.buttonFocusAuto.TabIndex = 10;
            this.buttonFocusAuto.Text = "Auto";
            this.buttonFocusAuto.UseVisualStyleBackColor = true;
            this.buttonFocusAuto.Click += new System.EventHandler(this.buttonFocusAuto_Click);
            // 
            // buttonFocusNear
            // 
            this.buttonFocusNear.Location = new System.Drawing.Point(43, 97);
            this.buttonFocusNear.Name = "buttonFocusNear";
            this.buttonFocusNear.Size = new System.Drawing.Size(43, 23);
            this.buttonFocusNear.TabIndex = 9;
            this.buttonFocusNear.Text = "Near";
            this.buttonFocusNear.UseVisualStyleBackColor = true;
            this.buttonFocusNear.MouseDown += new System.Windows.Forms.MouseEventHandler(this.buttonFocusNear_MouseDown);
            this.buttonFocusNear.MouseUp += new System.Windows.Forms.MouseEventHandler(this.buttonFocusNear_MouseUp);
            // 
            // groupBoxFocusControls
            // 
            this.groupBoxFocusControls.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBoxFocusControls.Controls.Add(this.buttonFocusFar);
            this.groupBoxFocusControls.Controls.Add(this.buttonFocusAuto);
            this.groupBoxFocusControls.Controls.Add(this.buttonFocusNear);
            this.groupBoxFocusControls.Controls.Add(this.buttonFocusSpeed);
            this.groupBoxFocusControls.Controls.Add(this.textBoxFocusSpeed);
            this.groupBoxFocusControls.Controls.Add(this.label4);
            this.groupBoxFocusControls.Controls.Add(this.buttonFocusDist);
            this.groupBoxFocusControls.Controls.Add(this.textBoxFocusDist);
            this.groupBoxFocusControls.Controls.Add(this.label2);
            this.groupBoxFocusControls.Controls.Add(this.buttonFocusSet);
            this.groupBoxFocusControls.Controls.Add(this.textBoxFocusPos);
            this.groupBoxFocusControls.Controls.Add(this.label1);
            this.groupBoxFocusControls.Location = new System.Drawing.Point(675, 27);
            this.groupBoxFocusControls.Name = "groupBoxFocusControls";
            this.groupBoxFocusControls.Size = new System.Drawing.Size(221, 126);
            this.groupBoxFocusControls.TabIndex = 20;
            this.groupBoxFocusControls.TabStop = false;
            this.groupBoxFocusControls.Text = "Focus Control";
            // 
            // buttonFocusSpeed
            // 
            this.buttonFocusSpeed.Location = new System.Drawing.Point(164, 72);
            this.buttonFocusSpeed.Name = "buttonFocusSpeed";
            this.buttonFocusSpeed.Size = new System.Drawing.Size(39, 20);
            this.buttonFocusSpeed.TabIndex = 8;
            this.buttonFocusSpeed.Text = "Set";
            this.buttonFocusSpeed.UseVisualStyleBackColor = true;
            this.buttonFocusSpeed.Click += new System.EventHandler(this.buttonFocusSpeed_Click);
            // 
            // textBoxFocusSpeed
            // 
            this.textBoxFocusSpeed.Location = new System.Drawing.Point(97, 72);
            this.textBoxFocusSpeed.Name = "textBoxFocusSpeed";
            this.textBoxFocusSpeed.Size = new System.Drawing.Size(61, 20);
            this.textBoxFocusSpeed.TabIndex = 7;
            this.textBoxFocusSpeed.Text = "0";
            this.textBoxFocusSpeed.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(6, 76);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(38, 13);
            this.label4.TabIndex = 6;
            this.label4.Text = "Speed";
            // 
            // buttonFocusDist
            // 
            this.buttonFocusDist.Location = new System.Drawing.Point(164, 46);
            this.buttonFocusDist.Name = "buttonFocusDist";
            this.buttonFocusDist.Size = new System.Drawing.Size(39, 20);
            this.buttonFocusDist.TabIndex = 5;
            this.buttonFocusDist.Text = "Set";
            this.buttonFocusDist.UseVisualStyleBackColor = true;
            this.buttonFocusDist.Click += new System.EventHandler(this.buttonFocusDist_Click);
            // 
            // textBoxFocusDist
            // 
            this.textBoxFocusDist.Location = new System.Drawing.Point(97, 46);
            this.textBoxFocusDist.Name = "textBoxFocusDist";
            this.textBoxFocusDist.Size = new System.Drawing.Size(61, 20);
            this.textBoxFocusDist.TabIndex = 4;
            this.textBoxFocusDist.Text = "0";
            this.textBoxFocusDist.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(6, 50);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(49, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "Distance";
            // 
            // buttonFocusSet
            // 
            this.buttonFocusSet.Location = new System.Drawing.Point(164, 20);
            this.buttonFocusSet.Name = "buttonFocusSet";
            this.buttonFocusSet.Size = new System.Drawing.Size(39, 20);
            this.buttonFocusSet.TabIndex = 2;
            this.buttonFocusSet.Text = "Set";
            this.buttonFocusSet.UseVisualStyleBackColor = true;
            this.buttonFocusSet.Click += new System.EventHandler(this.buttonFocusSet_Click);
            // 
            // textBoxFocusPos
            // 
            this.textBoxFocusPos.Location = new System.Drawing.Point(97, 20);
            this.textBoxFocusPos.Name = "textBoxFocusPos";
            this.textBoxFocusPos.Size = new System.Drawing.Size(61, 20);
            this.textBoxFocusPos.TabIndex = 1;
            this.textBoxFocusPos.Text = "0";
            this.textBoxFocusPos.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 24);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(44, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Position";
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
            this.toolStripStatusLabel7,
            this.toolStripStatusLabelSystemRunning});
            this.statusStrip1.Location = new System.Drawing.Point(0, 459);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(908, 24);
            this.statusStrip1.TabIndex = 19;
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
            this.toolStripStatusLabel4.Size = new System.Drawing.Size(45, 19);
            this.toolStripStatusLabel4.Text = "Frames";
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
            // toolStripStatusLabel7
            // 
            this.toolStripStatusLabel7.Name = "toolStripStatusLabel7";
            this.toolStripStatusLabel7.Size = new System.Drawing.Size(74, 19);
            this.toolStripStatusLabel7.Text = "Elapsed time";
            // 
            // toolStripStatusLabelSystemRunning
            // 
            this.toolStripStatusLabelSystemRunning.Name = "toolStripStatusLabelSystemRunning";
            this.toolStripStatusLabelSystemRunning.Size = new System.Drawing.Size(13, 19);
            this.toolStripStatusLabelSystemRunning.Text = "0";
            // 
            // pictureBoxThermal
            // 
            this.pictureBoxThermal.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBoxThermal.BackColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.pictureBoxThermal.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBoxThermal.Location = new System.Drawing.Point(12, 38);
            this.pictureBoxThermal.Name = "pictureBoxThermal";
            this.pictureBoxThermal.Size = new System.Drawing.Size(657, 400);
            this.pictureBoxThermal.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBoxThermal.TabIndex = 18;
            this.pictureBoxThermal.TabStop = false;
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(908, 483);
            this.Controls.Add(this.groupBoxCameraControl);
            this.Controls.Add(this.groupBoxFocusControls);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.pictureBoxThermal);
            this.Controls.Add(this.menuStrip1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "MainWindow";
            this.Text = "GigeVision Camera";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.MainWindow_FormClosing);
            this.Load += new System.EventHandler(this.MainWindow_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.groupBoxCameraControl.ResumeLayout(false);
            this.groupBoxCameraControl.PerformLayout();
            this.groupBoxFocusControls.ResumeLayout(false);
            this.groupBoxFocusControls.PerformLayout();
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxThermal)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem cameraToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem connectToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem disconnectToolStripMenuItem;
        private System.Windows.Forms.ComboBox comboBoxTempRanges;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.ComboBox comboBoxNucMode;
        private System.Windows.Forms.GroupBox groupBoxCameraControl;
        private System.Windows.Forms.Button buttonNuc;
        private System.Windows.Forms.Button buttonFocusFar;
        private System.Windows.Forms.Button buttonFocusAuto;
        private System.Windows.Forms.Button buttonFocusNear;
        private System.Windows.Forms.GroupBox groupBoxFocusControls;
        private System.Windows.Forms.Button buttonFocusSpeed;
        private System.Windows.Forms.TextBox textBoxFocusSpeed;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button buttonFocusDist;
        private System.Windows.Forms.TextBox textBoxFocusDist;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button buttonFocusSet;
        private System.Windows.Forms.TextBox textBoxFocusPos;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel1;
        private System.Windows.Forms.ToolStripStatusLabel toolStripConnectionStatus;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel2;
        private System.Windows.Forms.ToolStripStatusLabel toolStripFps;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel4;
        private System.Windows.Forms.ToolStripStatusLabel toolStripFrameCounter;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel7;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabelSystemRunning;
        private System.Windows.Forms.PictureBox pictureBoxThermal;
    }
}

