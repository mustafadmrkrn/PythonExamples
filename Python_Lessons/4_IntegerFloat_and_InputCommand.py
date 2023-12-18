not1 = 85
not2 = 95
ortalama = (not1 + not2) / 2
metin = "Notları {} ve {} olan öğrencilerin ortalaması {}'dır."
print (metin.format(not1, not2, ortalama))

sayi1 = input ("1. sayıyı giriniz:")
sayi2 = input ("2. sayıyı giriniz:")
toplam = int(sayi1) + int(sayi2)
metin = "{} sayısı ile {} sayısının toplamı {}"
print (metin.format(sayi1, sayi2, toplam))


sayi1 = input ("1. sayıyı giriniz:")
sayi2 = input ("2. sayıyı giriniz:")
toplam = float(sayi1) / float(sayi2)
metin = "{} sayısı ile {} sayısının bölümü {}"
print (metin.format(sayi1, sayi2, toplam))
