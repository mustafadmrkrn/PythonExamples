from tkinter import *
import sqlite3

# Veritabanına bağlantıyı açın
baglanti = sqlite3.connect("uyelik_veritabani.db")

# Cursor (imleç) oluşturun
cursor = baglanti.cursor()

# Kullanıcılar tablosunu oluşturun
cursor.execute("""
    CREATE TABLE IF NOT EXISTS kullanicilar (
        kullanici_adi TEXT PRIMARY KEY,
        sifre TEXT,
        ad TEXT,
        soyad TEXT,
        adres TEXT,
        telefon TEXT,
        email TEXT
    )
""")

def kullanici_ekle(kullanici_adi, sifre, ad, soyad, adres, telefon, email):
    cursor.execute("""
        INSERT INTO kullanicilar (kullanici_adi, sifre, ad, soyad, adres, telefon, email)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (kullanici_adi, sifre, ad, soyad, adres, telefon, email))
    baglanti.commit()
    print(f"{kullanici_adi} adlı kullanıcı oluşturuldu.")

def kullanici_giris(kullanici_adi, sifre):
    cursor.execute("""
        SELECT * FROM kullanicilar WHERE kullanici_adi = ? AND sifre = ?
    """, (kullanici_adi, sifre))
    kullanici = cursor.fetchone()

    if kullanici:
        print(f"{kullanici_adi} adlı kullanıcı giriş yaptı.")
        return True
    else:
        print("Kullanıcı adı veya şifre hatalı.")
        return False




class UyelikSistemi:
    def __init__(self):
        self.kullanicilar = {}

    def kullanici_ekle(self, kullanici_adi, sifre, ad, soyad, adres, telefon, email):
        if kullanici_adi not in self.kullanicilar:
            self.kullanicilar[kullanici_adi] = {
                "sifre": sifre,
                "ad": ad,
                "soyad": soyad,
                "adres": adres,
                "telefon": telefon,
                "email": email
            }
            print(f"{kullanici_adi} adlı kullanıcı oluşturuldu.")
        else:
            print("Bu kullanıcı adı zaten mevcut.")

    def kullanici_giris(self, kullanici_adi, sifre):
        if kullanici_adi in self.kullanicilar and self.kullanicilar[kullanici_adi]["sifre"] == sifre:
            print(f"{kullanici_adi} adlı kullanıcı giriş yaptı.")
            return True
        else:
            print("Kullanıcı adı veya şifre hatalı.")
            return False

def uyelik_olustur():
    kullanici_adi = kullanici_adi_entry.get()
    sifre = sifre_entry.get()
    ad = ad_entry.get()
    soyad = soyad_entry.get()
    adres = adres_entry.get()
    telefon = telefon_entry.get()
    email = email_entry.get()

    uyelik_sistemi.kullanici_ekle(kullanici_adi, sifre, ad, soyad, adres, telefon, email)

def ac_uye_ol():
    uye_ol_pencere = Toplevel(pencere)
    uye_ol_pencere.geometry("250x300")
    uye_ol_pencere.title("Üye Ol")

    kullanici_adi_label = Label(uye_ol_pencere, text="Kullanıcı Adı:")
    kullanici_adi_label.pack()

    kullanici_adi_entry = Entry(uye_ol_pencere)
    kullanici_adi_entry.pack()

    sifre_label = Label(uye_ol_pencere, text="Şifre:")
    sifre_label.pack()

    sifre_entry = Entry(uye_ol_pencere, show="*")
    sifre_entry.pack()

    ad_label = Label(uye_ol_pencere, text="Ad:")
    ad_label.pack()

    ad_entry = Entry(uye_ol_pencere)
    ad_entry.pack()

    soyad_label = Label(uye_ol_pencere, text="Soyad:")
    soyad_label.pack()

    soyad_entry = Entry(uye_ol_pencere)
    soyad_entry.pack()

    adres_label = Label(uye_ol_pencere, text="Adres:")
    adres_label.pack()

    adres_entry = Entry(uye_ol_pencere)
    adres_entry.pack()

    telefon_label = Label(uye_ol_pencere, text="Telefon:")
    telefon_label.pack()

    telefon_entry = Entry(uye_ol_pencere)
    telefon_entry.pack()

    email_label = Label(uye_ol_pencere, text="E-mail:")
    email_label.pack()

    email_entry = Entry(uye_ol_pencere)
    email_entry.pack()

    def uyelik_olustur():
        kullanici_adi = kullanici_adi_entry.get()
        sifre = sifre_entry.get()
        ad = ad_entry.get()
        soyad = soyad_entry.get()
        adres = adres_entry.get()
        telefon = telefon_entry.get()
        email = email_entry.get()

        uyelik_sistemi.kullanici_ekle(kullanici_adi, sifre, ad, soyad, adres, telefon, email)

    uyelik_olustur_button = Button(uye_ol_pencere, text="Üyelik Oluştur", command=uyelik_olustur)
    uyelik_olustur_button.pack()

    ac_uye_ol_button = Button(pencere, text="Üye Ol", command=ac_uye_ol)
    ac_uye_ol_button.pack()



def giris_yap():
    kullanici_adi = kullanici_adi_entry.get()
    sifre = sifre_entry.get()

    if uyelik_sistemi.kullanici_giris(kullanici_adi, sifre):
        # Giriş başarılı, istenen işlemi yapabilirsiniz.
        pass

uyelik_sistemi = UyelikSistemi()

pencere = Tk()
pencere.geometry("250x200")
pencere.title("Üyelik Sistemi")

kullanici_adi_label = Label(pencere, text="Kullanıcı Adı:")
kullanici_adi_label.pack()

kullanici_adi_entry = Entry(pencere)
kullanici_adi_entry.pack()

sifre_label = Label(pencere, text="Şifre:")
sifre_label.pack()

sifre_entry = Entry(pencere, show="*")
sifre_entry.pack()

uye_ol_button = Button(pencere, text="Üye Ol", command=ac_uye_ol)
uye_ol_button.pack()

giris_yap_button = Button(pencere, text="Giriş Yap", command=giris_yap)
giris_yap_button.pack()

pencere.mainloop()

# Veritabanı bağlantısını ve imleci kapatın
baglanti.close()
cursor.close()