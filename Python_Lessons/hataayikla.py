# ================== Hesap Makinesi Fonksiyonları ==================

def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        raise ZeroDivisionError("Sıfıra bölme hatası!")
    return a / b


# ================== Ana Program ==================

def hesap_makinesi():
    islemler = []  # Yapılan işlemleri saklayan liste

    while True:
        print("\n--- HESAP MAKİNESİ ---")
        print("1- Toplama")
        print("2- Çıkarma")
        print("3- Çarpma")
        print("4- Bölme")
        print("5- Yapılan İşlemleri Göster")
        print("0- Çıkış")

        secim = input("Seçiminizi girin: ")

        if secim == "0":
            print("Programdan çıkılıyor...")
            break

        if secim == "5":
            print("\n--- İşlem Geçmişi ---")
            if not islemler:
                print("Henüz işlem yapılmadı.")
            else:
                for i in islemler:
                    print(i)
            continue

        try:
            a = float(input("1. sayıyı girin: "))
            b = float(input("2. sayıyı girin: "))

            if secim == "1":
                sonuc = topla(a, b)
                ifade = f"{a} + {b} = {sonuc}"

            elif secim == "2":
                sonuc = cikar(a, b)
                ifade = f"{a} - {b} = {sonuc}"

            elif secim == "3":
                sonuc = carp(a, b)
                ifade = f"{a} * {b} = {sonuc}"

            elif secim == "4":
                sonuc = bol(a, b)
                ifade = f"{a} / {b} = {sonuc}"

            else:
                print("❌ Hatalı seçim yaptınız!")
                continue

            print("✅ Sonuç:", sonuc)
            islemler.append(ifade)

        except ValueError:
            print("❌ Lütfen sadece sayısal değer girin!")

        except ZeroDivisionError as hata:
            print("❌ Hata:", hata)

        except Exception as e:
            print("❌ Beklenmeyen bir hata oluştu:", e)


# ================== Programı Başlat ==================
hesap_makinesi()
