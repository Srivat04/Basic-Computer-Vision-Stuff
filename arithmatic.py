import argparse 
import cv2 as cv
import numpy as np 

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True,help = "Enter the path to the image")
args = parser.parse_args()

image  = cv.imread(args.image)
M 	= np.ones(image.shape,dtype = 'uint8')*100

add_opencv = cv.add(image,M)
sub_opencv = cv.subtract(image,M)

add_numpy = image + M
sub_numpy = image - M

cv.imshow("Opencv Add",add_opencv)
cv.imshow("Opencv sub",sub_opencv)
cv.imshow("Numpy Add" , add_numpy)
cv.imshow("Numpy Sub" , sub_numpy)

cv.waitKey(0)