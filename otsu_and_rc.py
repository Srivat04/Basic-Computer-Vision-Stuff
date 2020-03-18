from __future__ import print_function
import numpy as np
import cv2 as cv
import argparse
import mahotas

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True,help = "HELP!!!!")
args = parser.parse_args()

image = cv.imread(args.image)
image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Original",image)
blurred = cv.GaussianBlur(image,(5,5),0)

T = mahotas.thresholding.otsu(blurred)
print("Otsu's Threshold is {}".format(T))

thresh = image.copy()
thresh[thresh>T] = 255   #Why cant you write it in opposite order???
thresh[thresh<T] = 0
thresh = cv.bitwise_not(thresh)
cv.imshow("Otsu Thresholded image",thresh)

T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard's Threshold is {}".format(T))

thresh = image.copy()
thresh[thresh>T] = 255
thresh[thresh<T] = 0
thresh = cv.bitwise_not(thresh)
cv.imshow("Riddler-Calvard Thresholded image ",thresh)

cv.waitKey(0)


