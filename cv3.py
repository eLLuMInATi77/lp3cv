import cv2
import numpy as np

# Load the image
image = cv2.imread("img/fruit.jpeg")
mask = np.zeros(image.shape[:2], np.uint8)

# Define background and foreground models (required by GrabCut but initially set to zero)
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)

# Define a rectangle around the object for the GrabCut algorithm
rect = (50, 50, image.shape[1] - 100, image.shape[0] - 100)  # Adjust as needed

# Apply GrabCut algorithm
cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

# Modify mask so the segmented area is highlighted
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
segmented_image = image * mask2[:, :, np.newaxis]

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
