import cv2

# Cargar la imagen
imagen = cv2.imread('i12.jpg')

# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Mostrar la imagen original y la imagen en escala de grises
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Filtro Blanco y Negro', imagen_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()