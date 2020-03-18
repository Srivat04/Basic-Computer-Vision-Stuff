import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s","--Shape",type = int ,nargs = '?', default = 1 ,choices = [1,2,3] , help = "Enter the shape you want to be shown : 1 for line,2 for rectangle,3 for circle ")
args = parser.parse_args()

canvas = np.zeros((300,300,3), dtype = 'uint8')

(centerX,centerY) = (canvas.shape[1]/2,canvas.shape[0]/2)

blue  = (255,0,0)
green = (0,255,0)
red   = (0,0,255)

if args.Shape == 1 :
	cv.line(canvas,(150,0),(150,300),green,3)
	cv.imshow("Canvas",canvas)
	cv.waitKey(0)
elif args.Shape == 2 :
	cv.rectangle(canvas,(50,50),(250,250),red,3)
	cv.imshow("Canvas",canvas)
	cv.waitKey(0)
else :
	cv.circle(canvas,(centerX,centerY),50,blue,3)
	cv.imshow("Canvas",canvas)
	cv.waitKey(0)

