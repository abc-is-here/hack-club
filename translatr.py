from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg = 'light blue')

lab_txt = Label(root, text = "Translator", font = ("times roman new", 40, "bold"), bg='light blue', fg='white')
lab_txt.place(x = 100, y = 40, height=50, width=300)

frame = Frame(root).pack(side = BOTTOM)

lab_txt = Label(root, text = "Source text", font = ("times roman new", 20, "bold"), bg='light blue', fg='grey')
lab_txt.place(x = 100, y = 100, height=20, width=300)

src_txt = Text(frame, font = ("times roman new", 40, "bold"), wrap=WORD)
src_txt.place(x = 10, y = 130, height=200, width=480)

list_txt = [1,2,3,4]

com_src = ttk.Combobox(frame, values = list_txt)
com_src.place(x = 10, y = 350, height=40, width=90)
com_src.set("English")

root.mainloop()