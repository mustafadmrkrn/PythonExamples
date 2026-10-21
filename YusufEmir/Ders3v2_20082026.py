sayi = int(input("Bir sayı giriniz: "))
if sayi >0:
    print("Pozitif bir sayı girdiniz.")
elif sayi <0:
    print("Negatif bir sayı girdiniz.")
else:
    print("Sıfır girdiniz.")
    
not1 = int(input("Birinci notu giriniz: "))
not2 = int(input("İkinci notu giriniz: "))
ortalama = (not1 + not2) / 2
if ortalama < 50:
    print("Kaldınız.")
elif ortalama >= 50 and ortalama < 70:
    print("Orta.")
elif ortalama >= 70 and ortalama < 85:
    print("İyi.")
elif ortalama >= 85 and ortalama <= 100:
    print("Çok iyi.")
else:
    print("Geçersiz not girdiniz.")
