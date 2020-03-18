from __future__ import print_function
import argparse
import numpy as np
import cv2 as cv

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True,help = "HELP!!!")
args = parser.parse_args()

Image = cv.imread(args.image)
image = cv.cvtColor(Image,cv.COLOR_BGR2GRAY)
cv.imshow("Original",Image)

blurred = cv.GaussianBlur(image,(11,11),0)
edged = cv.Canny(blurred,30,150)
cv.imshow("Edges",edged)

(dummy1,contours,dummy2) = cv.findContours(edged.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

print("The number of coins in this image is {}".format(len(contours)))

coins = Image.copy()
cv.drawContours(coins,contours,-1,(0,255,0),2)
cv.imshow("Coins",coins)

for (i,contour) in enumerate(contours):
	(x,y,w,h) = cv.boundingRect(contour)
	print("Coin {}".format(i+1))
	coin = Image[y:y+h,x:x+w]
	mask = np.zeros(image.shape[:2],dtype = 'uint8')
	((c_x,c_y),r) = cv.minEnclosingCircle(contour)
	cv.circle(mask,(int(c_x),int(c_y)),int(r),255,-1)
	mask = mask[y:y+h,x:x+w]
	cv.imshow("Masked Coin",cv.bitwise_and(coin,coin,mask = mask))
	cv.waitKey(0) 
