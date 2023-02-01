namespace Thermal_Camera
{
    partial class CameraControl
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

        #region Component Designer generated code

        /// <summary> 
        /// Required method for Designer support - do not modify 
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.buttonFocusNear = new System.Windows.Forms.Button();
            this.buttonFocusFar = new System.Windows.Forms.Button();
            this.buttonNuc = new System.Windows.Forms.Button();
            this.buttonFocusAuto = new System.Windows.Forms.Button();
            this.groupBoxFocus = new System.Windows.Forms.GroupBox();
            this.groupBoxFocus.SuspendLayout();
            this.SuspendLayout();
            // 
            // buttonFocusNear
            // 
            this.buttonFocusNear.Location = new System.Drawing.Point(16, 54);
            this.buttonFocusNear.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.buttonFocusNear.Name = "buttonFocusNear";
            this.buttonFocusNear.Size = new System.Drawing.Size(112, 35);
            this.buttonFocusNear.TabIndex = 0;
            this.buttonFocusNear.Text = "Near";
            this.buttonFocusNear.UseVisualStyleBackColor = true;
            this.buttonFocusNear.MouseDown += new System.Windows.Forms.MouseEventHandler(this.buttonFocusNear_MouseDown);
            this.buttonFocusNear.MouseUp += new System.Windows.Forms.MouseEventHandler(this.buttonFocusNear_MouseUp);
            // 
            // buttonFocusFar
            // 
            this.buttonFocusFar.Location = new System.Drawing.Point(260, 54);
            this.buttonFocusFar.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.buttonFocusFar.Name = "buttonFocusFar";
            this.buttonFocusFar.Size = new System.Drawing.Size(112, 35);
            this.buttonFocusFar.TabIndex = 0;
            this.buttonFocusFar.Text = "Far";
            this.buttonFocusFar.UseVisualStyleBackColor = true;
            this.buttonFocusFar.MouseDown += new System.Windows.Forms.MouseEventHandler(this.buttonFocusFar_MouseDown);
            this.buttonFocusFar.MouseUp += new System.Windows.Forms.MouseEventHandler(this.buttonFocusFar_MouseUp);
            // 
            // buttonNuc
            // 
            this.buttonNuc.Location = new System.Drawing.Point(21, 17);
            this.buttonNuc.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.buttonNuc.Name = "buttonNuc";
            this.buttonNuc.Size = new System.Drawing.Size(112, 35);
            this.buttonNuc.TabIndex = 37;
            this.buttonNuc.Text = "NUC";
            this.buttonNuc.UseVisualStyleBackColor = true;
            this.buttonNuc.Click += new System.EventHandler(this.buttonNuc_Click_1);
            // 
            // buttonFocusAuto
            // 
            this.buttonFocusAuto.Location = new System.Drawing.Point(138, 54);
            this.buttonFocusAuto.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.buttonFocusAuto.Name = "buttonFocusAuto";
            this.buttonFocusAuto.Size = new System.Drawing.Size(112, 35);
            this.buttonFocusAuto.TabIndex = 0;
            this.buttonFocusAuto.Text = "Auto";
            this.buttonFocusAuto.UseVisualStyleBackColor = true;
            this.buttonFocusAuto.Click += new System.EventHandler(this.buttonFocusAuto_Click);
            // 
            // groupBoxFocus
            // 
            this.groupBoxFocus.Controls.Add(this.buttonFocusFar);
            this.groupBoxFocus.Controls.Add(this.buttonFocusAuto);
            this.groupBoxFocus.Controls.Add(this.buttonFocusNear);
            this.groupBoxFocus.Enabled = false;
            this.groupBoxFocus.Location = new System.Drawing.Point(21, 62);
            this.groupBoxFocus.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.groupBoxFocus.Name = "groupBoxFocus";
            this.groupBoxFocus.Padding = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.groupBoxFocus.Size = new System.Drawing.Size(408, 104);
            this.groupBoxFocus.TabIndex = 36;
            this.groupBoxFocus.TabStop = false;
            this.groupBoxFocus.Text = "Focus";
            // 
            // CameraControl
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.Controls.Add(this.buttonNuc);
            this.Controls.Add(this.groupBoxFocus);
            this.Name = "CameraControl";
            this.Size = new System.Drawing.Size(451, 181);
            this.Load += new System.EventHandler(this.CameraControl_Load);
            this.groupBoxFocus.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button buttonFocusNear;
        private System.Windows.Forms.Button buttonFocusFar;
        private System.Windows.Forms.Button buttonNuc;
        private System.Windows.Forms.Button buttonFocusAuto;
        private System.Windows.Forms.GroupBox groupBoxFocus;
    }
}
