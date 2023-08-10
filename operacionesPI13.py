import cv2

# Cargar la imagen
imagen = cv2.imread('i13.jpg')

# Aplicar el filtro de inversión (negativo)
imagen_invertida = cv2.bitwise_not(imagen)

# Mostrar la imagen original y la imagen con el filtro de inversión
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Filtro de Inversión (Negativo)', imagen_invertida)
cv2.waitKey(0)
cv2.destroyAllWindows()