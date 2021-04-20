import cv2 as cv
import numpy as np

class image_convertor:
    def __init__(self, filename):
        self.filename = filename
        self.result = None
        self.color_processed = None

    def color_to_gray(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (457, 569))
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.result = img
        self.color_processed = True
        return self.result

    def color_to_red(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (457, 569))
        img[:,:,2] = 115
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.result = img
        self.color_processed = True
        return self.result

    def color_to_blue(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (457, 569))

        img[:,:,0] = 115
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.result = img
        self.color_processed = True
        return self.result
    
    def color_to_green(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (457, 569))

        img[:,:,1] = 115
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.result = img
        self.color_processed = True
        return self.result
    
    

    def show(self):
        cv.imshow('frame', self.result)
        cv.waitKey(0)

class change_contrast:
    def __init__(self):
        # self.image_location = image_location
        # self.loaded_image = loaded_image
        pass

    def loaded_image_contrast(self,percentage_of_contrast, loaded_image):
        img = loaded_image
        img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
        
        l, a, b = cv.split(lab)
        clahe = cv.createCLAHE(clipLimit=(percentage_of_contrast/100), tileGridSize=(8,8))
        cl = clahe.apply(l)
        limg = cv.merge((cl,a,b))
        final = cv.cvtColor(limg, cv.COLOR_LAB2BGR)
        final = cv.resize(final,(457, 569))
        final = cv.cvtColor(final, cv.COLOR_BGR2RGB)
        self.result = final
        return self.result


    def image_contrast(self, percentage_of_contrast, image_location):
        img = cv.imread(image_location)
        lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
        
        l, a, b = cv.split(lab)
        clahe = cv.createCLAHE(clipLimit=(percentage_of_contrast/100), tileGridSize=(8,8))
        cl = clahe.apply(l)
        limg = cv.merge((cl,a,b))
        final = cv.cvtColor(limg, cv.COLOR_LAB2BGR)
        final = cv.resize(final,(457, 569))
        final = cv.cvtColor(final, cv.COLOR_BGR2RGB)
        self.result = final
        return self.result

class changing_brightness:
    def __init__(self, image_name, percentage_of_brightness):
        self.image_name = image_name
        self.percentage_of_brightness = percentage_of_brightness

    def brighting_enhancer(self):
        img = cv.imread(f"{self.image_name}")
        # cv.imshow('final1', img)
        lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
        l, a, b = cv.split(lab)
        clahe = cv.createCLAHE(clipLimit=(self.percentage_of_brightness/100), tileGridSize=(8,8))
        cl = clahe.apply(l)
        limg = cv.merge((cl,a,b))
        final = cv.cvtColor(limg, cv.COLOR_LAB2BGR)
        final = cv.resize(final,(500,500))
        
        return final

class save_file:
    def __init__(self,image, location, width, height):
        self.image = image
        self.location = location
        self.width = width
        self.height = height

    def save_image(self):
        img = cv.resize(self.image, (self.width, self.height))
        img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        cv.imwrite(f"{self.location}", img)

class Merging_images:
    def __init__(self, first_image, second_image):
        self.first_image = first_image
        self.second_image = second_image
    
    def merging_action(self, percentage_dominance):
        img1 = cv.imread(self.first_image)
        img1 = cv.resize(img1,(457, 569))

        img2 = cv.imread(self.second_image)
        img2 = cv.resize(img2,(457, 569))

        output = cv.addWeighted(img1,percentage_dominance/100, img2, (100-percentage_dominance)/100, 0)
        output = cv.cvtColor(output, cv.COLOR_BGR2RGB)
        # cv.imshow('output', output)
        # cv.waitKey(0)
        return output

class adv_coloring:
    def __init__(self,filename, color1, color2, color_rate1, color_rate2):
        self.filename = filename
        self.color1 = color1
        self.color2 = color2

        self.color_rate1 = color_rate1 
        self.color_rate2 = color_rate2 

        self.result = None
        
        self.img = cv.imread(self.filename)
        self.img = cv.resize(self.img, (457, 569))

    def color_action(self):
        
        if self.color1 == 'red':
            self.img[:,:,2] = self.color_rate1
        if self.color1 == 'blue':
            self.img[:,:,0] = self.color_rate1
        if self.color1 == 'green':
            self.img[:,:,1] = self.color_rate1
              
        if self.color2 == 'red':
            self.img[:,:,2] = self.color_rate2
        if self.color2 == 'blue':
            self.img[:,:,0] = self.color_rate2
        if self.color2 == 'green':
            self.img[:,:,1] = self.color_rate2
        
        
        self.img = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)
        return self.img
        

if __name__=="__main__":
    x = adv_coloring(filename='image_1.jpg', color1='red', color2='green', color_rate1=100, color_rate2=30)
    x.color_action()
    