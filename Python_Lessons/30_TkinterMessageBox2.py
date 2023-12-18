from tkinter import *
from tkinter import messagebox
pencere = Tk()
pencere.geometry("240x140")
pencere.title("Bahçeşehir")
def uyari():
    cevap = messagebox.askyesnocancel("Uyarı", "Tüm bilgileriniz silinecek!")
    if cevap == True:
        sonuc["text"]="Evet'e Tıkladınız"
    elif cevap == False:
        sonuc["text"] = "Hayır'a Tıkladınız"
    else:
        sonuc["text"] = "İptal'e Tıkladınız."
     
btn = Button(pencere,text="Tıkla",command=uyari)
btn.pack()
sonuc = Label(text="Butona Tıklamadınız")
sonuc.pack()

pencere.mainloop()