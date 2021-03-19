from tkinter import *
from tkinter import ttk

class main_interface:
    def __init__(self, width, height):
        self.width=width
        self.height = height
        self.status_var=None

    def win_development(self):
        root = Tk()
        root.geometry(f"{self.width}x{self.height}")
        root.title("COLOR CHANGER")
        
        self.status_var=StringVar()
        self.status_var.set('Test')

        def start():
            pass
        def selection_image():
            pass
        def storage_dir():
            pass



        f1=Frame(root)
        f1.pack(side=TOP, fill=X)

        control_frame=ttk.LabelFrame(f1, text="Control panel")
        control_frame.pack(fill=X)

        start_button = ttk.Button(control_frame, text="START", command=start)
        start_button.grid(row=0, column=0)
        selection_button = ttk.Button(control_frame, text="Select image", command=selection_image)
        selection_button.grid(row=0, column=1)
        dir_button = ttk.Button(control_frame, text="Select the storage location", command=storage_dir)
        dir_button.grid(row=0, column=2)

        f2 = Frame(root)
        f2.pack(side=TOP, fill=X)

        Label(f2, text='Change the shade of red').pack(anchor='w')
        red = ttk.Scale(f2, from_=0, to=255, orient=HORIZONTAL)
        red.pack(fill=X)
        
        Label(f2, text='Change the shade of blue').pack(anchor='w')
        blue = Scale(f2, from_=0, to=255, orient=HORIZONTAL, tickinterval=20)
        blue.pack(fill=X)
        
        Label(f2, text='Change the shade of green').pack(anchor='w')
        green = Scale(f2, from_=0, to=255, orient=HORIZONTAL, tickinterval=20)
        green.pack(fill=X)

        f3=Frame(root)
        f3.pack(side= TOP, fill=X)

        f4=Frame(root, borderwidth=3, relief='raised')
        f4.pack(side=BOTTOM, fill=X)

        status_bar = Label(f4, textvariable=self.status_var, anchor='w')
        status_bar.pack(side=BOTTOM, fill=X)

        root.mainloop()

if __name__=="__main__":
    x=main_interface(900,400)
    x.win_development()