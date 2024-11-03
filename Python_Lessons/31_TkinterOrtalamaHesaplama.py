from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.geometry("400x300")
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

hesapFrame = LabelFrame(pencere, text="Ders Geçme Notu Hesapla", width=220, height=120)
hesapFrame.place(x=10, y=10)

sinav1Etiket = Label(hesapFrame, text="1. sınav")
sinav1Etiket.place(x=10, y=10)
sinav1Entry = Entry(hesapFrame)
sinav1Entry.place(x=70, y=10)

sinav2Etiket = Label(hesapFrame, text="2. sınav")
sinav2Etiket.place(x=10, y=40)
sinav2Entry = Entry(hesapFrame)
sinav2Entry.place(x=70, y=40)

btnHesapla = Button(hesapFrame, text="Hesapla", command=hesapla)
btnHesapla.place(x=155, y=70)

pencere.mainloop()
