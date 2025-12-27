kullanici = "admin"
sifre = "1234"

if kullanici == "admin" and sifre == "1234":
    print("Giriş başarılı.")
elif kullanici == "admin" or sifre != "1234":
    print("Kullanıcı adı veya şifre hatalı.")
else:
    print("Giriş başarısız.")