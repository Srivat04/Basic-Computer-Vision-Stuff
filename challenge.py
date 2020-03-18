import numpy as np
import cv2 as cv

canvas = np.zeros((600,600,3), dtype = 'uint8')

for i in range( 0, 30):
	for j in range( 0, 30):
		if (i+j)%2 :
			cv.rectangle(canvas,(int(i*20),int(j*20)),(int(i*20+20),int(j*20+20)),(0,0,255),-1)

cv.circle(canvas,(300,300),100,(0,255,0),-1)
cv.imshow("canvas",canvas)
cv.waitKey(0)
