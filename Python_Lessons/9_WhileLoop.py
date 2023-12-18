sayi = 1
while sayi <= 5:
  print(sayi)
  sayi +=1

while True:
  sayi = int(input("Lütfen bir sayı giriniz:"))
  if sayi % 2 == 0:
    print ("Girilen sayı çift sayıdır.")
  else:
    print ("Girilen sayı tek sayıdır.")
    break