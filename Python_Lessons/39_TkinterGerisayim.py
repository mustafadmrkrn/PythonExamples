from tkinter import *

def start_countdown():
    try:
        hours = int(hour_var.get())
        minutes = int(minute_var.get())
        seconds = int(second_var.get())
        total_seconds = hours * 3600 + minutes * 60 + seconds  # Toplam saniye cinsinden süre
        countdown_label.config(text=str(total_seconds))  # Başlangıçta süreyi göster
        for i in range(total_seconds, -1, -1):  # Geri sayım döngüsü
            hours = i // 3600
            minutes = (i % 3600) // 60
            seconds = i % 60
            countdown_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")  # Her saniye sayıyı güncelle
            root.update()  # Tkinter penceresini güncelle
            time.sleep(1)  # 1 saniye beklet
        countdown_label.config(text="Süre Bitti!")  # Geri sayım tamamlandığında mesaj göster
    except ValueError:
        countdown_label.config(text="Geçersiz giriş!")  # Hatalı giriş durumunda hata mesajı göster

root = Tk()
root.title("Geri Sayım Programı")

frame = Frame(root, bg="#f0f0f0", pady=20)
frame.pack()

hour_var = StringVar(root)
minute_var = StringVar(root)
second_var = StringVar(root)

hours = [str(i).zfill(2) for i in range(24)]
minutes = [str(i).zfill(2) for i in range(60)]
seconds = [str(i).zfill(2) for i in range(60)]

hour_label = Label(frame, text="Saat:", font=("Arial", 12))
hour_label.grid(row=0, column=0, padx=5, pady=5)

minute_label = Label(frame, text="Dakika:", font=("Arial", 12))
minute_label.grid(row=0, column=2, padx=5, pady=5)

second_label = Label(frame, text="Saniye:", font=("Arial", 12))
second_label.grid(row=0, column=4, padx=5, pady=5)

hour_menu = OptionMenu(frame, hour_var, *hours)
hour_menu.config(bg="#ddd", fg="#333", font=("Arial", 12))  # Renkler ve yazı tipi
hour_menu.grid(row=0, column=1, padx=5, pady=5)

minute_menu = OptionMenu(frame, minute_var, *minutes)
minute_menu.config(bg="#ddd", fg="#333", font=("Arial", 12))  # Renkler ve yazı tipi
minute_menu.grid(row=0, column=3, padx=5, pady=5)

second_menu = OptionMenu(frame, second_var, *seconds)
second_menu.config(bg="#ddd", fg="#333", font=("Arial", 12))  # Renkler ve yazı tipi
second_menu.grid(row=0, column=5, padx=5, pady=5)

start_button = Button(root, text="Başlat", command=start_countdown)
start_button.config(bg="#4CAF50", fg="#fff", font=("Arial", 12))  # Renkler ve yazı tipi
start_button.pack(pady=10)

countdown_label = Label(root, text="", font=("Arial", 36))
countdown_label.config(bg="#f0f0f0", fg="#333")  # Arka plan ve yazı rengi
countdown_label.pack(pady=20)

root.mainloop()
