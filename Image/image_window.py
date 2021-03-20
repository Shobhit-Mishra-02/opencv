import cv2 as cv
import numpy as np

class ImageInterface:
    def __init__(self, ImageName):
        self.ImageName = ImageName

    def show(self):
        img = cv.imread(self.ImageName)
        cv.imshow('frame', img)
        cv.waitKey(0)