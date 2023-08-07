import random
import tkinter as tk
from tkinter.ttk import *

root = tk.Tk()
root.title("Random Password Generator")

def generate():
    entry.delete(0, tk.END)
    try:
        length = int(entry1.get())
    except ValueError:
        entry.insert(0, "Invalid length")
        return

    if length <= 0:
        entry.insert(0, "Invalid length")
        return

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    password = "".join(random.choice(digits) for _ in range(length))
    entry.insert(0, password)

txt = Label(root, text="Generate your Password")
txt.grid(row=0, column=1)

Random_password = Label(root, text="Password")
Random_password.grid(row=1)

entry = Entry(root)
entry.grid(row=1, column=1)

label = Label(root, text="Length")
label.grid(row=2)

button = Button(root, text="Generate", command=generate)
button.grid(row=6, column=1)

entry1 = Entry(root)
entry1.grid(column=1, row=2)

root.mainloop()
