import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True,help = "Fuck off")
args = parser.parse_args()

image = cv.imread(args.image)
cv.imshow("Original",image)

(B,G,R) = cv.split(image)
zeros = np.zeros(image.shape[:2],dtype = 'uint8')

Red   = cv.merge([zeros,zeros,R])
Blue  = cv.merge([B , zeros,zeros])
Green = cv.merge([zeros,G,zeros])

cv.imshow("Red_Channel",Red)
cv.imshow("Green_Channel",Green)
cv.imshow("Blue_Channel",Blue)

cv.waitKey(0)
