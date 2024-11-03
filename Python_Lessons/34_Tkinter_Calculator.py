from tkinter import *

def topla():
    try:
        sayi1 = int(sayi1Entry.get())
        sayi2 = int(sayi2Entry.get())
        sonuc = sayi1 + sayi2
        sonucEtiket["text"] = "Sonuç: Toplam:" + str(sonuc)
    except ValueError:
        sonucEtiket["text"] = "Geçersiz giriş!"

def fark():
    try:
        sayi1 = int(sayi1Entry.get())
        sayi2 = int(sayi2Entry.get())
        sonuc = sayi1 - sayi2
        sonucEtiket["text"] = "Sonuç: Fark:" + str(sonuc)
    except ValueError:
        sonucEtiket["text"] = "Geçersiz giriş!"
def carp():
    try:
        sayi1 = int(sayi1Entry.get())
        sayi2 = int(sayi2Entry.get())
        sonuc = sayi1 * sayi2
        sonucEtiket["text"] = "Sonuç: Çarpım:" + str(sonuc)
    except ValueError:
        sonucEtiket["text"] = "Geçersiz giriş!"

def bol():
    try:
        sayi1 = int(sayi1Entry.get())
        sayi2 = int(sayi2Entry.get())
        if sayi2 == 0:
            sonucEtiket["text"] = "Sıfıra bölme hatası!"
        else:
            sonuc = sayi1 / sayi2
            sonucEtiket["text"] = "Sonuç: Bölüm:" + str(sonuc)
    except ValueError:
        sonucEtiket["text"] = "Geçersiz giriş!"

pencere = Tk()
pencere.geometry("255x185")
pencere.title("Hesap Makinası")

hesapFrame = LabelFrame(pencere, text="Hesap Makinası", width=235, height=165)
hesapFrame.place(x=10, y=10)

sayi1Etiket = Label(hesapFrame, text="1. Sayı")
sayi1Etiket.place(x=10, y=10)
sayi1Entry = Entry(hesapFrame)
sayi1Entry.place(x=100, y=10)

sayi2Etiket = Label(hesapFrame, text="2. Sayı")
sayi2Etiket.place(x=10, y=40)
sayi2Entry = Entry(hesapFrame)
sayi2Entry.place(x=100, y=40)

sonucEtiket = Label(hesapFrame, text="Sonuç")
sonucEtiket.place(x=10, y=70)

btnTopla = Button(hesapFrame, text="+", command=topla)
btnTopla.place(x=5, y=100, width=50)
btnFark = Button(hesapFrame, text="-", command=fark)
btnFark.place(x=60, y=100, width=50)
btnCarp = Button(hesapFrame, text="*", command=carp)
btnCarp.place(x=115, y=100, width=50)
btnBol = Button(hesapFrame, text="/", command=bol)
btnBol.place(x=170, y=100, width=50)

pencere.mainloop()
