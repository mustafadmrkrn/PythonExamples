from tkinter import *

pencere = Tk()
pencere.geometry("200x105")
pencere.title("Bahçeşehir Kolej")
kirmiziFrame = Frame(bg="Red", width=220, height=60)
kirmiziFrame.place(x=200,y=10)
maviFrame = Frame(bg="Blue",width=220,height=60)
maviFrame.place(x=10, y=80)
b1=Button(kirmiziFrame, text="Button1 Kırmızı")
b1.place(x=0,y=0)
b2=Button(maviFrame,text="Button2 Mavi")
b2.place(x=0,y=0)
pencere.mainloop()