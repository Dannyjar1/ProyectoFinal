import cv2
import numpy as np
import cv2

img = cv2.imread('Spiderman.jpg')

blur = cv2.blur(img, (15, 15))

cv2.imshow('Original', img)
cv2.imshow('Difuminada', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
