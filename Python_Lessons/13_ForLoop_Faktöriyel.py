sayi = int(input("Lütfen bir sayı giriniz"))
faktoriyel = 1
for i in range (sayi,0,-1):
    faktoriyel *= i
print(str(sayi) + "faktöriyeli : " + str(faktoriyel))