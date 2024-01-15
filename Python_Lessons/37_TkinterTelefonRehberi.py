from tkinter import *
from tkinter import messagebox

def kaydet():
    dosya = open("TelefonDefterim.txt", mode="a")
    veri = adEntry.get() + " " + telEntry.get()
    dosya.write(veri + "\n")
    dosya.close()
    messagebox.showinfo("MD", "Kişi ekleme işlemi başarılı.")
    listele()
    adEntry.delete(0, END)
    telEntry.delete(0, END)

def sil():
    try:
        index = metin.curselection()[0]
        metin.delete(index)
        dosya = open("TelefonDefterim.txt", "r")
        lines = dosya.readlines()
        dosya.close()
        dosya = open("TelefonDefterim.txt", "w")
        for i in range(len(lines)):
            if i != index:
                dosya.write(lines[i])
        dosya.close()
    except IndexError:
        messagebox.showwarning("Uyarı", "Lütfen silinecek bir kişi seçin.")

def listele():
    metin.delete(0, END)
    dosya = open("TelefonDefterim.txt", mode="r")
    oku = dosya.readlines()
    for satir in oku:
        metin.insert(END, satir.strip())
    dosya.close()

pencere = Tk()
pencere.geometry("600x200")
pencere.title("MD Cooperation")

dosya = open("TelefonDefterim.txt", mode="a")
dosya.close()

kisiEkleFrame = LabelFrame(pencere, text="Kişi Ekle", width=235, height=125)
kisiEkleFrame.place(x=18, y=18)

adEtiket = Label(kisiEkleFrame, text="Ad Soyad:")
adEtiket.place(x=10, y=10)
adEntry = Entry(kisiEkleFrame)
adEntry.place(x=100, y=10)

telEtiket = Label(kisiEkleFrame, text="Telefon: ")
telEtiket.place(x=10, y=40)
telEntry = Entry(kisiEkleFrame)
telEntry.place(x=100, y=40)

btnKaydet = Button(kisiEkleFrame, text="Kaydet", command=kaydet)
btnKaydet.place(x=170, y=70, width=50)

btnSil = Button(kisiEkleFrame, text="Sil", command=sil)
btnSil.place(x=100, y=70, width=50)

ListeleFrame = LabelFrame(pencere, text="Listele", width=330, height=180)
ListeleFrame.place(x=268, y=18)

metin = Listbox(ListeleFrame, height=9, width=38)
metin.place(x=8, y=4)
listele()

pencere.mainloop()
