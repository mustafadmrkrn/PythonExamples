print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")
islem = int(input("Lütfen yapmak istediğiniz işlemi seçiniz(1-2-3-4):"))
if (islem == 1) or (islem == 2) or (islem == 3) or (islem == 4):
  sayi1 = int(input("Lütfen birinci sayıyı giriniz"))
  sayi2 = int(input("Lütfen ikinci sayıyı giriniz"))
  if islem == 1:
    sonuc = sayi1 + sayi2
    metin = "Seçmiş olduğunuz işlemin sonucu: {}"
    print(metin.format(sonuc))
  elif islem == 2:
    sonuc = sayi1 - sayi2
    metin = "Seçmiş olduğunuz işlemin sonucu: {}"
    print(metin.format(sonuc))
  elif islem == 3:
    sonuc = sayi1 * sayi2
    metin = "Seçmiş olduğunuz işlemin sonucu: {}"
    print(metin.format(sonuc))
  else:
    sonuc = sayi1 / sayi2
    metin = "Seçmiş olduğunuz işlemin sonucu: {}"
    print(metin.format(sonuc))
else:
    print("Yalnış seçim Yaptınız!")