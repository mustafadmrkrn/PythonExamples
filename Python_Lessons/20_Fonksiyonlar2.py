def hesapla(a,b,c):
    if c==1:
        sonuc = a + b
        metin = "{} + {} : {}"
    elif c==2:
        sonuc = a - b
        metin = "{} - {} : {}"
    elif c==3:
        sonuc = a * b
        metin = "{} * {} : {}"
    elif c==4:
        sonuc = a / b
        metin = "{} / {} : {}"
    print(metin.format(a,b,sonuc))
while (True):
    print("Lütfen seçim yapınız")
    secim = int(input("1. Toplama 2. Çıkarma 3. Çarpma 4. Bölme 0. Çıkış"))
    if secim ==1 or secim==2 or secim==3 or secim==4:
        sayi1 = int(input("1.Sayı"))
        sayi2 = int(input("2.Sayı"))
        hesapla(sayi1,sayi2,secim)
    elif secim ==0:
        print("Hoşçakalın")
        break
    else: print("Yalnış seçim yaptınız...")
    