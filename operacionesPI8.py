import cv2
import numpy as np

def moon_filter(image):
    # Apply the Moon filter to the image
    # Reduce brightness and increase contrast
    alpha = 0.7
    beta = -30
    image_filtered = np.clip(alpha * image + beta, 0, 255).astype(np.uint8)

    # Adjust the color balance to add a blueish tint
    blue_balance = np.array([1.0, 0.7, 1.5])
    image_filtered = np.clip(image_filtered * blue_balance, 0, 255).astype(np.uint8)

    return image_filtered

# Load the image
image = cv2.imread('fiesta.jpg')

# Apply the Moon filter
filtered_image = moon_filter(image)

# Show the original and filtered images
cv2.imshow('Original', image)
cv2.imshow('Moon Filtered', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
