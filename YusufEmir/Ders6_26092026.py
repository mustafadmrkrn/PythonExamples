import random 
rastgele_sayi = random.randint(1,100)
sayac = 0
while True:
    cevap = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
    sayac += 1
    if cevap < rastgele_sayi:
        print("Daha büyük bir sayı tahmin edin.")
    elif cevap > rastgele_sayi:
        print("Daha küçük bir sayı tahmin edin.")
    else:
        print(f"Tebrikler! {sayac} denemede doğru tahmin ettiniz.")
        break