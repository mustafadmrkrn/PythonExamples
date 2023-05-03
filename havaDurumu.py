import tkinter as tk
import urllib.request
import json

# OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"

def get_weather(city):
    # API request URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    # Extract weather data
    weather = {
        "description": data["weather"][0]["description"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }
    return weather

def show_weather(event=None):
    city = city_entry.get()
    if city:
        weather = get_weather(city)
        # Update weather labels
        desc_label.config(text=weather["description"])
        temp_label.config(text=f"{weather['temperature']}°C")
        humidity_label.config(text=f"{weather['humidity']}%")
        wind_speed_label.config(text=f"{weather['wind_speed']} m/s")

# Create Tkinter window
window = tk.Tk()
window.title("Hava Durumu")

# City entry widget
city_entry = tk.Entry(window, font=("Arial", 20))
city_entry.pack(padx=20, pady=20)
city_entry.bind("<Return>", show_weather)

# Weather labels
desc_label = tk.Label(window, font=("Arial", 16))
desc_label.pack()
temp_label = tk.Label(window, font=("Arial", 24, "bold"))
temp_label.pack()
humidity_label = tk.Label(window, font=("Arial", 16))
humidity_label.pack()
wind_speed_label = tk.Label(window, font=("Arial", 16))
wind_speed_label.pack()

# Show weather button
show_weather_button = tk.Button(window, text="Hava Durumu Göster", font=("Arial", 16), command=show_weather)
show_weather_button.pack(pady=20)

# Start Tkinter event loop
window.mainloop()
