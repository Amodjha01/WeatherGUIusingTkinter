from tkinter import *
import tkinter as tk
from PIL import ImageTk
import requests
import time

def getweather():
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city+ "&appid=df4f9848baf352a17dd01df0078abbf9&units=metric"
    json_data = requests.get(api).json()

    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'])
    final_info = condition
    final_data = str(temp)+"'c"
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

# Load the image using the ImageTk module and store it as a global variable
image_path = r"C:\Users\amodd\Documents\AMODJHA\project\Weather_App\download.jpeg"
image = ImageTk.PhotoImage(file=image_path)
img_label = tk.Label(canvas, image=image)
img_label.place(x=0, y=0, relheight=1, relwidth=1)

f = ("times new roman", 15, "bold")
t = ("times new roman", 35, "bold")

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', lambda event: getweather())

label1 = tk.Label(canvas, font=t)
label1.pack()

label2 = tk.Label(canvas, font=t)
label2.pack()

canvas.mainloop()
