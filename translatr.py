from tkinter import *
from tkinter import ttk
from googletrans import Translator as trs
from googletrans import LANGUAGES as lng

def conversion(text="type", src = "english", dest = "hindi"):
    text1 = text
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
root.geometry("500x800")
root.config(bg = 'light blue')

lab_txt = Label(root, text = "Translator", font = ("times roman new", 40, "bold"), bg='light blue', fg='white')
lab_txt.place(x = 100, y = 40, height=50, width=300)

frame = Frame(root).pack(side = BOTTOM)

lab_txt = Label(root, text = "Source text", font = ("times roman new", 20, "bold"), bg='light blue', fg='grey')
lab_txt.place(x = 100, y = 100, height=20, width=300)

src_txt = Text(frame, font = ("times roman new", 30, "bold"), wrap=WORD)
src_txt.place(x = 10, y = 130, height=200, width=480)

list_txt = list(lng.values())

com_src = ttk.Combobox(frame, values = list_txt)
com_src.place(x = 10, y = 350, height=40, width=150)
com_src.set("English")

button_change = Button(frame, text = "Translate", relief=RAISED, command=data)
button_change.place(x = 170, y = 350, height=40, width=150)

com_dest = ttk.Combobox(frame, values = list_txt)
com_dest.place(x = 340, y = 350, height=40, width=150)
com_dest.set("Hindi")

lab_txt = Label(root, text = "Destination text", font = ("times roman new", 20, "bold"), bg='light blue', fg='grey')
lab_txt.place(x = 100, y = 410, height=20, width=300)

dest_txt = Text(frame, font = ("times roman new", 30, "bold"), wrap=WORD)
dest_txt.place(x = 10, y = 450, height=200, width=480)

root.mainloop()