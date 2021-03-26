# Here I have created a gui which will allow you to select an image, customize it and save it
# Author : Shobhit Mishra

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from image_process import image_processor
import cv2 as cv
import os


# this is the main class which will create the gui
class interface:
    # interface constructor demands for the width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.status_var = None
        self.file_name = None
        self.img_slot = None

    # With the start method we will start the making of the gui interface
    def start(self):
        root = Tk()
        root.title("Color changer")  # Setting the title
        root.geometry(f"{self.width}x{self.height}+0+0")  # Setting the width
        root.maxsize(self.width, self.height)
        root.minsize(self.width, self.height)

        # self.status_var is a textvariable for the status bar
        self.status_var = StringVar()
        self.status_var.set("Just select the image and go ahead...")

        pro_status = True

        def button_pressed(e):
            # This binding function will produce the processed image.
            # Also save the image.
            global pro_status

            button = e.widget.cget("text")

            convertor = image_processor.image_convertor(self.file_name)

            if button == 'Gray shade':
                img = convertor.color_to_gray()
                self.img_slot = img
                img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

                img = Image.fromarray(img)

                lb = Label(f3)
                image = ImageTk.PhotoImage(img)
                lb['image'] = image
                lb.image = image
                lb.grid(row=0, column=1)
                pro_status = True

            elif button == 'Red shade':
                img = convertor.color_to_red()
                self.img_slot = img
                img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

                img = Image.fromarray(img)

                lb = Label(f3)
                image = ImageTk.PhotoImage(img)
                lb['image'] = image
                lb.image = image
                lb.grid(row=0, column=1)
                pro_status = True

            elif button == 'Blue shade':
                img = convertor.color_to_blue()
                self.img_slot = img
                img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

                img = Image.fromarray(img)

                lb = Label(f3)
                image = ImageTk.PhotoImage(img)
                lb['image'] = image
                lb.image = image
                lb.grid(row=0, column=1)
                pro_status = True

            elif button == 'Green shade':
                img = convertor.color_to_green()
                self.img_slot = img
                img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

                img = Image.fromarray(img)

                lb = Label(f3)
                image = ImageTk.PhotoImage(img)
                lb['image'] = image
                lb.image = image
                lb.grid(row=0, column=1)
                pro_status = True

            else:
                if pro_status == True:
                    save_filename = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[(
                        "jpg Image", "*.jpg"), ("png Image", "*.png"), ("jpeg Image", "*.jpeg")])
                    convertor.save_image(self.img_slot, save_filename)
        
        gray_button = None
        red_button = None
        blue_button = None
        green_button = None

        lt_button = [gray_button, red_button, blue_button, green_button]
        lt_txt = ['Gray shade', 'Red shade', 'Blue shade', 'Green shade']
        
        def open_file():
            # This function will open the directory
           

            self.file_name = filedialog.askopenfilename(defaultextension=".jpg", filetypes=[("jpg Image", "*.jpg"),
                                                                                            ("png Image", "*.png"), ("jpeg Image", "*.jpeg")])
            print(self.file_name)


            for i in range(4):
                lt_button[i]['state']='normal'

            self.status_var.set(
                f"Image name : {os.path.basename(self.file_name)}")

            img = Image.open(self.file_name)
            img = img.resize((500, 500), Image.ANTIALIAS)

            photo = ImageTk.PhotoImage(img)

            selected_img = Label(f3, borderwidth=2, relief='sunken', bg='gray')
            selected_img['image'] = photo
            selected_img.image = photo
            selected_img.grid(row=0, column=0)

            

        # Creating frame, Labeledframe and inserting a button(file_button)
        f1 = Frame(root)
        f1.pack(side=TOP, fill=X)

        dir = ttk.LabelFrame(f1, text="Select the image")
        dir.pack(side=TOP, fill=X)

        file_button = ttk.Button(dir, text="open files", command=open_file)
        file_button.grid(row=0, column=0)

        # Creating frame, Labeledframe and inserting a buttons(color buttons)
        f2 = Frame(root)
        f2.pack(side=TOP, fill=X)

        controls = ttk.LabelFrame(f2, text="Select the shade")
        controls.pack(side=TOP, fill=X, pady=10)

        root.bind("<Control-s>", button_pressed)


        for i in range(len(lt_button)):
            lt_button[i] = Button(controls, text=lt_txt[i])
            lt_button[i].grid(row=0, column=i)
            lt_button[i]['state']='disabled'
            lt_button[i].bind('<Button-1>', button_pressed)

        # An empty frame where our selected and processed images will appear
        f3 = Frame(root)
        f3.pack(side=TOP, fill=X)

        # The last frame is for the status bar
        f4 = Frame(root)
        f4.pack(side=BOTTOM, fill=X)

        status_bar = Label(f4, textvariable=self.status_var,
                           anchor='w', borderwidth=3, relief='sunken')
        status_bar.pack(side=BOTTOM, fill=X)

        root.mainloop()


if __name__ == "__main__":
    x = interface(1005, 637)
    x.start()
