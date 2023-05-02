import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk
import requests
import time

def getweather(canvas):
    city=textfield.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+ city+ "&appid=66c920c5c4fe56f1951fa6d3b75fa42e&units=metric"
    json_data=requests.get(api).json()

    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp'])
    final_info = condition
    final_data = str(temp)+"'c"
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
img=PhotoImage(file="C:\\Users\\AHANA\\Desktop\\weather\\weapic.png")
bg_image=tk.Label(canvas,image=img).place(x=0,y=0,relheight=1,relwidth=1)
f=("times new roman",15,"bold")
t=("times new roman",35,"bold")

textfield=tk.Entry(canvas,font=t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>',getweather)

label1=tk.Label(canvas,font=t)

label1.pack()

label2=tk.Label(canvas,font=t)
label2.pack()



canvas.mainloop()