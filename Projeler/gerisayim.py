import time
import tkinter as tk
from pygame import mixer

def geri_sayim():
    girilen_sure = int(sure_girdi.get())
    
    while girilen_sure > 0:
        zaman_etiketi.config(text=f"Kalan süre: {girilen_sure} saniye")
        root.update()
        time.sleep(1)
        girilen_sure -= 1

    zaman_etiketi.config(text="Geri sayım bitti!")
    oynat_sesli_uyari()

def oynat_sesli_uyari():
    mixer.init()  # Ses çaları başlat
    mixer.music.load("ses.mp3")  # Kullanmak istediğiniz ses dosyasının yolunu belirtin
    mixer.music.play()

root = tk.Tk()
root.title("Geri Sayım Uygulaması")

sure_girdi = tk.Entry(root)
sure_girdi.pack(pady=10)

basla_dugme = tk.Button(root, text="Geri Sayımı Başlat", command=geri_sayim)
basla_dugme.pack()

zaman_etiketi = tk.Label(root, text="", font=("Helvetica", 20))
zaman_etiketi.pack(pady=40)

root.mainloop()
