import cv2
import numpy as np

def apply_watercolor_effect(image, kernel_size=5, strength=0.5):
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar un filtro de difuminado (Blur)
    imagen_blur = cv2.medianBlur(imagen_gris, kernel_size)

    # Aplicar el efecto acuarela
    imagen_acuarela = cv2.adaptiveThreshold(imagen_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, kernel_size, strength)

    # Convertir la imagen a formato BGR
    imagen_acuarela = cv2.cvtColor(imagen_acuarela, cv2.COLOR_GRAY2BGR)

    return imagen_acuarela

# Cargar la imagen
imagen = cv2.imread('I14.jpg')

# Aplicar el filtro de efecto acuarela
imagen_acuarela = apply_watercolor_effect(imagen)

# Mostrar la imagen original y la imagen con el filtro de efecto acuarela
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Filtro de Efecto Acuarela', imagen_acuarela)
cv2.waitKey(0)
cv2.destroyAllWindows()