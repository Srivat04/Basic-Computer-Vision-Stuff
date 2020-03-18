from matplotlib import pyplot as plt
import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",required = True, help = "You know what to do!!!")
args = parser.parse_args()

image = cv.imread(args.image)
cv.imshow("Original ",image)

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale ",gray )

hist = cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)