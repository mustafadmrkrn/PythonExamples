from tkinter import *
pencere = Tk()
pencere.geometry("240*180")
pencere.title("MD Production")
def yaz():
	etiket["text"] = "MD Production"
buton = Button(text="Tıkla",Command=yaz)
buton.pack()
etiket = Label()
etiket.pack()
pencere.mainloop()