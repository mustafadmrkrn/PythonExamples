import random
Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

password_len = int(input("Şifre kaç karakterden oluşturulsun : "))
password_count = int(input("Kaç adet şifre oluşturulsun : "))
for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(Chars)
            password      = password + password_char
        print("Random Şifreniz : " , password)