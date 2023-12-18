liste5 = ["Türkçe", "Matematik","Fen Bilimleri"]
liste5.insert(1,"Kodlama")
for eleman in range (0,len(liste5)):
    print(liste5[eleman])

liste = ["a","b","c","d"]
liste.remove("c")
for eleman in range (0,len(liste)):
    print(liste[eleman])

liste2 = ["a","c","b","c","d"]
liste2.remove("c")
for eleman in range (0,len(liste2)):
    print(liste2[eleman])

sonuc = "b" in liste
print(sonuc)

indisNo = liste2.index("c")
metin = "C elemanına ait indis numarası {}"
print(metin.format(indisNo))