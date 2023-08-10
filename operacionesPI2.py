

import cv2
import numpy as np

imagen = cv2.imread('i2.jpg')
if imagen is None:
    print('No se pudo cargar la imagen.')
    exit()

altura, anchura = imagen.shape[:2]

# Valor máximo de desplazamiento en píxeles
max_desplazamiento = 1

# Genera una matriz aleatoria de desplazamiento
mapa_desplazamiento = np.random.randint(-max_desplazamiento, max_desplazamiento, (altura, anchura, 2), dtype=np.int32)

imagen_distorsionada = np.zeros_like(imagen)

for y in range(altura):
    for x in range(anchura):
        dx, dy = mapa_desplazamiento[y, x]
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < anchura and 0 <= new_y < altura:
            imagen_distorsionada[new_y, new_x] = imagen[y, x]

cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Distorsionada', imagen_distorsionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
