buyukHarfler = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVWXYZ"
kucukHarfler = "abcçdefgğhıijklmnoöprsştuüvwxyz"
rakamlar = "0123456789"
ozelKarakter = ".,*-_?"
bh_sayac = 0 #büyük harf sayısı
kh_sayac = 0 #küçük harf sayısı
r_sayac = 0 #rakam sayısı
ok_sayac = 0 #özel karakter sayısı
sifre = input("Lütfen Şifreninizi giriniz:")
for harf in sifre:
  if harf in buyukHarfler:
    bh_sayac +=1
  if harf in kucukHarfler:
    kh_sayac +=1
  if harf in rakamlar:
    r_sayac +=1
  if harf in ozelKarakter:
    ok_sayac +=1
if (bh_sayac == 0 or kh_sayac == 0 or r_sayac == 0 or ok_sayac ==0):
    print("Şifre güvenliği zayıf")
else:
    print("Şifre güvenliği yüksek")