from tkinter import *

pencere = Tk()
pencere.geometry("700x300")
pencere.title("Yusuf Emir Not Defteri")

def yaz():
    etiket["text"] = "İlk Not Alındı"

buton = Button(pencere, text="Tıkla", command=yaz)
buton.pack()

etiket = Label(pencere)  # Label doğru şekilde oluşturuldu
etiket.pack()

pencere.mainloop()
