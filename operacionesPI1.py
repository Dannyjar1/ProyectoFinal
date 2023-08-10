import cv2
import numpy as np

def apply_color_to_section(image, color, y_start, y_end):
    section = image[y_start:y_end, :]
    colorized_section = colorize_filter(section, color)
    image[y_start:y_end, :] = colorized_section
    return image

def colorize_filter(image, color):
    colorized_image = np.zeros_like(image)
    colorized_image[:] = color
    colorized_image = cv2.addWeighted(image, 0.7, colorized_image, 0.3, 0)
    return colorized_image

# Cargar la imagen
imagen = cv2.imread('i1.jpg')
cv2.imshow('Imagen Origal',imagen)

# Colores a aplicar (en formato BGR)
colores = [(0, 255, 255),   # Amarillo
           (255, 0, 0),     # Rojo
           (0, 0, 255)]     # Azul

# Dividir la imagen en tres secciones horizontales iguales
altura, anchura = imagen.shape[:2]
seccion_altura = altura // len(colores)

# Aplicar el filtro de tono a cada sección con un color diferente
for i, color in enumerate(colores):
    y_start = i * seccion_altura
    y_end = (i + 1) * seccion_altura if i < len(colores) - 1 else altura
    imagen = apply_color_to_section(imagen, color, y_start, y_end)

# Mostrar la imagen original y la filtrada
cv2.imshow('Imagen Original', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()