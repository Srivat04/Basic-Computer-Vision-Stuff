from __future__ import print_function
import argparse
import cv2 as cv

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True, help = "Path to the image")
args = parser.parse_args()
image = cv.imread(args.image)
(b,g,r) = image[0,0]
print("Pixel at (0,0) - Red = {} Blue = {} Green = {} ".format(r,g,b))


corner = image[0:100,0:100]
cv.imshow("Corner",corner)
cv.waitKey(0)

image[1:100,1:100] = (0,255,0)
cv.imshow("Updated_image",image)
cv.waitKey(0)