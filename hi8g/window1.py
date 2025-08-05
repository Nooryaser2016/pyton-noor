from tkinter import *

window = Tk()


window.title('Demo Window')
window.geometry('600x300')
l1 =  Label(text="this is my first window" , fg= "red" , bg= "skyblue")
l1.pack()
b1 = Button(text="click me",bg="yellow",foreground="black")
b1.pack()
e1 = Entry(fg="red",bg="yellow",width=10)
e1.pack()
window.mainloop()

