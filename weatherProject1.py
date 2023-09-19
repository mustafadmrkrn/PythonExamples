import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = 'e14bd01142900098680620a88f2048f3'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def display_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    
    if weather_data['cod'] == 200:
        temperature = weather_data['main']['temp']
        weather_desc = weather_data['weather'][0]['description']
        result_label.config(text=f"Weather: {weather_desc}\nTemperature: {temperature}°C")
    else:
        messagebox.showerror("Error", "City not found or an error occurred.")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place widgets
city_label = tk.Label(root, text="Enter city name:")
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=display_weather)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=300)
result_label.pack()

# Start the GUI event loop
root.mainloop()
