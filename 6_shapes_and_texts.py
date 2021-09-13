import cv2
import numpy as np


# creating a matrix
img = np.zeros((512, 512, 3), np.uint8) # 512, 512 -> size of the matrix 
print(img)

#coloring image
img[:]= 255, 0, 0

#                         height         width
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 255), 3)

#                          h  &  w            color     thickness
cv2.rectangle(img, (0,0), (255, 350), (0, 0, 255), 2)

#             center point  30-> radius 
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

cv2.putText(img, "Bruce Wayne", (260, 200), cv2.FONT_HERSHEY_COMPLEX, 1,(0, 150, 0), 1)

cv2.imshow('Image', img)
cv2.waitKey(0)