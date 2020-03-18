from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True, help = "???")
args = parser.parse_args()

image = cv.imread(args.image)
chans = cv.split(image)
colors = ("b","g","r")

plt.figure()
plt.title("Flattened Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan,color) in zip(chans, colors) :
	hist = cv.calcHist([chan],[0],None,[256],[0,256])
	plt.plot(hist,color = color)
	plt.xlim([0,256])

fig = plt.figure()
ax  = fig.add_subplot(131)
hist = cv.calcHist([chan[1],chan[0]],[0,1],None,[32,32],[0,256,0,256])
p = ax.imshow(hist,interpolation = "nearest")
ax.set_title(" 2D Histogram for B and G")
plt.colorbar(p)

ax  = fig.add_subplot(132)
hist = cv.calcHist([chan[2],chan[1]],[0,1],None,[32,32],[0,256,0,256])
p = ax.imshow(hist,interpolation = "nearest")
ax.set_title(" 2D Histogram for G and R")
plt.colorbar(p)

ax  = fig.add_subplot(133)
hist = cv.calcHist([chan[2],chan[0]],[0,1],None,[32,32],[0,256,0,256])
p = ax.imshow(hist,interpolation = "nearest")
ax.set_title(" 2D Histogram for R and B")
plt.colorbar(p)

plt.show()
cv.waitKey(0)

