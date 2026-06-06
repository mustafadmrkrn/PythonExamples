# 1. Ayaktaki Kısım
toplam = 0

# 2. Ayaktaki Kısım sonsuz döngü
while True:
    # 3. Ayaktaki Kısım kullanıcıdan sayı alma
    sayi = int(input("Bir sayı girin (Çıkmak için -1): "))
    # 4. Ayaktaki Kısım
    if sayi == 0:
        break
    
    # 5. Ayaktaki Kısım
    toplam = toplam + sayi
    
# 6. Ayaktaki Kısım
print("Toplam:", toplam)