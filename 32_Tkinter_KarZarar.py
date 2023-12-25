from tkinter import *

def hesapla():
    try:
        alis_fiyati = float(alisFiyatiEntry.get())
        kilogram = float(kiloEntry.get())
        kar_orani = float(karOraniEntry.get())

        satis_fiyati = alis_fiyati * (1 + kar_orani / 100)
        kar_miktari = (satis_fiyati - alis_fiyati) * kilogram

        sonucLabel.config(text=f"Toplam Kar: {kar_miktari:.2f} TL")
    except ValueError:
        sonucLabel.config(text="Lütfen geçerli sayılar girin!")

pencere = Tk()
pencere.title("Kar Hesaplama")

frame = Frame(pencere)
frame.pack(padx=10, pady=10)

alisFiyatiLabel = Label(frame, text="Alış Fiyatı (TL):")
alisFiyatiLabel.grid(row=0, column=0, padx=5, pady=5)
alisFiyatiEntry = Entry(frame)
alisFiyatiEntry.grid(row=0, column=1, padx=5, pady=5)

kiloLabel = Label(frame, text="Kaç Kilogram:")
kiloLabel.grid(row=1, column=0, padx=5, pady=5)
kiloEntry = Entry(frame)
kiloEntry.grid(row=1, column=1, padx=5, pady=5)

karOraniLabel = Label(frame, text="Kar Oranı (%):")
karOraniLabel.grid(row=2, column=0, padx=5, pady=5)
karOraniEntry = Entry(frame)
karOraniEntry.grid(row=2, column=1, padx=5, pady=5)

hesaplaButton = Button(frame, text="Hesapla", command=hesapla)
hesaplaButton.grid(row=3, columnspan=2, padx=5, pady=5)

sonucLabel = Label(frame, text="Sonuç")
sonucLabel.grid(row=4, columnspan=2, padx=5, pady=5)

pencere.mainloop()
