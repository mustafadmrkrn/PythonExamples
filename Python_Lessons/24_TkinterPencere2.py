from tkinter import *

pencere = Tk()
pencere.geometry("500x400")
pencere.title("Bahçeşehir Kolej")

def yaz():
    etiket["text"] = "Bahçeşehir Kodluyor"

buton = Button(pencere, text="Tıkla", command=yaz)
buton.pack()

etiket = Label(pencere)  # Label doğru şekilde oluşturuldu
etiket.pack()

pencere.mainloop()
