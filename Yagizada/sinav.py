import tkinter as tk
from tkinter import messagebox

def hesapla():
    try:
        sinav1 = float(giris_sinav1.get())
        sinav2 = float(giris_sinav2.get())
        
        ortalama = (sinav1 + sinav2) / 2
        
        if ortalama >= 50:
            durum = "Başarılı! 🎉"
        else:
            durum = "Biraz daha çalışmalısın. 💪"
            
        sonuc_etiketi.config(text=f"Ortalama: {ortalama:.2f}\nDurum: {durum}")
        
    except ValueError:
        messagebox.showerror("Hata", "Lütfen sadece sayı girin!")

pencere = tk.Tk()
pencere.title("Puan Hesaplayıcı")
pencere.geometry("300x250")

# MAC FIX: Yazı renklerini (fg) siyah, arka planı (bg) beyaz olarak sabitliyoruz.
# insertbackground="black" ise yazı yazarken yanıp sönen imlecin (cursor) rengidir.

tk.Label(pencere, text="1. Sınav Puanı:", fg="black").pack(pady=5)
giris_sinav1 = tk.Entry(pencere, fg="black", bg="white", insertbackground="black")
giris_sinav1.pack(pady=5)

tk.Label(pencere, text="2. Sınav Puanı:", fg="black").pack(pady=5)
giris_sinav2 = tk.Entry(pencere, fg="black", bg="white", insertbackground="black")
giris_sinav2.pack(pady=5)

hesapla_butonu = tk.Button(pencere, text="Hesapla", command=hesapla)
hesapla_butonu.pack(pady=10)

sonuc_etiketi = tk.Label(pencere, text="", font=("Arial", 12, "bold"), fg="black")
sonuc_etiketi.pack(pady=10)

pencere.mainloop()