import numpy as np
import cv2 as cv

def translate(image,x,y) :
	M = np.float32([[1,0,x],[0,1,y]])
	shifted = cv.wardAffine(image,M,(image.shape[1],image.shape[0]))
	return shifted

def rotate(image,angle,centre = None , scale = 1.0) :
	(h ,w) = image.shape[:2]
	if centre is None :
		centre = (w/2,h/2)
	M = cv.getRotationMatrix2D(centre,angle,scale)
	rotated = cv.wardAffine(image,M,(w,h))
	return rotated

def resize(image,width = None,height = None, inter = cv.INTER_AREA) :
	dim = None
	(h,w) = image.shape[:2]
	if width is None and height is None :
		return image
	if width is None :
		r = height/float(h)
		dim = (int(r*w),height)
	else :
		r = width/float(w)
		dim = (width,int(r*h))
	resized = cv.resize(image,dim,interpolation = inter)
	return resized
