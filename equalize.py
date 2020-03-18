import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True,help = "HELP!!!!")
args = parser.parse_args()

image = cv.imread(args.image)
image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

eq = cv.equalizeHist(image)

cv.imshow("Histogram Equalization", np.hstack([image,eq]))
cv.waitKey(0)
