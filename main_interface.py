from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from image_process import image_processor
import cv2 as cv

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
        
        file_name = None

        def button_pressed(e):
            global file_name

            button = e.widget.cget("text")

            convertor = image_processor.image_convertor(file_name)

            if button=='Gray shade':
                img = convertor.color_to_gray()
                img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
                
                img = Image.fromarray(img)

                lb=Label(f3)
                image = ImageTk.PhotoImage(img)
                lb['image']=image
                lb.image=image
                lb.grid(row=0,column=1)

            elif button=='Red shade':
                pass
            elif button=='Blue shade':
                pass
            elif button=='Green shade':
                pass

        def open_file():
            global file_name
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

        

        button_text = ['Gray shade', 'Red shade', 'Blue shade', 'Green shade']

        j=0
        for i in range(len(button_text)):
            b=Button(controls, text=button_text[i])
            b.grid(row=0, column=i+j)
            j += 1
            b.bind('<Button-1>', button_pressed)

        
        


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