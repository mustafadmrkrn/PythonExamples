alis_fiyati = int(input("Kilogram alış fiyatı:"))
kilogram_satis = int(input("Kaç kilogram satacaksın:"))
kar_orani = int(input("Yüzde kaç kar yapmak istiyorsunuz:"))
satis_fiyati = (alis_fiyati * kilogram_satis) / 100 * (100 + kar_orani)
metin = "Satış Fiyatı: {} TL"
print(metin.format(satis_fiyati))