import cv2
import numpy as np 


image = cv2.imread('Spiderman.jpg')
if image is None:
    print('No se pudo cargar la imagen.')
    exit()

# Centro del efecto "twirl"
center_x = image.shape[1] // 2
center_y = image.shape[0] // 2

# Radio del efecto "twirl"
radius = min(center_x, center_y) // 2

# Ángulo de rotación del efecto "twirl"
angle = 180

# Factor de distorsión del efecto "twirl"
strength = 1.0

twirl_image = np.zeros_like(image)

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        # Calcula la distancia del píxel al centro del efecto "twirl"
        dx = x - center_x
        dy = y - center_y
        distance = np.sqrt(dx**2 + dy**2)
        
        # Calcula el ángulo de desplazamiento
        if distance < radius:
            angle_offset = (1 - distance / radius) * angle * strength
            angle_offset = np.deg2rad(angle_offset)
            
            # Calcula las coordenadas del píxel en la imagen de origen
            src_x = int(center_x + dx * np.cos(angle_offset) - dy * np.sin(angle_offset))
            src_y = int(center_y + dx * np.sin(angle_offset) + dy * np.cos(angle_offset))
            
            # Verifica que las coordenadas estén dentro de los límites de la imagen
            if 0 <= src_x < image.shape[1] and 0 <= src_y < image.shape[0]:
                twirl_image[y, x] = image[src_y, src_x]

cv2.imshow('Imagen Original', image)
cv2.imshow('Imagen con Efecto Twirl', twirl_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
