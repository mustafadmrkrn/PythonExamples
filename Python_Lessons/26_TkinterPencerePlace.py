﻿from tkinter import *

pencere = Tk()
pencere.geometry("200x105")
pencere.title("Bahçeşehir Kolej")
adEtiket = Label(text="Adınız:")
adEtiket.place(x=10, y=10)
adEntry = Entry()
adEntry.place(x=50, y=10)
soyadEtiket = Label(text="Soyadınız")
soyadEtiket.place(x=10, y=40)
soyadEntry = Entry()
soyadEntry.place(x=70, y=40)
giris = Button(text="Giriş Yap")
giris.place(x=135, y=70)
pencere.mainloop()
