import cv2
import numpy as np

# Lee la imagen
image = cv2.imread('bod.jpg')
if image is None:
    print('No se pudo cargar la imagen.')
    exit()

# Convierte la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplica el filtro de desenfoque gaussiano
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Aplica el filtro de detección de bordes Canny
edges = cv2.Canny(blurred, 100, 200)

# Muestra la imagen original y los bordes detectados
cv2.imshow('Imagen Original', image)
cv2.imshow('Bordes Detectados', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()