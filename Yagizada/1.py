not1 = int(input("Birinci notu girin: "))
not2 = int(input("İkinci notu girin: "))
ortalama = (not1 + not2) / 2

if ortalama < 45:
    print("Kaldınız.")
elif ortalama >= 90 and ortalama <= 100:
    print("Tebrikler, yüksek not aldınız.")
elif ortalama >= 45:
    print("Geçtiniz.")
else:
    print("Geçtiniz, ancak daha yüksek not alabilirsiniz.")