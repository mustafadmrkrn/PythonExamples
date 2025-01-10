import requests
import json

# Güncel API URL ve anahtarınızı buraya ekleyin.
api_url = "https://api.apilayer.com/exchangerates_data/latest"
api_key = "API_KEYINIZ"  # API anahtarınızı buraya yazın.

headers = {
    "apikey": api_key
}

# Kullanıcıdan veri alma
bozulan_doviz = input("Bozulan döviz türü (ör. USD): ").upper()
alinan_doviz = input("Alınan döviz türü (ör. EUR): ").upper()
miktar = float(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

# API isteği gönderme
response = requests.get(f"{api_url}?base={bozulan_doviz}", headers=headers)

# Yanıtı kontrol etme
if response.status_code == 200:
    data = response.json()
    try:
        rate = data["rates"][alinan_doviz]
        print(f"1 {bozulan_doviz} = {rate} {alinan_doviz}")
        print(f"{miktar} {bozulan_doviz} = {miktar * rate} {alinan_doviz}")
    except KeyError:
        print(f"Hatalı döviz türü girdiniz: {alinan_doviz}")
else:
    print(f"API isteği başarısız! Hata kodu: {response.status_code}")
    print("Detay:", response.text)
