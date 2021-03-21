import cv2 as cv
import numpy as np


class ImageInterface:
    def __init__(self, ImageName):
        self.ImageName = ImageName

    def show_blue(self):
        # In the img variable we have loaded the image
        img = cv.imread(self.ImageName)

        def func(x):
            pass

        # Here we have resized the image
        img_resize = cv.resize(img, (560, 506))

        cv.namedWindow('frame')
        cv.moveWindow('frame', 570, 0)

        # putting the trackbars on the frame
        cv.createTrackbar('Blue', 'frame', 0, 255, func)

        # This will show the image
        while True:

            cv.imshow('frame', img_resize)
            b = cv.getTrackbarPos('Blue', 'frame')

            img_resize[:, :, 0] = b
            
            if cv.waitKey(1) == ord('q'):
               break
        cv.destroyAllWindows()

    def show_red(self):
        # In the img variable we have loaded the image
        img = cv.imread(self.ImageName)

        def func(x):
            pass

        # Here we have resized the image
        img_resize = cv.resize(img, (560, 506))

        cv.namedWindow('frame')
        cv.moveWindow('frame', 570, 0)

        # putting the trackbars on the frame

        cv.createTrackbar('Red', 'frame', 0, 255, func)
        

        # This will show the image
        while True:
            cv.imshow('frame', img_resize)
            r=cv.getTrackbarPos('Red', 'frame')
            
            img_resize[:,:,2]=r

            if cv.waitKey(1) == ord('q'):
                
                break
        cv.destroyAllWindows()

    def show_green(self):
        # In the img variable we have loaded the image
        img = cv.imread(self.ImageName)

        def func(x):
            pass

        # Here we have resized the image
        img_resize = cv.resize(img, (560, 506))

        cv.namedWindow('frame')
        cv.moveWindow('frame', 570, 0)

        # putting the trackbars on the frame
        cv.createTrackbar('Green', 'frame', 0, 255, func)
        

        # This will show the image
        while True:

            cv.imshow('frame', img_resize)
            
            g=cv.getTrackbarPos('Green', 'frame')
           
            img_resize[:,:,1]=g
           
            if cv.waitKey(1) == ord('q'):
                break
        cv.destroyAllWindows()

if __name__ == "__main__":
    x = ImageInterface('image.jpg')
    x.show_red()
