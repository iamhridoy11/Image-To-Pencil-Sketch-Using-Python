
#This program converts an image to a pencil sketch

#import the library
import cv2
from google.colab.patches import cv2_imshow

#Get the image file

filename = 'dogs.jpeg'

#Read in the image

img = cv2.imread(filename)

#Convert the image to Gray Scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Invert the image

invert_gray_image = 255 - gray_image

#Blur the image by using Gaussian function

blurred_img = cv2.GaussianBlur(invert_gray_image, (21,21), 0)

#Invert blurred image

invertBlurredImage = 255 - blurred_img

#Create pencil sketch image

pencilImage = cv2.divide(gray_image, invertBlurredImage, scale= 256.0)

#Show the image
cv2_imshow(img)
cv2_imshow(pencilImage)