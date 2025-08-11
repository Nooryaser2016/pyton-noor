import random
import string
import tkinter as tk

def generate():
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
    label.config(text=password)

root = tk.Tk()
tk.Button(root, text="Generate", command=generate).pack()
label = tk.Label(root, font=14)
label.pack()
root.mainloop()