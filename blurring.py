import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True,help = "Help!!!")
args = parser.parse_args()

image = cv.imread(args.image)
cv.imshow("Original",image)

blurred_avg = np.hstack([cv.blur(image,(3,3)),cv.blur(image,(5,5)),cv.blur(image,(7,7))])
cv.imshow("Average Blurring ",blurred_avg)

blurred_gau = np.hstack([cv.GaussianBlur(image,(3,3),0),
						 cv.GaussianBlur(image,(5,5),0),
						 cv.GaussianBlur(image,(7,7),0)])
cv.imshow("Gaussian Blur ",blurred_gau)

blurred_med = np.hstack([cv.medianBlur(image,3),
						 cv.medianBlur(image,5),
						 cv.medianBlur(image,7)])
cv.imshow("Median Blur", blurred_med)

blurred_biF = np.hstack([cv.bilateralFilter(image,5,21,21),
						 cv.bilateralFilter(image,7,31,31),
						 cv.bilateralFilter(image,9,41,41)])
cv.imshow("Bilateral Filter ",blurred_biF)

cv.waitKey(0)