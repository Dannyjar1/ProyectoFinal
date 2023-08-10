import cv2
import numpy as np

def sierra_filter(image):
    # Apply the Sierra filter to the image
    # Reduce contrast and saturation
    alpha = 0.7
    beta = -30
    image_filtered = np.clip(alpha * image + beta, 0, 255).astype(np.uint8)

    # Adjust the color balance to add warm tones
    warm_balance = np.array([1.2, 1.0, 0.8])
    image_filtered = np.clip(image_filtered * warm_balance, 0, 255).astype(np.uint8)

    return image_filtered

# Load the image
image = cv2.imread('i9.jpg')

# Apply the Sierra filter
filtered_image = sierra_filter(image)

# Show the original and filtered images
cv2.imshow('Original', image)
cv2.imshow('Sierra Filtered', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
