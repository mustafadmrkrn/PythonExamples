from tkinter import *
from tkinter import messagebox
pencere = Tk()
pencere.geometry("300x150")  
pencere.title("Ortalama Hesabı")
def hesapla():
    try:
        not1 = int(sinav1Entry.get())
        not2 = int(sinav2Entry.get())
        ortalama = (not1 + not2) / 2
        if ortalama < 45:
            durum = "Başarısız"
        elif ortalama < 55:
            durum = "Geçer"
        elif ortalama < 70:
            durum = "Orta"
        elif ortalama < 85:
            durum = "İyi"
        else:
            durum = "Pekiyi"
        messagebox.showinfo("Sınıf geçme durumu", f"Ortalamanız: {ortalama}\nDurum: {durum}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")
hesapFrame = LabelFrame(pencere, text="Ders Geçme Notu Hesapla", padx=10, pady=10)
hesapFrame.pack(padx=10, pady=10)

sinav1Etiket = Label(hesapFrame, text="1. sınav")
sinav1Etiket.grid(row=0, column=0, padx=5, pady=5)
sinav1Entry = Entry(hesapFrame)
sinav1Entry.grid(row=0, column=1, padx=5, pady=5)

sinav2Etiket = Label(hesapFrame, text="2. sınav")
sinav2Etiket.grid(row=1, column=0, padx=5, pady=5)
sinav2Entry = Entry(hesapFrame)
sinav2Entry.grid(row=1, column=1, padx=5, pady=5)

# Hesapla button
btnHesapla = Button(hesapFrame, text="Hesapla", command=hesapla)
btnHesapla.grid(row=2, columnspan=2, pady=10)

pencere.mainloop()
