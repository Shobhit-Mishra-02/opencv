'''
Author: Shobhit Mishra

Here in the main interface and here I have developed the appearance of the GUI.
'''

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as msg
from PIL import Image, ImageTk
from image_process import image_processor
import numpy as np
import os
import numpy as np



class main_interace:
    '''
    In this class I have added two methods,
    the first one is start_creation which starts the creation of the GUI and 
    the second one is end_statement which completes the GUI. 
    '''

    # This constructor demands for the width and height of the GUI.
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        
        self.contrast_rate = IntVar()
        self.merge_img1 = None
        self.merge_img2 = None
        self.merge_percentage = IntVar()
        self.var_width = IntVar()
        self.var_height = IntVar()

        self.var_height.set(500)
        self.var_width.set(500)

        self.combo_color1 = StringVar()
        self.combo_color2 = StringVar()

        self.color_rate1 = IntVar()
        self.color_rate2 = IntVar()

        self.status_var = StringVar()

    # This method holds all those widgets which will appear in the GUI screen.
    def start_creation(self):
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        self.root.maxsize(self.width, self.height)
        self.root.minsize(self.width, self.height)
        self.root.title('Photo color enhancer')

    
    # This is the ending statement whcih will end the mainloop.
    def end_statement(self):
        self.root.mainloop()

if __name__=="__main__":
    win = main_interace(973,660)
    win.start_creation()
    win.end_statement()