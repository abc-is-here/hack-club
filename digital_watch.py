from tkinter import *
import datetime

def dat_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    minu = time.strftime("%M")
    sec = time.strftime("%S")
    ampm = time.strftime("%p")
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%Y")
    day = time.strftime("%A")
    hr_label.config(text=hr)
    min_label.config(text=minu)
    sec_label.config(text=sec)
    ampm_label.config(text=ampm)
    date_label.config(text=date)
    month_label.config(text=month)
    year_label.config(text=year)
    day_label.config(text=day)
    hr_label.after(1000, dat_time)

clock = Tk()

clock.title("Digital Clock")
clock.geometry("1000x500")
clock.configure(bg="black")

title_label = Label(clock, text="Digital Clock", font=("Comic Sans Ms", 44, "bold"), bg="black", fg="white")
title_label.pack(side=TOP)

hr_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
hr_label.place(x=40+170, y=120, height=110, width=100)

hr_label_txt = Label(clock, text="hrs", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
hr_label_txt.place(x=40+170, y=200, height=60, width=100)

min_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
min_label.place(x=200+170, y=120, height=110, width=100)

min_label_txt = Label(clock, text="Min", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
min_label_txt.place(x=200+170, y=200, height=60, width=100)

sec_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
sec_label.place(x=360+170, y=120, height=110, width=100)

sec_label_txt = Label(clock, text="Sec", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
sec_label_txt.place(x=360+170, y=200, height=60, width=100)

ampm_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
ampm_label.place(x=520+170, y=120, height=110, width=100)

date_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
date_label.place(x=40+170, y=300, height=110, width=100)

date_label_txt = Label(clock, text="Date", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
date_label_txt.place(x=40+170, y=380, height=60, width=100)

month_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
month_label.place(x=200+170, y=300, height=110, width=100)

month_label_txt = Label(clock, text="Month", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
month_label_txt.place(x=200+170, y=380, height=60, width=100)

year_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
year_label.place(x=360+170, y=300, height=110, width=100)

year_label_txt = Label(clock, text="Year", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
year_label_txt.place(x=360+170, y=380, height=60, width=100)

day_label = Label(clock, text="00", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
day_label.place(x=520+170, y=300, height=110, width=130)

day_label_txt = Label(clock, text="Day", font=("Comic Sans Ms", 20, "bold"), bg="white", fg="black")
day_label_txt.place(x=520+170, y=380, height=60, width=130)

dat_time()

clock.mainloop()