
import numpy as np
import cv2 as cv

img = cv.imread('image.jpg')
# resize_img = cv.resize(img, (500,500))

# cv.imshow('frame', resize_img)

# cv.waitKey(0)

cv.namedWindow('Image')
cv.moveWindow('Image', 0,0)

cv.imshow('Image', img)
cv.waitKey(0)