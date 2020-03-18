import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True,help = "HELP!!!")
args = parser.parse_args()

Image = cv.imread(args.image)
cv.imshow("Original",Image)
image = cv.cvtColor(Image,cv.COLOR_RGB2GRAY)
blurred = cv.GaussianBlur(image ,(5,5),0)

thresh = cv.adaptiveThreshold(blurred,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,4)
cv.imshow("Mean Thresh",thresh)

thresh = cv.adaptiveThreshold(blurred,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,15,3)
cv.imshow("Gaussian Thresh",thresh)

cv.waitKey(0)
