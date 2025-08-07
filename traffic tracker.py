import time
import psutil
import threading
import tkinter as tk

INTERVAL = 10  # ثانیه

def mb(bytes_val):
    return round(bytes_val / (1024 * 1024), 2)

def get_total_bytes():
    counters = psutil.net_io_counters()
    return counters.bytes_sent + counters.bytes_recv

class TrafficMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Traffic Monitor")

        self.text = tk.Text(root, height=20, width=40)
        self.text.pack()

        self.start_bytes = get_total_bytes()
        self.elapsed = 0

        # اجرای مانیتورینگ در thread جدا
        threading.Thread(target=self.monitor_traffic, daemon=True).start()

    def monitor_traffic(self):
        while True:
            time.sleep(INTERVAL)
            current_bytes = get_total_bytes()
            used_bytes = current_bytes - self.start_bytes
            used_mb = mb(used_bytes)
            self.elapsed += INTERVAL

            msg = f"Time: {self.elapsed}s, Used: {used_mb} MB\n"
            # اضافه کردن متن به Text widget به صورت thread-safe
            self.root.after(0, self.text.insert, tk.END, msg)
            self.root.after(0, self.text.see, tk.END)  # اسکرول خودکار به پایین

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficMonitorApp(root)
    root.mainloop()
