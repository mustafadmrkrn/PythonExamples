import tkinter as tk
from tkinter import messagebox

def not_hesapla():
    try:
        skor = float(entry_skor.get())
        if 0 <= skor <= 100:
            if skor >= 80:
                sonuc = "Notunuz: A"
            elif skor >= 60:
                sonuc = "Notunuz: B"
            elif skor >= 50:
                sonuc = "Notunuz: C"
            else:
                sonuc = "Başarısız"
            label_sonuc.config(text=sonuc)
        else:
            messagebox.showerror("Hata", "Lütfen 0 ile 100 arasında bir değer girin.")
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir sayı girin.")

# Ana pencere oluştur
pencere = tk.Tk()
pencere.title("Not Hesaplama")
pencere.geometry("300x200")

# Skor girişi için etiket ve giriş alanı
label_skor = tk.Label(pencere, text="Skorunuzu girin (0-100 arası):")
label_skor.pack(pady=10)

entry_skor = tk.Entry(pencere)
entry_skor.pack(pady=5)

# Hesapla butonu
button_hesapla = tk.Button(pencere, text="Hesapla", command=not_hesapla)
button_hesapla.pack(pady=10)

# Sonuç etiketi
label_sonuc = tk.Label(pencere, text="")
label_sonuc.pack(pady=10)

# Pencereyi çalıştır
pencere.mainloop()
