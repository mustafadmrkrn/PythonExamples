﻿from tkinter import *
pencere =Tk()
pencere.geometry("240x140")
pencere.title("Bahçeşehir Koleji")
yeniUye = LabelFrame(text="Yeni Üye Formu",width=220,height=120)
yeniUye.place(x=10,y=10)
adEtiket = Label(yeniUye,text="Adınız: ")
adEtiket.place(x=10,y=10)
adEntry=Entry(yeniUye)
adEntry.place(x=70,y=10)
soyadEtiket = Label(yeniUye,text="Soyadınız: ")
soyadEtiket.place(x=10,y=40)
soyadEntry=Entry(yeniUye)
soyadEntry.place(x=70,y=40)
btnKaydet = Button(yeniUye, text="Kaydet ")
btnKaydet.place(x=165,y=70)
pencere.mainloop()