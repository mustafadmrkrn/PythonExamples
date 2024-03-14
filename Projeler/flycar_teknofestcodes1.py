class UcanAraba:
    def __init__(self, A, B, havalimanı):
        self.A = A
        self.B = B
        self.havalimanı = havalimanı

    def rota_belirle(self):
        rota = [self.A]  # Başlangıç noktasıyla başlayalım
        current_position = self.A
        
        while current_position != self.B:
            next_position = self.sonraki_noktayı_bul(current_position)
            if next_position is None:
                print("Hedefe ulaşılamıyor, rota sonlandırıldı.")
                break
            else:
                rota.append(next_position)
                current_position = next_position
        
        return rota

    def sonraki_noktayı_bul(self, current_position):
        # En yakın noktayı hesapla
        next_position = None
        min_distance = float('inf')
        
        for point in [point for point in [self.A, self.B] if point != current_position]:
            if self.izni_var_mi(current_position, point):
                distance = self.mesafeyi_hesapla(current_position, point)
                if distance < min_distance:
                    min_distance = distance
                    next_position = point
        
        return next_position

    def izni_var_mi(self, current_position, next_position):
        # Uçuşa yasak bölgeyi kontrol et
        return not self.havalimanı.kapsamında_mi(current_position, next_position)

    def mesafeyi_hesapla(self, current_position, next_position):
        # Basit mesafe hesabı için Euclidean mesafesini kullanabiliriz
        return ((next_position[0] - current_position[0])**2 + (next_position[1] - current_position[1])**2)**0.5


class Havalimani:
    def __init__(self, yasak_bolgeler):
        self.yasak_bolgeler = yasak_bolgeler

    def kapsamında_mi(self, current_position, next_position):
        # Verilen iki nokta arasında bir yasak bölge var mı kontrol et
        for yasak_bolge in self.yasak_bolgeler:
            if self.nokta_bolge_icinde_mi(yasak_bolge, next_position):
                return False
        return True
