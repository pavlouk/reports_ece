using System;
using System.Collections.Generic;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace IRImageReaderDemo
{
    //Code from http://www.codeproject.com/KB/graphics/a_mini_media_player.aspx
    public class MediaPlayer
    {
        public const int MM_MCINOTIFY = 0x3B9;

        private string fileName;
        private bool isOpen = false;
        private Form notifyForm;
        private string mediaName = "media";
        private bool _isPaused = false;
        private bool _isPlaying = false;

        public bool IsPlaying
        {
            get
            {
                return _isPlaying;
            }
        }

        //mciSendString 
        [DllImport("winmm.dll")]
        private static extern long mciSendString(
            string command,
            StringBuilder returnValue,
            int returnLength,
            IntPtr winHandle);

        private void ClosePlayer()
        {
            if (isOpen)
            {
                String playCommand = "Close " + mediaName;
                mciSendString(playCommand, null, 0, IntPtr.Zero);
                isOpen = false;
            }
        }

        private void OpenMediaFile()
        {
            ClosePlayer();
            string playCommand = "Open \"" + fileName + "\" type mpegvideo alias " + mediaName;
            mciSendString(playCommand, null, 0, IntPtr.Zero);
            isOpen = true;
        }


        private void PlayMediaFile()
        {
            if (isOpen)
            {
                string playCommand = "Play " + mediaName + " notify";
                mciSendString(playCommand, null, 0, notifyForm.Handle);
                _isPlaying = true;
            }
        }


        public void Play(string fileName, Form notifyForm)
        {
            if (!_isPaused)
            {
                this.fileName = fileName;
                this.notifyForm = notifyForm;
                OpenMediaFile();
                PlayMediaFile();
            }
            else
            {
                _isPaused = false;
                PlayMediaFile();
            }
        }

        public void Stop()
        {
            //ClosePlayer();
            if (isOpen)
            {
                string stopCommand = "Stop " + mediaName;
                mciSendString(stopCommand, null, 0, IntPtr.Zero);
                _isPaused = false;
                _isPlaying = false;
            }
        }

        public void Pause()
        {
            if (isOpen)
            {
                string pauseCommand = "Pause " + mediaName;
                mciSendString(pauseCommand, null, 0, IntPtr.Zero);
                _isPaused = true;
                _isPlaying = false;
            }
        }
    }
}
