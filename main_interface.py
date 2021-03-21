from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import os
from Image import image_window

class main_interface:
    def __init__(self, width, height):
        self.width=width
        self.height = height
        self.status_var=None
        # self.filename=None

    def win_development(self):
        root = Tk()
        root.geometry(f"{self.width}x{self.height}+0+0")
        root.title("COLOR CHANGER")
        
        self.status_var=StringVar()
        self.status_var.set('Select the image and goahead.....')

        filename=None


        
        def selection_image():
            # print(root.geometry())
            global filename
            filename = filedialog.askopenfilename()
            # print(filename)
            img = Image.open(filename)
            img = img.resize((555, 441), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)

            panel = Label(f3, image=photo)
            panel.image=photo
            panel.grid(row=0, column=0)

            self.status_var.set(f"(original) Image Name: {os.path.basename(filename)}")

            # start_button['state']='!disabled'

        def blue():
            global filename
            x=image_window.ImageInterface(filename)
            x.show_blue()

        def green():
            global filename
            x=image_window.ImageInterface(filename)
            x.show_green()

        def red():
            global filename
            x=image_window.ImageInterface(filename)
            x.show_red()


        f1=Frame(root)
        f1.pack(side=TOP, fill=X)

        # controll frame
        control_frame=ttk.LabelFrame(f1, text="Control panel")
        control_frame.pack(fill=X)

        # buttons in controll frame
        # start_button = ttk.Button(control_frame, text="START", command=start)
        # start_button.grid(row=0, column=0)
        # start_button['state'] = 'disabled'
        selection_button = ttk.Button(control_frame, text="Select image", command=selection_image)
        selection_button.grid(row=0, column=1)
        
        # separate frame for the color changers 
        f2 = Frame(root)
        f2.pack(side=TOP, fill=X)

        lb_color=ttk.LabelFrame(f2, text="Select the color shade")
        lb_color.pack(side=TOP, fill=X)

        Button_blue = ttk.Button(lb_color, text="Blue", command=blue)
        Button_blue.grid(row=0, column=0)
        
        Button_red = ttk.Button(lb_color, text="Red", command=red)
        Button_red.grid(row=0, column=1)

        Button_green = ttk.Button(lb_color, text="Green", command=green)
        Button_green.grid(row=0, column=2)

        f3=Frame(root)
        f3.pack(side= TOP, fill=X)


        
        f4=Frame(root, borderwidth=3, relief='raised')
        f4.pack(side=BOTTOM, fill=X)

        status_bar = Label(f4, textvariable=self.status_var, anchor='w')
        status_bar.pack(side=BOTTOM, fill=X)

        root.mainloop()

if __name__=="__main__":
    x=main_interface(555,656)
    x.win_development()