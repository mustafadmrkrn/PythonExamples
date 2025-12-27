import tkinter as tk
import time
import threading

# ------------------ AYARLAR ------------------
SURE = 60  # geri sayım (saniye)
# --------------------------------------------

def geri_sayim():
    kalan = SURE
    while kalan >= 0:
        dakika = kalan // 60
        saniye = kalan % 60
        sayac_label.config(text=f"{dakika:02d}:{saniye:02d}")
        time.sleep(1)
        kalan -= 1

    ders_modu()

def ders_modu():
    ekran.config(bg="black")
    for widget in ekran.winfo_children():
        widget.destroy()

    mesaj = tk.Label(
        ekran,
        text="""
🎓 SİBER GÜVENLİK DERSİ

Bu bir FİDYE VİRÜSÜ DEĞİLDİR.
Hiçbir dosyanız zarar görmedi.

Gerçek ransomware:
• Sessiz girer
• Dosyaları gerçekten şifreler
• Panik ve zaman baskısı kurar

DERS:
❌ Korku ile hareket etme
❌ Bilinmeyen dosyayı açma
✅ Yedek al
✅ Güncel sistem kullan
""",
        fg="lime",
        bg="black",
        font=("Arial", 18),
        justify="left"
    )
    mesaj.pack(padx=40, pady=40)

def baslat():
    threading.Thread(target=geri_sayim, daemon=True).start()

# ------------------ GUI ------------------
ekran = tk.Tk()
ekran.title("Dosyalarınız Şifrelendi")
ekran.attributes("-fullscreen", True)
ekran.config(bg="darkred")

baslik = tk.Label(
    ekran,
    text="🔒 DOSYALARINIZ ŞİFRELENDİ!",
    fg="white",
    bg="darkred",
    font=("Arial", 36, "bold")
)
baslik.pack(pady=40)

aciklama = tk.Label(
    ekran,
    text="""
Tüm dosyalarınız askeri düzeyde şifreleme ile kilitlendi.

Geri sayım bitmeden ödeme yapılmazsa:
• Dosyalar silinecek
• Kurtarma mümkün olmayacak
""",
    fg="white",
    bg="darkred",
    font=("Arial", 20),
    justify="left"
)
aciklama.pack(pady=20)

sayac_label = tk.Label(
    ekran,
    text="01:00",
    fg="yellow",
    bg="darkred",
    font=("Arial", 40, "bold")
)
sayac_label.pack(pady=30)

buton = tk.Button(
    ekran,
    text="ÖDEME YAP",
    font=("Arial", 20),
    bg="black",
    fg="red",
    command=ders_modu
)
buton.pack(pady=20)

baslat()
ekran.mainloop()
