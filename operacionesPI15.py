import cv2
import numpy as np

def night_filter(image):
    # Ajustar el brillo y el contraste para oscurecer la imagen
    alpha = 0.7  # Puedes ajustar este valor para cambiar el brillo
    beta = -30   # Puedes ajustar este valor para cambiar el contraste
    dark_image = np.clip(alpha * image + beta, 0, 255).astype(np.uint8)

    # Ajustar el balance de color para obtener un tono más frío
    blue_balance = np.array([1.0, 0.3, 0.5])  # Puedes ajustar estos valores para cambiar el balance
    cold_image = np.clip(dark_image * blue_balance, 0, 255).astype(np.uint8)

    return cold_image

# Cargar la imagen
image = cv2.imread('i15.jpg')

# Aplicar el filtro nocturno
filtered_image = night_filter(image)

# Mostrar la imagen original y la imagen con el filtro nocturno
cv2.imshow('Imagen Original', image)
cv2.imshow('Filtro Nocturno', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
