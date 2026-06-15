import random
print("Hoş Geldiniz!")
print("İlk 3 olan kazanır! (Çıkmak için 'q' tuşuna basabilirsiniz)\n")
secenekler = ["taş", "kağıt", "makas"]
oyuncu_skor = 0
bilgisayar_skor = 0
while oyuncu_skor < 3 and bilgisayar_skor < 3:
    oyuncu_secimi = input("Taş, Kağıt veya Makas? : ").lower()
    if oyuncu_secimi == 'q':
        print("Oyun isteğiniz üzerine sonlandırıldı.")
        break
    if oyuncu_secimi not in secenekler:
        print("Geçersiz giriş, lütfen taş, kağıt veya makas yazın.\n")
        continue
    bilgisayar_secimi = random.choice(secenekler)
    print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
    if oyuncu_secimi == bilgisayar_secimi:
        print("Durum Berabere!")
    elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
         (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
         (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
        print("Bu turu KAZANDINIZ! 🟢")
        oyuncu_skor += 1
    else:
        print("Bu turu bilgisayar kazandı. 🔴")
        bilgisayar_skor += 1
    print(f"SKOR -> Sen: {oyuncu_skor} | Bilgisayar: {bilgisayar_skor}\n")
if oyuncu_skor == 3:
    print("🏆 TEBRİKLER! Oyunu sen KAZANDIN! 🏆")
elif bilgisayar_skor == 3:
    print("💻 Maalesef oyunu bilgisayar kazandı. Başka sefere! 💻")