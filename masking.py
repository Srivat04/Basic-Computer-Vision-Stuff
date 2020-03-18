import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True,help = "You know what to do!!!")
args = parser.parse_args()

image = cv.imread(args.image)
cv.imshow("Original",image)

(h,w) = image.shape[:2]
mask = np.zeros((h,w),dtype = 'uint8')

cv.rectangle(mask,(int(.1*w),int(.1*h)),(int(.9*w),int(.9*h)),255,-1)
cv.imshow("Mask",mask)

masked = cv.bitwise_and(image,image,mask = mask)
cv.imshow("Image after masking",masked)
cv.waitKey(0)
