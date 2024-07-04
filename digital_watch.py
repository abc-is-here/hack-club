from tkinter import *

clock = Tk()

clock.title("Digital Clock")
clock.geometry("1000x500")
clock.configure(bg="black")

title_label = Label(clock, text="Digital Clock", font=("Comic Sans Ms", 44, "bold"), bg="black", fg="white")
title_label.pack(side=TOP)

hr_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
hr_label.place(x=40+170, y=120, height=110, width=100)

min_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
min_label.place(x=200+170, y=120, height=110, width=100)

sec_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
sec_label.place(x=360+170, y=120, height=110, width=100)

ampm_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
ampm_label.place(x=520+170, y=120, height=110, width=100)

date_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
date_label.place(x=40+170, y=300, height=110, width=100)

month_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
month_label.place(x=200+170, y=300, height=110, width=100)

year_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
year_label.place(x=360+170, y=300, height=110, width=100)

day_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
day_label.place(x=520+170, y=300, height=110, width=100)


clock.mainloop()