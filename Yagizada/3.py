not1 = int(input("Sınav notunuzu giriniz: "))
not2 = int(input("Sınav notunuzu giriniz: "))   
ortalama = (not1 + not2) / 2
if ortalama <= 50:
    print("Kaldınız.")
elif ortalama > 50 and ortalama <= 70:
    print("Ortalamanız: ", ortalama, "Geçtiniz.")
else:
    print("Ortalamanız: ", ortalama, "Tebrikler, Başarılısınız.")