names = ["Ali", "Yaðmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

#1 "Cenk" ismini listenin sonuna ekleyeniz.

names.append("Cenk")

#2 "Sena" deðerini listenin baþýna ekleyiniz.

names.insert(0,"Sena")

#3-4 "Deniz" isminin index nosu ve listeden siliniz. index=4

# names.remove("Deniz")
# index = names.index("Deniz")
# print(index)

#5 "Ali" listenin bir elemaný mýdýr?

# result = "Ali" in names
# result = names.index("Ali") - -1 den büyük bir deðer getiriyorsa liste içindeki index nosunu verir.
#6 Liste elemanlarýný ters çevirin.


names.reverse()


#7 Liste elemanlarýný alfabetik olarak sýralayýnýz.

names.sort()

#8 years listesini rakamsal büyüklüðe göre sýralayýnýz.

years.sort()
years.reverse()



#9 karakter dizisini listeye çeviriniz.

#str = "Chevrolet, Dacia" 
# cars = "Chevrolet", "Dacia"
# cars = cars.split(",")
# print(cars)

#10 years dizisinin en büyük ve en küçük elemaný nedir?

# print(min(years))
# print(max(years))

#11 years dizisinde kaç tane 1998 deðeri vardýr?

# print(years.count(1998))

#12 years dizisinin tüm elemanlarýný siliniz.

years.clear()

#13 Kullanýcýdan alacaðýnýz 3 tane marka bilgisini bir listede saklayýnýz.

# cars.append(["Ford","Mercedes","BMW"])
markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)


# print(names)
# print(years)
# print(cars)
# print(result)