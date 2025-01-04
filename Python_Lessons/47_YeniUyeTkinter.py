from tkinter import *
from tkinter import messagebox

# Kaydet butonu işlevi
def kaydet():
    ad = adEntry.get()
    soyad = soyadEntry.get()
    if ad and soyad:  # Alanlar dolu mu kontrol et
        # Text kutusuna yeni üyeyi ekle
        uyeListesi.insert(END, f"{ad} {soyad}\n")
        # Mesaj kutusu göster
        messagebox.showinfo("Bilgi", f"Üyelik başarıyla kaydedildi!\nAd: {ad}\nSoyad: {soyad}")
        # Formu temizle
        adEntry.delete(0, END)
        soyadEntry.delete(0, END)
    else:
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurunuz!")

def uyari():
    cevap = messagebox.askyesnocancel("Uyarı", "Tüm bilgileriniz silinecek!")
    if cevap == True:
        sonuc["text"]="Evet'e Tıkladınız"
    elif cevap == False:
        sonuc["text"] = "Hayır'a Tıkladınız"
    else:
        sonuc["text"] = "İptal'e Tıkladınız."
     

sonuc = Label(text="Butona Tıklamadınız")
sonuc.pack()

# Pencere ayarları
pencere = Tk()
pencere.geometry("400x400")
pencere.title("Üyelik Sistemi")

# Yeni Üye Formu
yeniUye = LabelFrame(text="Yeni Üye Formu", width=380, height=140)
yeniUye.place(x=10, y=10)

# Ad etiketi ve giriş kutusu
adEtiket = Label(yeniUye, text="Adınız: ")
adEtiket.place(x=10, y=10)
adEntry = Entry(yeniUye)
adEntry.place(x=70, y=10)

# Soyad etiketi ve giriş kutusu
soyadEtiket = Label(yeniUye, text="Soyadınız: ")
soyadEtiket.place(x=10, y=40)
soyadEntry = Entry(yeniUye)
soyadEntry.place(x=70, y=40)

# Kaydet butonu
btn = Button(yeniUye, text="Kaydet", command=kaydet)
btn.place(x=165, y=70)

# Üye Listesi
uyeListesiEtiket = Label(pencere, text="Kayıtlı Üyeler:")
uyeListesiEtiket.place(x=10, y=160)

uyeListesi = Text(pencere, width=45, height=10, wrap=WORD)
uyeListesi.place(x=10, y=180)

# Pencere döngüsü
pencere.mainloop()
