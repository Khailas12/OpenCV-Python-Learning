import cv2
import numpy as np

img = cv2.imread(
    'OpenCV-Learning/images/p1.jpg'
)
kernal = np.ones((5, 5), np.uint8)

# converting into greyscale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # cvtColor converts img to differnt clr spaces


imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0) # kernal size = (7, 7). it can be (3, 3) or (5, 5) etc...
#sigmaX is (0)
# kernal = A matrix that we defines the size of and value of

# edge detector
imgCanny = cv2.Canny(img, 150, 200)

# to increase thickness of edge
imgDialation = cv2.dilate(imgCanny, kernal, iterations=1)

#to make img thinner
imgEroded = cv2.erode(imgDialation, kernal, iterations=1)


cv2.imshow('Greay Image', imgGray)
cv2.imshow('Blurred Image', imgBlur)
cv2.imshow('Canny image', imgCanny)
cv2.imshow('Dialation Image', imgDialation)
cv2.imshow('Eroded Image', imgEroded)
cv2.waitKey(0)