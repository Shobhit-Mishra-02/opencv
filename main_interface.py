from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

class interface:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.status_var = None

    def start(self):
        root = Tk()
        root.geometry(f"{self.width}x{self.height}+0+0")
        self.status_var = StringVar()
        self.status_var.set("Processing...")

        def open_file():
            # print(root.geometry())
            file_name = filedialog.askopenfilename()
            print(file_name)
            img = Image.open(file_name)
            img = img.resize((500,500), Image.ANTIALIAS)

            photo = ImageTk.PhotoImage(img)

            selected_img = Label(f3, borderwidth = 2, relief='sunken', bg='gray')
            selected_img['image']=photo
            selected_img.image=photo
            selected_img.grid(row=0, column=0)

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

        gray_button = ttk.Button(controls , text='Gray shade')
        gray_button.grid(row=0, column=0, pady=3, padx=3)
        
        red_button = ttk.Button(controls , text='Red shade')
        red_button.grid(row=0, column=1, pady=3, padx=3)
        
        blue_button = ttk.Button(controls , text='Blue shade')
        blue_button.grid(row=0, column=2, pady=3, padx=3)
        
        green_button = ttk.Button(controls , text='Green shade')
        green_button.grid(row=0, column=3, pady=3, padx=3)
        
        # gray_button = ttk.Button(controls , text='Gray shade')
        # gray_button.grid(row=0, column=0, pady=3, padx=3)

        ttk.Button.bind('<>')

        f3 = Frame(root)
        f3.pack(side=TOP, fill=X)
        
        
        
        # processed_img = Label(f3, borderwidth = 2, relief='sunken', bg='gray', width=60,height=30)
        # processed_img.grid(row=0, column=1)

        # save_button = Button(f3, text="Save the image", borderwidth=3, relief='raised')
        # save_button.grid(row=1, column=1, sticky=['news'], pady=4)

        
        
        f4 = Frame(root)
        f4.pack(side=BOTTOM, fill=X)

        status_bar = Label(f4, textvariable=self.status_var, anchor='w', borderwidth=3, relief='sunken')
        status_bar.pack(side=BOTTOM, fill=X)




        root.mainloop()

if __name__=="__main__":
    x=interface(852,637)
    x.start()