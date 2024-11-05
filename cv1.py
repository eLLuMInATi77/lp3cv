import cv2
import numpy as np

# Load the image
img = cv2.imread('img/fruit.jpeg')

# Display the original image
cv2.imshow('Original Image', img)
cv2.waitKey(0)

# Crop the image (x_start, y_start, width, height)
crop_img = img[50:200, 100:300]
cv2.imshow('Cropped Image', crop_img)
cv2.waitKey(0)


# Resize the image
resized_img = cv2.resize(img, (500, 500))
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_img)
cv2.waitKey(0)

#Apply thresholding
_, thresh_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresholded Image', thresh_img)
cv2.waitKey(0)

# Find contours
contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
contour_img = np.zeros_like(img)
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
cv2.imshow('Contours', contour_img)
cv2.waitKey(0)

# Blob detection
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 150
params.maxArea = 2000

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(thresh_img)

# Draw detected blobs as red circles
blob_img = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Blob Detection', blob_img)
cv2.waitKey(0)