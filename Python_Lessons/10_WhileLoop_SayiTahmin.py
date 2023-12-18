import random
rastgeleSayi = random.randint(1,100)
sayac = 0
while True:
  cevap = int(input("Tahmininiz(1-100):"))
  sayac+=1
  if cevap > rastgeleSayi:
    print("Lütfen daha küçük bir sayı giriniz")
  elif cevap < rastgeleSayi:
    print("Lütfen daha büyük bir sayı giriniz")
  else:
    metin = "Tebrikler {}. Tahmininizde bildiniz"
    print(metin.format(sayac))
    break