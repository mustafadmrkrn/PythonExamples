from tkinter import *

pencere = Tk()
# macOS başlık çubuğu sığsın diye genişliği biraz artırdık
pencere.geometry("300x150") 
pencere.title("Bahçeşehir Kolej")

# Tüm widget'lara 'pencere' parametresi eklendi
adEtiket = Label(pencere, text="Adınız:")
adEtiket.place(x=10, y=10)

adEntry = Entry(pencere)
# Etiketle üst üste binmemesi için X konumu 50'den 90'a çekildi
adEntry.place(x=90, y=10) 

soyadEtiket = Label(pencere, text="Soyadınız:")
soyadEtiket.place(x=10, y=40)

soyadEntry = Entry(pencere)
# Etiketle üst üste binmemesi için X konumu 70'ten 90'a çekildi
soyadEntry.place(x=90, y=40)

giris = Button(pencere, text="Giriş Yap")
giris.place(x=135, y=80)

pencere.mainloop()