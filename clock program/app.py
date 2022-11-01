from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)


window = Tk()

time_label = Label(window,font=("bold",50),fg="black",bg="#911797")
time_label.pack()

day_label = Label(window,font=("bold",25,"bold"),bg="#911797")
day_label.pack()

date_label = Label(window,font=("bold",30),bg="#911797")
date_label.pack()

update()

window.mainloop()