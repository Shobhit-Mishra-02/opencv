import numpy as np
from tkinter import *
from tkinter import filedialog

root =Tk()
root.geometry('500x500')

def pro():
    location = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[(
        "jpg Image", "*.jpg"), ("png Image", "*.png"), ("jpeg Image", "*.jpeg")])
    print(location)

Button(root, text = 'press me', command = pro).pack()


root.mainloop()
