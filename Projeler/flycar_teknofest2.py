class UcanAraba:
    def __init__(self):
        self.gnss = True
        self.radar = True
        self.barometre = True

    def iniş_tamamla(self):
        print("B noktasına iniş başlatılıyor...")
        if not self.gnss or not self.radar or not self.barometre:
            self.alternatif_iniş()
        else:
            print("Normal iniş tamamlandı.")

    def alternatif_iniş(self):
        print("Veri kaybı yaşandığı için alternatif iniş prosedürü başlatılıyor...")
        # Alternatif iniş prosedürleri burada uygulanır.
        # Örneğin, acil iniş yeri seçimi veya alternatif sensörlerin kullanımı.

# Örnek kullanım
if __name__ == "__main__":
    ucan_araba = UcanAraba()
    # Veri kaybı durumunu simüle etmek için GNSS, radar ve barometre verilerini devre dışı bırakabiliriz.
    ucan_araba.gnss = False
    ucan_araba.radar = False
    ucan_araba.barometre = False
    ucan_araba.iniş_tamamla()
