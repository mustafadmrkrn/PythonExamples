# Su markaları ve pH değerleri
su_ph_listesi = {
    "Erikli": 6.5,
    "Saka": 8.22,
    "Hayat": 7.96,
    "Pınar": 7.65,
    "Fuska": 8.45,
    "Damla": 6.45,
    "Nestle": 7.18,
    "Buzdağı": 8.5,
    "Sırma": 7.6
}

# Kullanıcıdan marka ismi al
marka = input("Su markasını girin: ").capitalize()

# Marka listede varsa pH değerini göster
if marka in su_ph_listesi:
    ph = su_ph_listesi[marka]
    print(f"{marka} markasının pH değeri: {ph}")
    
    if ph < 7:
        print("Bu su asidik.")
    elif ph == 7:
        print("Bu su nötr.")
    else:
        print("Bu su bazik.")
else:
    print("Bu marka listede yok.")