def mesaj():
    print("Merhaba")
mesaj()
def topla(a,b):
    sonuc = a + b
    metin = "{} + {} : {}"
    print(metin.format(a,b,sonuc))

sayi1 = int(input("1.Sayı:"))
sayi2 = int(input("2.Sayı:"))
topla(sayi1,sayi2)