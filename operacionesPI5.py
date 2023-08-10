import cv2
import numpy as np

IMG = cv2.imread('i5.jpg')
cv2.imshow('Imagen', IMG)
IMG = cv2.cvtColor(IMG, cv2.COLOR_BGR2RGB)

K = np.ones((5, 5), np.float32)/25
HMG = cv2.filter2D(IMG, -1, K)
BL = cv2.blur(IMG, (5, 5))

T = ['Imagen Original ', '2D Convolution', 'Blur']
IMGS = [IMG, HMG, BL]

for j in range(3):
    cv2.imshow(T[j], IMGS[j])

cv2.waitKey(0)
cv2.destroyAllWindows()

