import cv2
import numpy as np

rectangle = np.zeros((600,600),dtype = 'uint8')
cv2.rectangle(rectangle,(100,100),(500,500),255,-1)

circle = np.zeros((600,600),dtype = 'uint8')
cv2.circle(circle,(300,300),250,255,-1)

cv2.imshow("Rectangle",rectangle)
cv2.imshow("Circle",circle)

And = cv2.bitwise_and(rectangle,circle)
Or  = cv2.bitwise_or(rectangle,circle)
Xor = cv2.bitwise_xor(rectangle,circle)
Not = cv2.bitwise_not(circle)

cv2.imshow("And",And)
cv2.imshow("Or",Or)
cv2.imshow("Xor",Xor)
cv2.imshow("Not",Not)

cv2.waitKey(0)