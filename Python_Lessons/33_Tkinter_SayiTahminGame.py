import random
from tkinter import *

def tahmin_et():
    global tahmin_sayisi
    try:
        tahmin = int(tahminEntry.get())
        tahmin_sayisi += 1
        if tahmin == rastgele_sayi:
            sonucLabel.config(text=f"Tebrikler! {tahmin_sayisi}. denemede doğru tahmin ettiniz.")
        elif tahmin < rastgele_sayi:
            sonucLabel.config(text="Daha büyük bir sayı deneyin.")
        else:
            sonucLabel.config(text="Daha küçük bir sayı deneyin.")
    except ValueError:
        sonucLabel.config(text="Lütfen bir sayı girin!")

def yeni_oyun():
    global rastgele_sayi, tahmin_sayisi
    rastgele_sayi = random.randint(1, 100)
    tahmin_sayisi = 0
    sonucLabel.config(text="Yeni oyuna başlandı. 1 ile 100 arasında bir sayı tuttum.")

pencere = Tk()
pencere.title("Sayı Tahmin Oyunu")

rastgele_sayi = random.randint(1, 100)
tahmin_sayisi = 0

frame = Frame(pencere)
frame.pack(padx=10, pady=10)

tahminLabel = Label(frame, text="Tahmininizi Girin (1-100):")
tahminLabel.grid(row=0, column=0, padx=5, pady=5)
tahminEntry = Entry(frame)
tahminEntry.grid(row=0, column=1, padx=5, pady=5)

tahminButton = Button(frame, text="Tahmin Et", command=tahmin_et)
tahminButton.grid(row=1, columnspan=2, padx=5, pady=5)

sonucLabel = Label(frame, text="Başlayalım!")
sonucLabel.grid(row=2, columnspan=2, padx=5, pady=5)

yeniOyunButton = Button(frame, text="Yeni Oyun", command=yeni_oyun)
yeniOyunButton.grid(row=3, columnspan=2, padx=5, pady=5)

pencere.mainloop()