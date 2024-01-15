from importlib.metadata import EntryPoint
from tkinter import *
from tkinter import messagebox
pencere = Tk()
pencere.geometry("255x115")
pencere.title("Dosya Oluştur")
def olustur():
    dosyaAdi = adEntry.get()
    open(dosyaAdi+".txt",mode="w")
    messagebox.showinfo("MD cooparation", dosyaAdi+"dosyasını oluşturma işlemi başarılı.")
    
dosyaFrame = LabelFrame(text="Dosya Oluştur", width=235, height=95)
dosyaFrame.place(x=10, y=10)
adEtiket = Label(dosyaFrame, text="Dosya Adı:")
adEtiket.place(x=10, y=10)
adEntry = Entry(dosyaFrame)
adEntry.place(x=100, y=10)
btnOlustur = Button(dosyaFrame, text="Oluştur", command=olustur)
btnOlustur.place(x=170,y=40,width=50)
pencere.mainloop()