import cv2
import numpy as np

def ginza_filter(image):
    # Apply the Ginza filter to the image
    # Enhance colors
    image_enhanced = np.clip(1.2 * image, 0, 255).astype(np.uint8)

    # Increase contrast
    alpha = 1.2
    beta = -20
    image_contrast = np.clip(alpha * image_enhanced + beta, 0, 255).astype(np.uint8)

    # Add a vignette effect
    h, w = image_contrast.shape[:2]
    center = (w // 2, h // 2)
    radius = int(np.sqrt(center[0]**2 + center[1]**2) * 0.7)

    mask = np.zeros_like(image_contrast)
    cv2.circle(mask, center, radius, (1, 1, 1), -1, cv2.LINE_AA)
    image_vignette = image_contrast * mask

    return image_vignette

# Load the image
image = cv2.imread('Spiderman.jpg')

# Apply the Ginza filter
filtered_image = ginza_filter(image)

# Show the original and filtered images
cv2.imshow('Original', image)
cv2.imshow('Ginza Filtered', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
