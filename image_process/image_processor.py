import cv2 as cv
import numpy as np

class image_convertor:
    def __init__(self, filename):
        self.filename = filename
        self.result = None

    def color_to_gray(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (500,500))
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        self.result = img
        return self.result

    def color_to_red(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (500,500))
        img[:,:,2] = 115

        self.result = img

        return self.result

    def color_to_blue(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (500,500))

        img[:,:,0] = 115

        self.result = img

        return self.result
    
    def color_to_green(self):
        img = cv.imread(self.filename)
        img = cv.resize(img, (500,500))

        img[:,:,1] = 115

        self.result = img

        return self.result

        

    def show(self):
        cv.imshow('frame', self.result)
        cv.waitKey(0)
    
    def save_image(self, image, location):
        cv.imwrite(f"{location}.png", image)
        

if __name__=="__main__":
    x=image_convertor('image_1.jpg')
    x.color_to_gray()
    x.show()
    x.save_image()
