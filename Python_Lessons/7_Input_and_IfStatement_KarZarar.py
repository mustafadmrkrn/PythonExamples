alisfiyati = int(input("Kilogram alış fiyatı:"))
kilogramsatis = int(input("Kaç kilogram satacaksın:"))
karorani = int(input("Yüzde kaç kar yapmak istiyorsunuz:"))
satisfiyati = (alisfiyati * kilogramsatis) / 100 * (100 + karorani)
karorani1 = satisfiyati - (alisfiyati * kilogramsatis)
maliyet = (alisfiyati * kilogramsatis)
metin2 = "Kar Oranı: {} TL"
metin = "Satış Fiyatı: {} TL"
metin3 = "Ürünün Maliyet Fiyatı {}"
print(metin.format(satisfiyati))
print(metin2.format(karorani1))
print(metin3.format(maliyet))

sayi = int(input("Lütfen bir sayı giriniz:"))
kalan = sayi % 2
if kalan == 0:
  print("Girilen sayı çift sayıdır.")
else:
  print("Girilen sayı tek sayıdır.")