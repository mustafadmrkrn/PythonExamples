sayi = int(input("Lütfen bir sayı giriniz:"))
durum = False
if sayi>1:
  for i in range(2,sayi):
    if (sayi % i) ==0:
      durum = True
      break
  if durum == True:
    print(str(sayi) + "Asal sayı değildir")
  else:
      print(str(sayi) + "Asal Sayıdır")
else:
  print(str(sayi) + "Asal sayı değildir.")