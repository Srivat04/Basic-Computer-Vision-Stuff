import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True, help = "F*** off")
args = parser.parse_args()

image = cv.imread(args.image)
cv.imshow("RGB_Colourspace",image)

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale image",gray)

hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
cv.imshow("HSV colorspace",hsv)

lab = cv.cvtColor(image,cv.COLOR_BGR2LAB)
cv.imshow("L*a*b",lab)

cv.waitKey(0)