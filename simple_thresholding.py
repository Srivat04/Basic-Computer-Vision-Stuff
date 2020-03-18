import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True,help = "HELP")
args = parser.parse_args()

Image = cv.cvtColor(cv.imread(args.image),cv.COLOR_BGR2GRAY)
cv.imshow("Original",Image)

image = cv.equalizeHist(Image)

blurred = cv.GaussianBlur(image,(11,11),0)
(T,thresh) = cv.threshold(blurred,155,255,cv.THRESH_BINARY)
cv.imshow("Threshold_Binary",thresh)

(T,thresh_inv) = cv.threshold(blurred,155,255,cv.THRESH_BINARY_INV)
cv.imshow("Inverse Threshold Binary",thresh_inv)

cv.imshow("Coins",cv.bitwise_and(Image,Image,mask = thresh_inv))

cv.waitKey(0)
