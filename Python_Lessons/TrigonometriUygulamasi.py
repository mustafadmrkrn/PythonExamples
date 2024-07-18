import math

def trigonometrik_degerler(acı):
    # Açıları radyan cinsine çevir
    acı_radyan = math.radians(acı)
    
    # Trigonometrik değerleri hesapla
    sin_deger = math.sin(acı_radyan)
    cos_deger = math.cos(acı_radyan)
    tan_deger = math.tan(acı_radyan)
    
    # Sonuçları yazdır
    print(f"Açı: {acı} derece")
    print(f"Sinüs: {sin_deger}")
    print(f"Kosinüs: {cos_deger}")
    print(f"Tanjant: {tan_deger}")

# Kullanıcıdan açı değeri al
aci = float(input("Açı (derece cinsinden): "))
trigonometrik_degerler(aci)
