from tkinter import *

pencere = Tk()
pencere.geometry("240x180")
pencere.title("Bahçeşehir Kolej")

def yaz():
    metin["text"] = "Merhaba " + ad.get()

adEtiket = Label(text="Lütfen Adınızı Giriniz:")
adEtiket.pack()
ad = Entry()
ad.pack()

buton = Button(pencere, text="Tıkla", command=yaz)
buton.pack()

metin = Label()
metin.pack()

pencere.mainloop()
