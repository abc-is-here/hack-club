from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Weather App")
win.config(bg = 'light blue')
win.geometry("500x550")

name_label = Label(win, text = "My Weather", font = ("Comic Sans MS", 30, "bold"), bg = 'light blue', fg = "Blue")
name_label.place(x = 25, y = 50, height=50, width=450)

list_name = [1,2,3,4,5,6,7,8,9,10]

com = ttk.Combobox(win, values = list_name, font = ("Comic Sans MS", 15, "bold"))
com.place(x = 10, y = 120, height=40, width=480)
com.set("Select City")

button = Button(win,text = "Get Weather",relief=RAISED,font = ("Comic Sans MS", 20, "bold"),background='Blue', fg="White")
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