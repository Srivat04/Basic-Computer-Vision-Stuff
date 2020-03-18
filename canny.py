import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True,help = "HELP")
args = parser.parse_args()

image = cv.cvtColor(cv.imread(args.image),cv.COLOR_BGR2GRAY)
cv.imshow("Original",image)
image = cv.GaussianBlur(image,(5,5),0)
cv.imshow("Blurred Image",image)

canny = cv.Canny(image,30,150)
cv.imshow("Canny Edge of the Image",canny)
cv.waitKey(0)

