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
    
    # def color_to_black(self):
    #     img = cv.imread(self.filename)
    #     img = cv.resize(img, (457, 569))

    #     edges = cv.Canny(img, 100,200)

    #     self.result = edges
    #     self.color_processed = True
    #     return self.result
    
    # def contrast(self, percentage_of_contrast, image=None):
        
    #     if image == None:
    #         img = cv.imread(self.filename)
    #     else:
    #         img = image
    #         img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

    #     lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
    #     l, a, b = cv.split(lab)
    #     clahe = cv.createCLAHE(clipLimit=(percentage_of_contrast/100), tileGridSize=(8,8))
    #     cl = clahe.apply(l)
    #     limg = cv.merge((cl,a,b))
    #     final = cv.cvtColor(limg, cv.COLOR_LAB2BGR)
    #     final = cv.resize(final,(457, 569))
    #     final = cv.cvtColor(final, cv.COLOR_BGR2RGB)
    #     self.result = final
    #     return self.result

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
        
        # cv.imshow('final', final)
        # cv.waitKey(0)
        
        return final

class save_file:
    def __init__(self,image, location):
        self.image = image
        self.location = location

    def save_image(self):
        cv.imwrite(f"{self.location}", self.image)

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
    
if __name__=="__main__":
    x=Merging_images(first_image='image_1.jpg', second_image='image.jpg')
    x.merging_action(80)
    