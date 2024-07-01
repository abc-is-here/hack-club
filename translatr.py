from tkinter import *
from tkinter import ttk
from googletrans import Translator as trs
from googletrans import LANGUAGES as lng

color1 = '#020f12'
color2 = '#05d7ff'
color3 = '#65e7ff'
color4 = 'BLACK'

def conversion(text="type", src = "english", dest = "hindi"):
    src1 = src
    dest1 = dest
    trans = trs()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text


def data():
    s = com_src.get()
    d = com_dest.get()
    msg = src_txt.get(1.0, END)
    textget = conversion(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x680")
root.config(bg = 'black')

img = PhotoImage(file = 'assets/logo.png')
root.iconphoto(False, img)

lab_txt = Label(root, text = "Translator", font = ("Comic Sans MS", 40, "bold"), bg = 'black', fg=color2)
lab_txt.place(x = 100, y = 25, height=50, width=300)

frame = Frame(root).pack(side = BOTTOM)

lab_txt = Label(root, text = "Source text", font = ("Comic Sans MS", 20, "bold"), bg = 'black', fg='WHITE')
lab_txt.place(x = 100, y = 90, height=25, width=300)

src_txt = Text(frame, font = ("Comic Sans MS", 30, "bold"), wrap=WORD, bg='GREY', fg='WHITE')
src_txt.place(x = 10, y = 130, height=200, width=480)

list_txt = list(lng.values())

com_src = ttk.Combobox(frame, values = list_txt, font = ("Comic Sans MS", 15, "bold"))
com_src.place(x = 10, y = 350, height=40, width=150)
com_src.set("English")

button_change = Button(frame,text = "changes to",relief=RAISED,command=data,font = ("Comic Sans MS", 20, "bold"),background=color2,
    foreground=color4,
    activebackground=color3,
    activeforeground=color1,
    highlightthickness=2,
    highlightbackground=color2,
    highlightcolor='WHITE',
    border=0,
    cursor="hand1",
    )
button_change.place(x = 170, y = 350, height=40, width=160)

com_dest = ttk.Combobox(frame, values = list_txt, font = ("Comic Sans MS", 15, "bold"))
com_dest.place(x = 340, y = 350, height=40, width=150)
com_dest.set("Hindi")

lab_txt = Label(root, text = "Destination text", font = ("Comic Sans MS", 20, "bold"), bg = 'black', fg="WHITE")
lab_txt.place(x = 100, y = 410, height=25, width=300)

dest_txt = Text(frame, font = ("Comic Sans MS", 30, "bold"), wrap=WORD, bg='GREY', fg='WHITE')
dest_txt.place(x = 10, y = 450, height=200, width=480)

root.mainloop()