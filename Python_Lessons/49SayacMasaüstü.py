import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import calendar
import time
import threading
from PIL import Image, ImageTk  # Pillow kütüphanesi ile görsel desteği

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zamanlayıcı ve Takvim Uygulaması")
        self.root.geometry("600x600")

        # Arka plan görseli
        self.set_background("1.jpg")

        # Güncel Tarih ve Saat
        self.time_label = tk.Label(root, font=("Helvetica", 16), bg="white", fg="black")
        self.time_label.pack(pady=10)
        self.update_time()

        # Takvim
        tk.Label(root, text="Takvim", font=("Helvetica", 14, "bold"), bg="white").pack(pady=5)
        self.calendar_frame = tk.Frame(root, bg="white")
        self.calendar_frame.pack(pady=5)
        self.show_calendar()

        # Geri Sayım
        tk.Label(root, text="Geri Sayım (Saniye):", font=("Helvetica", 12), bg="white").pack()
        self.countdown_entry = tk.Entry(root, font=("Helvetica", 12))
        self.countdown_entry.pack()
        self.countdown_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
        self.countdown_label.pack(pady=5)
        tk.Button(root, text="Geri Sayımı Başlat", command=self.start_countdown).pack()

        # Kronometre
        self.stopwatch_running = False
        self.stopwatch_seconds = 0
        self.stopwatch_label = tk.Label(root, text="Kronometre: 00:00", font=("Helvetica", 14), bg="white")
        self.stopwatch_label.pack(pady=10)
        tk.Button(root, text="Kronometreyi Başlat", command=self.start_stopwatch).pack()
        tk.Button(root, text="Kronometreyi Durdur", command=self.stop_stopwatch).pack()

    def set_background(self, image_path):
        """Arka plan görselini ayarla."""
        try:
            image = Image.open(image_path)
            image = image.resize((600, 600), Image.ANTIALIAS)
            bg_image = ImageTk.PhotoImage(image)
            bg_label = tk.Label(self.root, image=bg_image)
            bg_label.image = bg_image
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            messagebox.showerror("Hata", "Arka plan görseli bulunamadı.")

    def update_time(self):
        """Güncel tarih ve saat göstergesi."""
        now = datetime.now()
        self.time_label.config(text=now.strftime("%Y-%m-%d %H:%M:%S"))
        self.root.after(1000, self.update_time)

    def show_calendar(self):
        """Bir aylık takvimi göster."""
        now = datetime.now()
        year = now.year
        month = now.month
        cal = calendar.TextCalendar()
        month_calendar = cal.formatmonth(year, month)
        cal_label = tk.Label(self.calendar_frame, text=month_calendar, font=("Courier", 12), bg="white", justify="left")
        cal_label.pack()

    def start_countdown(self):
        """Geri sayım başlatma."""
        try:
            seconds = int(self.countdown_entry.get())
            threading.Thread(target=self.run_countdown, args=(seconds,)).start()
        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

    def run_countdown(self, seconds):
        """Geri sayım işlemi."""
        while seconds >= 0:
            mins, secs = divmod(seconds, 60)
            self.countdown_label.config(text=f"{mins:02}:{secs:02}")
            time.sleep(1)
            seconds -= 1
        self.countdown_label.config(text="Zaman Doldu!")

    def start_stopwatch(self):
        """Kronometre başlatma."""
        if not self.stopwatch_running:
            self.stopwatch_running = True
            threading.Thread(target=self.run_stopwatch).start()

    def run_stopwatch(self):
        """Kronometre işlemi."""
        while self.stopwatch_running:
            mins, secs = divmod(self.stopwatch_seconds, 60)
            self.stopwatch_label.config(text=f"Kronometre: {mins:02}:{secs:02}")
            time.sleep(1)
            self.stopwatch_seconds += 1

    def stop_stopwatch(self):
        """Kronometre durdurma."""
        self.stopwatch_running = False


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
