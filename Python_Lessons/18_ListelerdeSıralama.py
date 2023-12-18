liste = [30,3,56,25,8]
liste.sort()
print("Küçükten büyüğe sıralama")
for eleman in range(0,len(liste)):
    print(liste[eleman])
print("büyükten küçüğe sıralama")
liste.reverse()
for eleman in range (0,len(liste)):
    print(liste[eleman])

kucuk = min(liste)
buyuk = max(liste)
metin1 = "Listenin en büyük elemanı:{}"
metin2 = "Listenin en küçük elemanı:{}"
print(metin1.format(kucuk))
print(metin2.format(buyuk))