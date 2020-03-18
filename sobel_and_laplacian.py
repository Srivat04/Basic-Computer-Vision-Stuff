import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True,help = "HELP")
args = parser.parse_args()

image = cv.cvtColor(cv.imread(args.image),cv.COLOR_BGR2GRAY)
cv.imshow("Original",image)

lap = cv.Laplacian(image,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian of the image",lap)

sobelX = cv.Sobel(image,cv.CV_64F,1,0)
sobelY = cv.Sobel(image,cv.CV_64F,0,1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobel_combined = cv.bitwise_or(sobelX,sobelY)
cv.imshow("Sobel X",sobelX)
cv.imshow("Sobel Y",sobelY)
cv.imshow("Combined Sobel",sobel_combined)

cv.waitKey(0)




