import dny
import tkinter as tk
from datetime import datetime


window = tk.Tk()
window.geometry("800x670")
window.configure(background="black")
window.title("Docházka")

entry_prichody_list = []
entry_odchody_list = []
label_rozdil = []


def button_click():
    for entryp, entryo, rozdil in zip(entry_prichody_list, entry_odchody_list, label_rozdil):
        if entryp.get():

            p = datetime.strptime(entryp.get(), "%H:%M")
            o = datetime.strptime(entryo.get(), "%H:%M")
            r = str(o - p)[:-3]
            rozdil["text"] = r
        else:
            rozdil["text"] = ""


datum_label = tk.Label(window, text="Datum", bg="black", fg="white")
datum_label.grid(row=0, column=0)

prichod_label = tk.Label(window, text="Příchod", bg="black", fg="white")
prichod_label.grid(row=0, column=1)

odchod_label = tk.Label(window, text="Odchod", bg="black", fg="white")
odchod_label.grid(row=0, column=2)

for day in range(dny.pocet(9)):
    Label_datum = tk.Label(window, text=dny.datumy(9, day), padx=20, bg="black", fg="white")
    Label_datum.grid(row=day + 1, column=0)

for i in range(dny.pocet(9)):
    entry_prichod = tk.Entry(window, width=10, justify="right")
    entry_prichod.grid(row=i + 1, column=1, padx=10)
    entry_prichody_list.append(entry_prichod)

for i in range(dny.pocet(9)):
    entry_odchod = tk.Entry(window, width=10, justify="right")
    entry_odchod.grid(row=i + 1, column=2, padx=10)
    entry_odchody_list.append(entry_odchod)

for i in range(dny.pocet(9)):
    Label_rozdil = tk.Label(window, text="", bg="black", fg="white")
    Label_rozdil.grid(row=i + 1, column=3)
    label_rozdil.append(Label_rozdil)

button_potvrd = tk.Button(window, text="Potvrdit", command=button_click, width=30)
button_potvrd.grid(row=dny.pocet(9) + 1, column=4)

window.mainloop()
