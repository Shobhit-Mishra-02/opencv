'''
Author: Shobhit Mishra

So here I have created the sole of the GUI, in the main interface I was dealing with 
apperance and user experiance. But in this file I have added the functions which will perform
the required operations on the image and return the processed image as the output. 
'''

import cv2 as cv
import numpy as np

class image_convertor:
    '''
    This class holds some methods which will convert image from colored to gray, red, blue
    and green. Basically this will just change the background shade of the image.
    '''
    
    # This constructor demands for the filename, which is the location of the selected image.
    def __init__(self, filename):
        self.filename = filename
        self.result = None
        self.color_processed = None

    # This method will convert the selected image into the gray shaded image.
    def color_to_gray(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (457, 587))
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.result = img
        self.color_processed = True
        return self.result

    # This method will convert the selected image into the red shaded image.
    def color_to_red(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (457, 587))
        img[:,:,2] = 115
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.result = img
        self.color_processed = True
        return self.result

    # This method will convert the image into the blue shaded image.
    def color_to_blue(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (457, 587))

        img[:,:,0] = 115
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.result = img
        self.color_processed = True
        return self.result
    
    # This method will convert the image into the green shaded image.
    def color_to_green(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (457, 587))

        img[:,:,1] = 115
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.result = img
        self.color_processed = True
        return self.result

    # This method will just show the selected image.
    # But I have not used this one in the main interface 
    # because with this we can just do some error findings if required.
    def show(self):
        cv.imshow('frame', self.result)
        cv.waitKey(0)


class change_contrast:
    '''
    This class holds a method which will edit the contrast.
    '''
    def __init__(self):
        pass
    
    # This method will edit the image contrast if the loaded image is given.
    def loaded_image_contrast(self,percentage_of_contrast, loaded_image):
        img = loaded_image
        img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
        
        l, a, b = cv.split(lab)
        clahe = cv.createCLAHE(clipLimit=(percentage_of_contrast/100), tileGridSize=(8,8))
        cl = clahe.apply(l)
        limg = cv.merge((cl,a,b))
        final = cv.cvtColor(limg, cv.COLOR_LAB2BGR)
        final = cv.resize(final,(457, 587))
        final = cv.cvtColor(final, cv.COLOR_BGR2RGB)
        self.result = final
        return self.result

    # This method will edit the image contrast if the location of the image is given.
    def image_contrast(self, percentage_of_contrast, image_location):
        img = cv.imread(image_location)
        lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
        
        l, a, b = cv.split(lab)
        clahe = cv.createCLAHE(clipLimit=(percentage_of_contrast/100), tileGridSize=(8,8))
        cl = clahe.apply(l)
        limg = cv.merge((cl,a,b))
        final = cv.cvtColor(limg, cv.COLOR_LAB2BGR)
        final = cv.resize(final,(457, 587))
        final = cv.cvtColor(final, cv.COLOR_BGR2RGB)
        self.result = final
        return self.result


class save_file:
    '''
    This class holds a method which save the processed image.
    '''

    # This constructor demands for the location of the image where you want to save the image,
    # the image which you want to save, width and height of the image.
    def __init__(self,image, location, width, height):
        self.image = image
        self.location = location
        self.width = width
        self.height = height

    # This method will save the image.
    def save_image(self):
        img = cv.resize(self.image, (self.width, self.height))
        img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        cv.imwrite(f"{self.location}", img)

class Merging_images:
    '''
    This class will holds a method which merges the two images according to the image dominance
    which you have selected.
    '''

    # This constructor demands for two images which you want to be merged.
    def __init__(self, first_image, second_image):
        self.first_image = first_image
        self.second_image = second_image
    
    # This method will merge the two images and also demands for the percentage of the dominance.
    def merging_action(self, percentage_dominance):
        img1 = cv.imread(self.first_image)
        img1 = cv.resize(img1,(457, 587))

        img2 = cv.imread(self.second_image)
        img2 = cv.resize(img2,(457, 587))

        output = cv.addWeighted(img1,percentage_dominance/100, img2, (100-percentage_dominance)/100, 0)
        output = cv.cvtColor(output, cv.COLOR_BGR2RGB)
        return output

class adv_coloring:
    '''
    This class will holds a method which will edit the two selected colors in the image 
    and it will change the background of the image according to that.
    '''

    # This constructor demand for two colors and their corresponding percentage of the colors. 
    def __init__(self,filename, color1, color2, color_rate1, color_rate2):
        self.filename = filename
        self.color1 = color1
        self.color2 = color2

        self.color_rate1 = color_rate1 
        self.color_rate2 = color_rate2 

        self.result = None
        
        self.img = cv.imread(self.filename)
        self.img = cv.resize(self.img, (457, 587))

    # This method will produce the processed image.
    def color_action(self):
        
        if self.color1 == 'Red':
            self.img[:,:,2] = self.color_rate1
        if self.color1 == 'Blue':
            self.img[:,:,0] = self.color_rate1
        if self.color1 == 'Green':
            self.img[:,:,1] = self.color_rate1
              
        if self.color2 == 'Red':
            self.img[:,:,2] = self.color_rate2
        if self.color2 == 'Blue':
            self.img[:,:,0] = self.color_rate2
        if self.color2 == 'Green':
            self.img[:,:,1] = self.color_rate2
        
        
        self.img = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)
        return self.img
        