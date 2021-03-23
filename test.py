from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import cv2 as cv
from PIL import Image, ImageTk


root = Tk()

img = cv.imread('image_1.jpg')
img = cv.resize(img, (500,500) )
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

img = Image.fromarray(img)


lb=Label(root)
lb.pack()

image = ImageTk.PhotoImage(img)
lb['image']=image


root.mainloop()