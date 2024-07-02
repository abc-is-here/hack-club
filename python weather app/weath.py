from tkinter import *
from tkinter import ttk
import requests

# city_name = "Delhi"
# data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=81dcb6a1a95bc53294c8c197fd4de815").json()
# print(data)
# print(data["weather"][0]["description"])

def get_weather():
    city = city_name.get()
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=81dcb6a1a95bc53294c8c197fd4de815"
    response = requests.get(url).json()
    w_label1.config(text=response["weather"][0]["main"])
    wb_label1.config(text=response["weather"][0]["description"])
    temp_label1.config(text=str(int(response["main"]["temp"]-273.15)))
    per_label1.config(text=response["main"]["pressure"])

win = Tk()
win.title("Weather App")
win.config(bg = 'light blue')
win.geometry("500x550")

name_label = Label(win, text = "My Weather", font = ("Comic Sans MS", 30, "bold"), bg = 'light blue', fg = "Blue")
name_label.place(x = 25, y = 50, height=50, width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win, values = list_name, font = ("Comic Sans MS", 15, "bold"), textvariable=city_name)
com.place(x = 10, y = 120, height=40, width=480)
com.set("Select City")

button = Button(win,text = "Get Weather",relief=RAISED,font = ("Comic Sans MS", 20, "bold"),background='Blue', fg="White", command=get_weather)
button.place(x = 150, y = 180, height=40, width=200)

w_label = Label(win, text = "Weather", font = ("Comic Sans MS", 15, "bold"), bg = 'black', fg = "light blue")
w_label.place(x = 25, y = 260, height=50, width=210)

w_label1 = Label(win, text = "", font = ("Comic Sans MS", 15, "bold"), bg = 'black', fg = "light blue")
w_label1.place(x = 250, y = 260, height=50, width=210)

wb_label = Label(win, text = "Weather description", font = ("Comic Sans MS", 15, "bold"), bg = 'black', fg = "light blue")
wb_label.place(x = 25, y = 330, height=50, width=210)

wb_label1 = Label(win, text = "", font = ("Comic Sans MS", 15, "bold"), bg = 'black', fg = "light blue")
wb_label1.place(x = 250, y = 330, height=50, width=210)

temp_label = Label(win, text = "Temperature", font = ("Comic Sans MS", 15, "bold"), bg = 'black', fg = "light blue")
temp_label.place(x = 25, y = 400, height=50, width=210)

temp_label1 = Label(win, text = "", font = ("Comic Sans MS", 15, "bold"), bg = 'black', fg = "light blue")
temp_label1.place(x = 250, y = 400, height=50, width=210)

per_label = Label(win, text = "Pressure", font = ("Comic Sans MS", 15, "bold"), bg = 'black', fg = "light blue")
per_label.place(x = 25, y = 470, height=50, width=210)

per_label1 = Label(win, text = "", font = ("Comic Sans MS", 15, "bold"), bg = 'black', fg = "light blue")
per_label1.place(x = 250, y = 470, height=50, width=210)

win.mainloop()