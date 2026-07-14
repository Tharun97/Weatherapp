import tkinter as tk
import requests as rq

from tkinter import *

root = Tk()
root.title("Weather App")
root.geometry("400x350")

#Base URL
BASE_URL="http://api.openweathermap.org/data/2.5/weather?"

#API key
API_KEY="493de4bfea9b9cf5f9ea162f5421ebb9"

#Function to get weather data
def get_weather():
    city=city_entry.get()
    #prepare our data
    params={
        "q":city,
        "appid":API_KEY,
        "units":"metric",
        }
    #send request
    response=rq.get(BASE_URL,params=params)
    data=response.json()
    print(data)
    if data['cod']==200:
        temp=data['main']['temp']
        weather_description=data['weather'][0]['description']
        output_label=tk.Label(root,font=("Arial",15))
        output_label.pack(pady=10)
        output_label.config(text=f"Temperature:{temp} °C"
                            f"\nDescription: {weather_description}")
    else:
            output_label.config(text="City Not Found")

#Top label
top_label=tk.Label(root,text="Weather App",font=("Arial",20))
top_label.pack(pady=10)

#City label
city_label=tk.Label(root,text="Enter the city name:",font=("Arial",15))
city_label.pack(pady=10)

#Entry Box
city_entry=tk.Entry(root,font=("Arial",15))
city_entry.pack(pady=10)

#submit button
submit_btn=tk.Button(root,text="Submit",font=("Arial",15),command=get_weather)
submit_btn.pack(pady=10)


root.mainloop()
