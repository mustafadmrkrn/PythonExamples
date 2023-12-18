liste = list ()
liste = []
liste = ([1,2,3])
liste = ["a","b","c"]
liste = [1,"a",2,"b"]

liste = [1,3,5,7,9]
print(liste[1])
liste[1] = "üç"
print(liste[1])

print(liste[-1])
print(liste[-2])

uzunluk = len(liste)
print(uzunluk)

for eleman in liste:
    print(eleman)

for eleman in range (0,len(liste)):
    print(liste[eleman])

