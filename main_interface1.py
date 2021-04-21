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

        self.filename = None
        self.slot_image = None
        self.processed_image = None
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
        self.status_var.set(
            'Select the file option, open a image and go ahead .....')
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        self.root.maxsize(self.width, self.height)
        self.root.minsize(self.width, self.height)
        self.root.title('Photo color enhancer')

        def output_image_inserter(img):
            img = Image.fromarray(img)

            image = ImageTk.PhotoImage(img)
            self.slot_image['image'] = image
            self.slot_image.image = image
            self.slot_image.grid(row=1, column=0, rowspan=4)
        
        def submit_adv_color():
            if self.combo_color1.get() != self.combo_color2.get():
                color1_scale['state'] = 'normal'
                color1_scale['label'] = f'First color: {self.combo_color1.get()}'
                color2_scale['state'] = 'normal'
                color2_scale['label'] = f'Second color: {self.combo_color2.get()}'
                button_rbg['state'] = 'normal'
            else:
                msg.showerror("Error",'You have to select two different colors.')
        
        def button_pressed(e):
            pro = image_processor.image_convertor(self.filename)

            if e.widget.cget('text') == 'Gray shade':
                img = pro.color_to_gray()
                self.processed_image = img
                output_image_inserter(img)
                processed_image_in = True

            elif e.widget.cget('text') == 'Red shade':
                img = pro.color_to_red()
                self.processed_image = img
                output_image_inserter(img)
                processed_image_in = True

            elif e.widget.cget('text') == 'Blue shade':
                img = pro.color_to_blue()
                self.processed_image = img
                output_image_inserter(img)
                processed_image_in = True

            elif e.widget.cget('text') == 'Green shade':
                img = pro.color_to_green()
                self.processed_image = img
                output_image_inserter(img)
                processed_image_in = True

            elif e.widget.cget('text') == 'Apply contrast':
                contrast_converter = image_processor.change_contrast()
                if type(self.processed_image) == np.ndarray:
                    img = contrast_converter.loaded_image_contrast(
                        percentage_of_contrast=self.contrast_rate.get(), loaded_image=self.processed_image)
                    self.processed_image = img
                    output_image_inserter(img)
                else:
                    img = contrast_converter.image_contrast(
                        percentage_of_contrast=self.contrast_rate.get(), image_location=self.filename)
                    self.processed_image = img
                    output_image_inserter(img)

            elif e.widget.cget('text') == 'Apply color':
                rbg = image_processor.adv_coloring(self.filename, color1=self.combo_color1.get(), color2=self.combo_color2.get(), color_rate1=self.color_rate1.get(), color_rate2=self.color_rate2.get())
                img = rbg.color_action()
                self.processed_image = img
                output_image_inserter(img)

            elif e.widget.cget('text') == 'Apply merging':
                if self.merge_img1 != None and self.merge_img2 != None and self.merge_percentage.get() != 0:
                    merge = image_processor.Merging_images(self.merge_img1, self.merge_img2)
                    img = merge.merging_action(percentage_dominance=self.merge_percentage.get())
                    self.processed_image = img
                    output_image_inserter(img)
                else:
                    msg.showerror('Error', 'First select both the images , then select the percentage dominance and then press the Apply merging button')

            elif e.widget.cget('text') == 'Apply changes':
                print(var_width.get())
                control_size.state(['disabled'])
                image_height['state'] = 'disabled'
                image_width['state'] = 'disabled'
                size_apply['state'] = 'disabled'
                
        def merge_event(e):
            if e.widget.cget('text') == 'Select first image':
                self.merge_img1 = filedialog.askopenfilename()
            elif e.widget.cget('text') == 'Select second image':
                self.merge_img2 = filedialog.askopenfilename()
        
        def openfile():
            self.filename = filedialog.askopenfilename()

            img = Image.open(self.filename)
            img = img.resize((457, 587), Image.ANTIALIAS)

            photo = ImageTk.PhotoImage(img)

            self.slot_image['width'] = 0
            self.slot_image['height'] = 0
            self.slot_image['image'] = photo
            self.slot_image.image = photo
            self.slot_image.grid(row=1, column=0, rowspan=4)
            self.status_var.set(f"Image name: {os.path.basename(self.filename)}")
            for i in lt_button:
                i['state'] = 'normal'

        def savefile():
            pass
            if type(self.processed_image) == np.ndarray:
                location = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[(
                    "jpg Image", "*.jpg"), ("png Image", "*.png"), ("jpeg Image", "*.jpeg")])
                file_saver = image_processor.save_file(
                    image=self.processed_image, location=location, width=var_width.get(), height=var_height.get())
                file_saver.save_image()
            else:
                msg.showerror(
                    'Error', 'First select the image from the open file option.')

        def Exit():
            self.root.destroy()

        def contrast():
            if self.filename != None:

                if control_merging.instate(['disabled']) == False:
                    control_merging.state(['disabled'])
                    button_img1['state'] = 'disabled'
                    button_img2['state'] = 'disabled'
                    button_merg['state'] = 'disabled'
                    dominance_scale['state'] = 'disabled'

                if control_rbg.instate(['disabled']) == False:
                    control_rbg.state(['disabled'])
                    first_color['state'] = 'disabled'
                    second_color['state'] = 'disabled'
                    button_color['state'] = 'disabled'
                    color1_scale['state'] = 'disabled'
                    color2_scale['state'] = 'disabled'
                    button_rbg['state'] = 'disabled'

                if control_size.instate(['disabled']) == False:
                    control_size.state(['disabled'])
                    image_height['state'] = 'disabled'
                    image_width['state'] = 'disabled'
                    size_apply['state'] = 'disabled'

                for i in lt_button:
                    i['state'] = 'disabled'
                
                control_contrast.state(['!disabled'])
                contrast_scale['state'] = 'normal'
                button_contrast['state'] = 'normal'
            else:
                msg.showerror(
                    'Error', 'First select the image from the openfile option from the file submenu.')

        def rbg():
            if self.filename != None:

                if control_merging.instate(['disabled']) == False:
                    control_merging.state(['disabled'])
                    button_img1['state'] = 'disabled'
                    button_img2['state'] = 'disabled'
                    button_merg['state'] = 'disabled'
                    dominance_scale['state'] = 'disabled'

                if control_contrast.instate(['disabled']) == False:
                    control_contrast.state(['disabled'])
                    contrast_scale['state'] = 'disabled'
                    button_contrast['state'] = 'disabled'

                if control_size.instate(['disabled']) == False:
                    control_size.state(['disabled'])
                    image_height['state'] = 'disabled'
                    image_width['state'] = 'disabled'
                    size_apply['state'] = 'disabled'

                for i in lt_button:
                    i['state'] = 'disabled'

                control_rbg.state(['!disabled'])
                first_color['state'] = 'normal'
                second_color['state'] = 'normal'
                button_color['state'] = 'normal'
            else:
                msg.showerror(
                    'Error', 'First select the image from the openfile option from the file submenu.')

        def merging_effect():
            if self.filename != None:

                if control_rbg.instate(['disabled']) == False:
                    control_rbg.state(['!disabled'])
                    first_color['state'] = 'disabled'
                    second_color['state'] = 'disabled'
                    button_color['state'] = 'disabled'
                    color1_scale['state'] = 'disabled'
                    color2_scale['state'] = 'disabled'
                    button_rbg['state'] = 'disabled'

                if control_contrast.instate(['disabled']) == False:
                    control_contrast.state(['disabled'])
                    contrast_scale['state'] = 'disabled'
                    button_contrast['state'] = 'disabled'

                if control_size.instate(['disabled']) == False:
                    control_size.state(['disabled'])
                    image_height['state'] = 'disabled'
                    image_width['state'] = 'disabled'
                    size_apply['state'] = 'disabled'

                for i in lt_button:
                    i['state'] = 'disabled'

                control_merging.state(['!disabled'])
                button_img1['state'] = 'normal'
                button_img2['state'] = 'normal'
                button_merg['state'] = 'normal'
                dominance_scale['state'] = 'normal'
            else:
                msg.showerror(
                    'Error', 'First select the image from the openfile option from the file submenu.')

        def size_change():
            if self.filename != None:

                if control_rbg.instate(['disabled']) == False:
                    control_rbg.state(['!disabled'])
                    first_color['state'] = 'disabled'
                    second_color['state'] = 'disabled'
                    button_color['state'] = 'disabled'
                    color1_scale['state'] = 'disabled'
                    color2_scale['state'] = 'disabled'
                    button_rbg['state'] = 'disabled'

                if control_contrast.instate(['disabled']) == False:
                    control_contrast.state(['disabled'])
                    contrast_scale['state'] = 'disabled'
                    button_contrast['state'] = 'disabled'

                if control_merging.instate(['disabled']) == False:
                    control_merging.state(['disabled'])
                    button_img1['state'] = 'disabled'
                    button_img2['state'] = 'disabled'
                    button_merg['state'] = 'disabled'
                    dominance_scale['state'] = 'disabled'


                for i in lt_button:
                    i['state'] = 'disabled'

                control_size.state(['!disabled'])
                image_height['state'] = 'normal'
                image_width['state'] = 'normal'
                size_apply['state'] = 'normal'
            else:
                msg.showerror(
                    'Error', 'First select the image from the openfile option from the file submenu.')

        def simple_shade():
            if self.filename != None:
                if control_rbg.instate(['disabled']) == False:
                    control_rbg.state(['!disabled'])
                    first_color['state'] = 'disabled'
                    second_color['state'] = 'disabled'
                    button_color['state'] = 'disabled'
                    color1_scale['state'] = 'disabled'
                    color2_scale['state'] = 'disabled'
                    button_rbg['state'] = 'disabled'
            
                if control_merging.instate(['disabled']) == False:
                    control_merging.state(['disabled'])
                    button_img1['state'] = 'disabled'
                    button_img2['state'] = 'disabled'
                    button_merg['state'] = 'disabled'
                    dominance_scale['state'] = 'disabled'
            
                if control_contrast.instate(['disabled']) == False:
                    control_contrast.state(['disabled'])
                    contrast_scale['state'] = 'disabled'
                    button_contrast['state'] = 'disabled'

                if control_size.instate(['disabled']) == False:
                    control_size.state(['disabled'])
                    image_height['state'] = 'disabled'
                    image_width['state'] = 'disabled'
                    size_apply['state'] = 'disabled'

            for i in lt_button:
                i['state'] = 'normal'

        def about():
            msg.showinfo('About application', 'This is an application which will allow you to do editing in the image color, size and also there is a unique feature of merging two images.')

        # Here I have started the development of the menu of the main interface.
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        # This function will add the submenues in the menubar.
        def func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu):
            m = Menu(menubar, tearoff=0)
            for i in range(len(menu_lb)):
                m.add_command(label=menu_lb[i], command=menu_command[i])
            menubar.add_cascade(label=nameofsubmenu, menu=m)

        menu_lb = ["Open image", "save as", "Exit"]
        menu_command = [openfile, savefile, Exit]
        nameofsubmenu = "File"
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)

        menu_lb = ['Edit Contrast', 'Edit RBG',
                   'Meging effect', 'Change size', 'Simple shades']
        menu_command = [contrast, rbg,
                        merging_effect, size_change, simple_shade]
        nameofsubmenu = "customization"
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)

        menu_lb = ['About application']
        menu_command = [about]
        nameofsubmenu = 'About'
        func_for_submenu(menubar, menu_lb, menu_command, nameofsubmenu)


        control_frame = ttk.LabelFrame(self.root, text='Color controls')
        control_frame.grid(row=0, column=0, columnspan=2, sticky=['n', 'e', 'w', 's'])

        # empty variables for the buttons in the control frame
        gray_button = None
        red_button = None
        blue_button = None
        green_button = None


        lt_button = [gray_button, red_button,
                    blue_button, green_button]
        lt_txt = ['Gray shade', 'Red shade',
                'Blue shade', 'Green shade', ]
        for i in range(len(lt_button)):
            lt_button[i] = ttk.Button(control_frame, text=lt_txt[i])
            lt_button[i].grid(row=0, column=i)
            lt_button[i]['state'] = 'disabled'
            lt_button[i].bind('<Button-1>', button_pressed)

    
        # placing a temp label where the image would be placed
        self.slot_image = Label(self.root, borderwidth=3,
                        relief='sunken', width=65, height=39, bg = 'gray70')
        self.slot_image.grid(row=1, column=0, rowspan=4)


        # labeled frame for the contrast
        control_contrast = ttk.LabelFrame(self.root, text='Controling contrast')
        control_contrast.grid(row=1, column=1, sticky=['n'])
        control_contrast.state(['disabled'])

        # labled frame for the merging effects
        control_merging = ttk.LabelFrame(self.root, text='Merging the images')
        control_merging.grid(row=2, column=1, sticky=['n', 'e', 'w'])
        control_merging.state(['disabled'])

        # label frame for the selection of the rbg colors
        control_rbg = ttk.LabelFrame(self.root, text='Advanced color controls')
        control_rbg.grid(row=3, column=1, sticky=['n', 'e', 'w'])
        control_rbg.state(['disabled'])

        # label for selecting the size of the saved image
        control_size = ttk.LabelFrame(self.root, text='Sizing controls')
        control_size.grid(row=4, column=1, sticky=['n', 'e', 'w'])
        control_size.state(['disabled'])


        # placing a scale and button in the contrast frame
        contrast_scale = Scale(control_contrast, from_=0, to=100, tickinterval=10,
                            orient=HORIZONTAL, length=500, variable=self.contrast_rate)
        contrast_scale.pack(fill=X, side=TOP)
        contrast_scale['state'] = 'disabled'

        button_contrast = ttk.Button(control_contrast, text='Apply contrast')
        button_contrast.pack(pady=8)
        button_contrast.bind('<Button-1>', button_pressed)
        button_contrast['state'] = 'disabled'

        # placing three buttons in the merging frame
        button_img1 = ttk.Button(control_merging, text='Select first image')
        button_img1.grid(row=0, column=0, padx=10, pady=12)
        button_img1.bind('<Button-1>', merge_event)

        button_img2 = ttk.Button(control_merging, text='Select second image')
        button_img2.grid(row=0, column=1, pady=12)
        button_img2.bind('<Button-1>', merge_event)

        button_merg = ttk.Button(control_merging, text='Apply merging')
        button_merg.grid(row=0, column=2, padx=50, pady=12)
        button_merg.bind('<Button-1>', button_pressed)

        dominance_scale = Scale(control_merging, variable=self.merge_percentage, label='Select the dominance wrt first image',
                                orient=HORIZONTAL, length=500, from_=0, to=100, tickinterval=10)
        dominance_scale.grid(row=1, column=0, columnspan=3)


        button_img1['state'] = 'disabled'
        button_img2['state'] = 'disabled'
        button_merg['state'] = 'disabled'
        dominance_scale['state'] = 'disabled'

        # placing two combobox and two scales in the rbg frame and buttons also
        first_color = ttk.Combobox(control_rbg, values=['Red', 'Blue', 'Green'], textvariable = self.combo_color1)
        first_color.grid(row=0, column=0, padx=10, pady=8)

        second_color = ttk.Combobox(control_rbg, values=['Red', 'Blue', 'Green'], textvariable = self.combo_color2)
        second_color.grid(row=0, column=1, pady=8)

        button_color = ttk.Button(control_rbg, text='Submit', command=submit_adv_color)
        button_color.grid(row=0, column=2, padx=40, pady=8)


        color1_scale = Scale(control_rbg, from_=0, to=255, tickinterval=50,label = 'First color:',
                            orient=HORIZONTAL, length=500,variable = self.color_rate1)
        color1_scale.grid(row=2, column=0, columnspan=3)



        color2_scale = Scale(control_rbg, from_=0, to=255, tickinterval=50,label ='Second color:',
                            orient=HORIZONTAL, length=500 ,variable = self.color_rate2)
        color2_scale.grid(row=3, column=0, columnspan=3)

        button_rbg = ttk.Button(control_rbg, text='Apply color')
        button_rbg.grid(row=5, column=0, columnspan=3, pady=8)
        button_rbg.bind('<Button-1>', button_pressed)

        first_color['state'] = 'disabled'
        second_color['state'] = 'disabled'
        button_color['state'] = 'disabled'
        color1_scale['state'] = 'disabled'
        color2_scale['state'] = 'disabled'
        button_rbg['state'] = 'disabled'

        # placing two entry widgets in the sizing frame
        Label(control_size, text = 'Width').grid(row=0, column=0)
        image_width = ttk.Entry(control_size, textvariable=self.var_width)
        image_width.grid(row=0, column=1, pady=8)

        Label(control_size, text = 'Height').grid(row=0, column=2)
        image_height = ttk.Entry(control_size, textvariable=self.var_height)
        image_height.grid(row=0, column=3, pady=8)

        size_apply = ttk.Button(control_size, text='Apply changes')
        size_apply.grid(row=0, column=4, padx=25, pady=8)
        size_apply.bind('<Button-1>', button_pressed)

        image_height['state'] = 'disabled'
        image_width['state'] = 'disabled'
        size_apply['state'] = 'disabled'

        status_bar = Label(self.root,anchor='w', borderwidth=3, relief='raised', textvariable = self.status_var, font='helvertica 10 bold')
        status_bar.grid(row=6, column=0, columnspan=2, sticky=['n', 'e', 'w', 's'])


    # This is the ending statement whcih will end the mainloop.
    def end_statement(self):
        self.root.mainloop()


if __name__ == "__main__":
    win = main_interace(973, 660)
    win.start_creation()
    win.end_statement()
