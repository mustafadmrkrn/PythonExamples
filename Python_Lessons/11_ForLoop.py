kelime = input("Lütfen bir kelime giriniz:")
for harf in kelime:
  print(harf)

for sayi in range(5):
  print(sayi)

for sayi in range(5,11):
  print(sayi)

for sayi in range(10):
  if not sayi % 2 == 1:
    continue
  print(sayi)

yukseklik = int(input("Lütfen pramitin yüksekliğini giriniz:"))
for i in range(yukseklik):
  print(' '*(yukseklik-i-1) + '*'*(2*i+1))