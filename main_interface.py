from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from image_process import image_processor
import cv2 as cv
import os


class interface:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.status_var = None
        self.file_name = None
        self.button_lt = []

    def start(self):
        root = Tk()
        root.title("Color changer")
        root.geometry(f"{self.width}x{self.height}+0+0")
        self.status_var = StringVar()
        self.status_var.set("Just select the image and go ahead...")

        self.file_name = None

        def button_pressed(e):
            # global self.file_name

            button = e.widget.cget("text")

            convertor = image_processor.image_convertor(self.file_name)

            if button == 'Gray shade':
                img = convertor.color_to_gray()
                img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

                img = Image.fromarray(img)

                lb = Label(f3)
                image = ImageTk.PhotoImage(img)
                lb['image'] = image
                lb.image = image
                lb.grid(row=0, column=1)

            elif button == 'Red shade':
                img = convertor.color_to_red()
                img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

                img = Image.fromarray(img)

                lb = Label(f3)
                image = ImageTk.PhotoImage(img)
                lb['image'] = image
                lb.image = image
                lb.grid(row=0, column=1)
                
            elif button == 'Blue shade':
                img = convertor.color_to_blue()
                img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

                img = Image.fromarray(img)

                lb = Label(f3)
                image = ImageTk.PhotoImage(img)
                lb['image'] = image
                lb.image = image
                lb.grid(row=0, column=1)

            elif button == 'Green shade':
                img = convertor.color_to_green()
                img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

                img = Image.fromarray(img)

                lb = Label(f3)
                image = ImageTk.PhotoImage(img)
                lb['image'] = image
                lb.image = image
                lb.grid(row=0, column=1)

        def open_file():
            # global self.file_name

            print(root.geometry())
            self.file_name = filedialog.askopenfilename()
            print(self.file_name)

            gray_button['state'] = 'normal'
            green_button['state'] = 'normal'
            red_button['state'] = 'normal'
            blue_button['state'] = 'normal'

            self.status_var.set(f"Image name : {os.path.basename(self.file_name)}")

            img = Image.open(self.file_name)
            img = img.resize((500, 500), Image.ANTIALIAS)

            photo = ImageTk.PhotoImage(img)

            selected_img = Label(f3, borderwidth=2, relief='sunken', bg='gray')
            selected_img['image'] = photo
            selected_img.image = photo
            selected_img.grid(row=0, column=0)

            for i in range(len(self.button_lt)):
                self.button_lt[i]['state'] = '!disable'

        f1 = Frame(root)
        f1.pack(side=TOP, fill=X)

        dir = ttk.LabelFrame(f1, text="Select the image")
        dir.pack(side=TOP, fill=X)

        file_button = ttk.Button(dir, text="open files", command=open_file)
        file_button.grid(row=0, column=0)

        f2 = Frame(root)
        f2.pack(side=TOP, fill=X)

        controls = ttk.LabelFrame(f2, text="Select the shade")
        controls.pack(side=TOP, fill=X, pady=10)

        button_text = ['Gray shade', 'Red shade', 'Blue shade', 'Green shade']

        # j=0
        # for i in range(len(button_text)):
        #     self.button_lt.append(i)

        #     self.button_lt[i]=Button(controls, text=button_text[i])
        #     self.button_lt[i].grid(row=0, column=i+j)

        #     j += 1

        #     self.button_lt[i].bind('<Button-1>', button_pressed)
        #     self.button_lt[i]['state']='disable'

        gray_button = Button(controls, text='Gray shade')
        gray_button['state'] = 'disabled'
        gray_button.grid(row=0, column=0)

        red_button = Button(controls, text='Red shade')
        red_button['state'] = 'disabled'
        red_button.grid(row=0, column=1)

        blue_button = Button(controls, text='Blue shade')
        blue_button['state'] = 'disabled'
        blue_button.grid(row=0, column=2)

        green_button = Button(controls, text='Green shade')
        green_button['state'] = 'disabled'
        green_button.grid(row=0, column=3)

        gray_button.bind('<Button-1>', button_pressed)
        red_button.bind('<Button-1>', button_pressed)
        blue_button.bind('<Button-1>', button_pressed)
        green_button.bind('<Button-1>', button_pressed)

        f3 = Frame(root)
        f3.pack(side=TOP, fill=X)

        # processed_img = Label(f3, borderwidth = 2, relief='sunken', bg='gray', width=60,height=30)
        # processed_img.grid(row=0, column=1)

        # save_button = Button(f3, text="Save the image", borderwidth=3, relief='raised')
        # save_button.grid(row=1, column=1, sticky=['news'], pady=4)

        f4 = Frame(root)
        f4.pack(side=BOTTOM, fill=X)

        status_bar = Label(f4, textvariable=self.status_var,
                           anchor='w', borderwidth=3, relief='sunken')
        status_bar.pack(side=BOTTOM, fill=X)

        root.mainloop()


if __name__ == "__main__":
    x = interface(1005, 637)
    x.start()
