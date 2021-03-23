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
        

    def show(self):
        cv.imshow('frame', self.result)
        cv.waitKey(0)
    
    def save_image(self):
        cv.imwrite('image_1.png', self.result)

if __name__=="__main__":
    x=image_convertor('image_1.jpg')
    x.color_to_gray()
    x.show()
    x.save_image()
