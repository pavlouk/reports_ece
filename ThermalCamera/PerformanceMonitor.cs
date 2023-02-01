using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Thermal_Camera
{
    class PerformanceMonitor
    {
        private const double KiloByte = 1024;
        private const double MegaByte = 1024 * 1024;

        PerformanceCounter perfCounter;
        Process processToMonitor;

        Timer _timer = new Timer();

        public event EventHandler<EventArgs> Updated;

        public void Start(Process process)
        {
            processToMonitor = process;
            if (processToMonitor == null)
            {
                throw new ArgumentNullException(nameof(process));
            }

            perfCounter = new PerformanceCounter
            {
                CategoryName = "Process",
                CounterName = "% Processor Time",
                InstanceName = processToMonitor.ProcessName,
                ReadOnly = true
            };

            _timer.Interval = 1000;
            _timer.Tick += _timer_Tick;
            _timer.Start();
        }

        public void Stop()
        {
            _timer.Stop();
        }

        void _timer_Tick(object sender, EventArgs e)
        {
            processToMonitor.Refresh();

            if (perfCounter != null)
            {
                try
                {
                    var processCpu = Convert.ToInt32(perfCounter.NextValue());
                    Cpu = Convert.ToString(processCpu / Environment.ProcessorCount);
                }
                catch (Exception)
                {
                    Cpu = "N/A";
                    perfCounter = null;
                }
            }
            UserProcessorTime = string.Format("{0}", processToMonitor.UserProcessorTime);
            PrivilegedProcessorTime = string.Format("{0}", processToMonitor.PrivilegedProcessorTime);
            TotalProcessorTime = string.Format("{0}", processToMonitor.TotalProcessorTime);
            WorkingSet64 = string.Format("{0} KB", processToMonitor.WorkingSet64 / KiloByte);
            PagedSystemMemorySize64 = string.Format("{0} KB", processToMonitor.PagedSystemMemorySize64 / KiloByte);
            PagedMemorySize64 = string.Format("{0} KB", processToMonitor.PagedMemorySize64 / KiloByte);
            PeakWorkingSet64 = string.Format("{0} KB", processToMonitor.PeakWorkingSet64 / KiloByte);
            PeakPagedMemorySize64 = string.Format("{0} KB", processToMonitor.PeakPagedMemorySize64 / KiloByte);
            PeakVirtualMemorySize64 = string.Format("{0} KB", processToMonitor.PeakVirtualMemorySize64 / KiloByte);

            Updated?.Invoke(this, new EventArgs());
        }

        public string Cpu { get; private set; }

        public string UserProcessorTime { get; private set; }

        public string PrivilegedProcessorTime { get; private set; }
        public string TotalProcessorTime { get; private set; }
        public string WorkingSet64 { get; private set; }
        public string PagedSystemMemorySize64 { get; private set; }
        public string PagedMemorySize64 { get; private set; }
        public string PeakWorkingSet64 { get; private set; }
        public string PeakPagedMemorySize64 { get; private set; }
        public string PeakVirtualMemorySize64 { get; private set; }

    }
}
