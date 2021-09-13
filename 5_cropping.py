import cv2

img = cv2.imread('OpenCV-Learning/images/land.jpg')

# height first and width
imgCropped = img[0: 200, 200:500]

cv2.imshow('Untouched image', img)
cv2.imshow("Cropped image", imgCropped)
cv2.waitKey(0)