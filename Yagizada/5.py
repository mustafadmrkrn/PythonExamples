dogru_kullanici = "admin"
dogru_sifre = "1234"

hak = 0  # giriş sayacı

while True:
    kullanici = input("Kullanıcı adı: ")
    sifre = input("Şifre: ")
    hak += 1

    # 10'dan fazla giriş yapıldıysa sistem kitlenir
    if hak > 10:
        print("❌ Sistem kilitlendi! Çok fazla deneme yapıldı.")
        break

    if kullanici == dogru_kullanici and sifre == dogru_sifre:
        print("✔️ Giriş başarılı.")
        break

    elif kullanici != dogru_kullanici and sifre == dogru_sifre:
        print("❗ Kullanıcı adı yanlış, şifre doğru.")

    elif kullanici == dogru_kullanici and sifre != dogru_sifre:
        print("❗ Kullanıcı adı doğru, şifre yanlış.")

    elif kullanici == "" or sifre == "":
        print("❗ Kullanıcı adı veya şifre boş bırakılamaz.")

    elif len(sifre) < 4:
        print("❗ Şifre en az 4 karakter olmalı.")

    elif " " in kullanici:
        print("❗ Kullanıcı adı boşluk içeremez.")

    else:
        print("❗ Giriş başarısız. Bilinmeyen hata!")

    print(f"Kalan hak: {10 - hak}")
