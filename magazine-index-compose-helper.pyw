# -*- coding: utf8 -*-

import configparser
import io
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

config_addr = "config.ini"
config = configparser.ConfigParser()
config.read(config_addr)
icon_file = config.get("icon", "window_icon")

def show_label_for_textfield2(event):
    print(event)

def parse_form(event):
    """
    Parses text input from two textfields.
    Puts formatted input into one of two files
    (one for Companies, second for Non-profit organisations).
    Format:
    Name - Page
    """
    name = ent.get()
    print(name)
    ent.delete(0, END)
    page = ent2.get()
    if Choise2.get() == u"Компания":
        org_type = "1"
    else:
        org_type = "0"
    with io.open(Choise2.get() + ".txt", encoding="utf8", mode="a+") as f:
            f.write(name + " - " + page + "\n")

root = Tk()
root.title("Добавить компанию или организацию в индекс")
try:
    window_icon = PhotoImage(file=icon_file)
    root.tk.call("wm", "iconphoto", root._w, window_icon)
except Exception as e:
    print("Exception: %s" % (e))
root.geometry("450x200")

# Textfield for the number of page with mentioned company / organisation
Label(root, text="Номер страницы внутри PDF-файла").pack(side=TOP)
ent2 = Entry(root, width=3, font="Verdana 14")
ent2.pack(side=TOP)
ent2.bind("<Return>", show_label_for_textfield2)

Choise2 = StringVar(root)
Choise2.set("Компания")
w2 = OptionMenu(root, Choise2,
                "Компания",
                "Организация")
w2.pack()

# Textfield for the name of the mentioned company/organisation
ent = Entry(root, width=25, font="Verdana 14")
ent.pack(side=TOP)
ent.focus()
ent.bind("<Return>", parse_form)
Label(root, text="Название").pack(side=TOP)
# Reminder on editorial mentioning format
Label(root, text="Птицефабрика «Синявинская» >> Синявинская, птицефабрика", bg="#f5f5eb", font="Times 10").pack(side=TOP)

root.mainloop()
