import cv2
import numpy as np

def apply_sepia_filter(image):
    sepia_matrix = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia_image = cv2.transform(image, sepia_matrix)

    # Ajustar los valores para que estén en el rango 0-255
    sepia_image[np.where(sepia_image > 255)] = 255
    sepia_image = np.uint8(sepia_image)

    return sepia_image

# Cargar la imagen
imagen = cv2.imread('Spiderman.jpg')

# Aplicar el filtro de sepia
imagen_sepia = apply_sepia_filter(imagen)

# Mostrar la imagen original y la imagen con el filtro de sepia
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Filtro Sepia', imagen_sepia)
cv2.waitKey(0)
cv2.destroyAllWindows()