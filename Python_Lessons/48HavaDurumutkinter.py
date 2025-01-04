import tkinter as tk
from tkinter import messagebox
import requests

# API bilgileri
API_KEY = "3108732aa0add8bd40b4facbcef12fa2"  # OpenWeatherMap API anahtarınızı buraya yazın
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Şehir bilgisine göre hava durumu verilerini al
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Uyarı", "Lütfen bir şehir adı girin!")
        return
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # Sıcaklık birimi: Celsius
        "lang": "tr"        # Dil: Türkçe
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Hava durumu verilerini al ve ekrana yazdır
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        
        # Gece veya gündüz durumu
        is_night = "n" in data["weather"][0]["icon"]
        
        result_label.config(
            text=f"Hava Durumu: {weather}\n"
                 f"Sıcaklık: {temp}°C\n"
                 f"Nem: %{humidity}"
        )
        
        # Hava durumuna göre efekt göster
        update_weather_effect(weather, is_night)
        
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Hata", "API isteği başarısız oldu!")
    except KeyError:
        messagebox.showerror("Hata", "Şehir bulunamadı!")

# Hava durumuna göre efekt güncelle
def update_weather_effect(weather, is_night):
    canvas.delete("all")
    
    # Gece ve gündüz arka planı
    if is_night:
        canvas.config(bg="darkblue")
        canvas.create_text(100, 20, text="Gece", font=("Arial", 16), fill="white")
        canvas.create_oval(50, 50, 100, 100, fill="yellow", outline="yellow")  # Ay
    else:
        canvas.config(bg="skyblue")
        canvas.create_text(100, 20, text="Gündüz", font=("Arial", 16), fill="black")
        canvas.create_oval(50, 50, 150, 150, fill="yellow", outline="orange")  # Güneş
    
    # Hava durumu efektleri
    weather = weather.lower()
    
    if "güneş" in weather or "açık" in weather:
        canvas.create_text(100, 200, text="Güneşli", font=("Arial", 14), fill="black")
    
    elif "yağmur" in weather:
        for i in range(5):
            canvas.create_line(80 + i * 10, 110, 80 + i * 10, 150, fill="blue", width=2)
        canvas.create_text(100, 200, text="Yağmurlu", font=("Arial", 14), fill="white" if is_night else "black")
    
    elif "kar" in weather:
        for i in range(8):
            x = 50 + i * 15
            y = 70
            canvas.create_oval(x, y, x + 10, y + 10, fill="white", outline="white")
        canvas.create_text(100, 200, text="Karlı", font=("Arial", 14), fill="white" if is_night else "black")
    
    elif "bulut" in weather:
        canvas.create_oval(60, 70, 140, 110, fill="lightgray", outline="gray")
        canvas.create_oval(90, 50, 160, 100, fill="lightgray", outline="gray")
        canvas.create_text(100, 200, text="Bulutlu", font=("Arial", 14), fill="white" if is_night else "black")
    
    elif "sis" in weather:
        for i in range(5):
            canvas.create_rectangle(50, 60 + i * 20, 150, 70 + i * 20, fill="gray", outline="gray")
        canvas.create_text(100, 200, text="Sisli", font=("Arial", 14), fill="white" if is_night else "black")
    
    else:
        canvas.create_text(100, 100, text="Efekt Bulunamadı", font=("Arial", 14), fill="red")

# Tkinter arayüzü
root = tk.Tk()
root.title("Hava Durumu")

# Şehir girişi
tk.Label(root, text="Şehir Adı:").pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Hava durumu sorgulama butonu
tk.Button(root, text="Hava Durumunu Getir", command=get_weather).pack(pady=10)

# Sonuç etiketi
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

# Hava durumu efektleri için Canvas
canvas = tk.Canvas(root, width=200, height=250, bg="white")
canvas.pack(pady=10)

# Pencereyi çalıştır
root.mainloop()
