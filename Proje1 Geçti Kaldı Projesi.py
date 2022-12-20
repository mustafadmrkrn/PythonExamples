not1 = int(input("Lütfen 1. sınav notunuzu giriniz:"))
not2 = int(input("Lütfen 2. sınav notunuzu giriniz:"))
ortalama = (not1 + not2) / 2
if ortalama < 45:
  print("Başarısız")
elif ortalama >=45 and ortalama < 55:
  print("Geçer")
elif ortalama >=55 and ortalama < 70:
  print("Orta")
elif ortalama >=70 and ortalama < 85:
  print("İyi")
elif ortalama >=85 and ortalama < 100:
  print("Pekiyi")