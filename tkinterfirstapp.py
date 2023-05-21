# -*- coding: utf-8 -*-
from tkinter import *

pencere = Tk()
pencere.geometry("240x180")
pencere.title("MD Production")

def yaz():
    etiket["text"] = "MD Production"

buton = Button(text="Tıkla", command=yaz)
buton.pack()

etiket = Label(pencere)
etiket.pack()

pencere.mainloop()
