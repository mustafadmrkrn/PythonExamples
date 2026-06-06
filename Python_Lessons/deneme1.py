sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
toplam = sayi1 + sayi2
if toplam <50 or toplam >60:
    print("Toplam 50'den küçük veya 60'dan büyük")
elif toplam == 50 or toplam == 60:
    print("Toplam 50 veya 60")