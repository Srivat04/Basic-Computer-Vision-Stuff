import numpy as np
import cv2 as cv
import argparse
from matplotlib import pyplot as plt

def plot_histogram(image , title, mask = None) :
	chans  = cv.split(image)
	colors = ("b","g","r")
	plt.figure()
	plt.title(title)
	plt.xlabel("Bins")
	plt.ylabel("# of Pixels")
	for (chan,color) in zip(chans,colors) :
		hist = cv.calcHist([chan],[0],mask,[256],[0,256])
		plt.plot(hist, color = color)
		plt.xlim([0,256])


parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True,help = "HELP???")
args = parser.parse_args()

image = cv.imread(args.image)
cv.imshow("Original",image)
plot_histogram(image,"Histogram for original image")

mask = np.zeros(image.shape[:2],dtype = 'uint8')
cv.rectangle(mask,(15,15),(100,100),255,-1)
cv.imshow("Mask",mask)

masked = cv.bitwise_and(image,image,mask = mask)
cv.imshow("Masked Image",masked)

plot_histogram(image,"Histogram for Masked image",mask = mask)
plt.show()
cv.waitKey(0)