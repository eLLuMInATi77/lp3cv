import cv2
import numpy as np

# Create a blank image (white background)
image = np.ones((600, 600, 3), dtype="uint8") * 255

# Draw the text "OpenCV Annotation" at the top and an underline
cv2.putText(image, "OpenCV Annotation", (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv2.line(image, (140, 60), (460, 60), (0, 0, 0), thickness=2)  # Black line as an underline

# Draw the text "Rectangle" and the rectangle below it
cv2.putText(image, "Rectangle", (240, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
cv2.rectangle(image, (200, 140), (400, 240), (0, 255, 0), thickness=3)  # Green rectangle

# Draw the text "Circle" and the circle below it
cv2.putText(image, "Circle", (270, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
cv2.circle(image, (300, 350), 50, (0, 0, 255), thickness=-1)  # Red filled circle

# Draw the text "Ellipse" and the circular ellipse below it
cv2.putText(image, "Ellipse", (260, 420), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
cv2.ellipse(image, (300, 470), (50, 50), 0, 0, 360, (255, 255, 0), thickness=3)  # Cyan circular ellipse

# Show the image
cv2.imshow("Annotated Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
