import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(api_key, city):
    base_url = "http://api.weatherstack.com/current"
    params = {"query": city, "access_key": api_key, "units": "m"} 
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        if "current" in weather_data and "temperature" in weather_data["current"]:
            temperature = weather_data["current"]["temperature"]
            description = weather_data["current"]["weather_descriptions"][0]
            result_text = f"The weather in {city} is {temperature}°C with {description}."
            result_label.config(text=result_text)
        else:
            messagebox.showerror("Error", "Unable to parse weather data. Response format might have changed.")
    else:
        messagebox.showerror("Error", f"Unable to fetch weather data. Status code: {response.status_code}")

def get_weather_button_click():
    city_name = city_entry.get()
    get_weather(api_key, city_name)

api_key = '95a83cbcced4d4263baf5372489e9d0e'

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter the city name:")
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=10)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather_button_click)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

while True:
    try:
        root.update()
    except tk.TclError:
        break

