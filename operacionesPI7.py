import cv2
import numpy as np

def lark_filter(image):
    # Apply the Lark filter to the image
    # Increase saturation
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image_hsv[:, :, 1] = np.clip(image_hsv[:, :, 1] + 20, 0, 255)
    image_filtered = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

    # Reduce contrast and add faded highlights
    alpha = 0.7
    beta = 30
    image_filtered = np.clip(alpha * image_filtered + beta, 0, 255).astype(np.uint8)

    return image_filtered

# Load the image
image = cv2.imread('i7.jpg')

# Apply the Lark filter
filtered_image = lark_filter(image)

# Show the original and filtered images
cv2.imshow('Original', image)
cv2.imshow('Lark Filtered', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
