from tkinter import *
from  PIL import Image , ImageTk
root = Tk()
root.title("MY PICTURE")
root.geometry('500x500')
pic1 = Image.open('Siamese_kitten.webp')#
image = ImageTk.PhotoImage(pic1)
label = Label(root, image=image)

label.pack()
root.mainloop()

