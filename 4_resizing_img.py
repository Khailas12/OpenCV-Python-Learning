import cv2

img = cv2.imread(
    'OpenCV-Learning/images/lambo.PNG'
)
print(img.shape)
# O/P -> (462, 623, 3) 
# 463 -> height | 623 -> Width | 3 -> Num for the channel that's BGR

imgResize = cv2.resize(img, (300, 200)) # 300-> width  |  200-> width
print(imgResize.shape)


cv2.imshow('Image Untouched', img)
cv2.imshow('Image resized', imgResize)
cv2.waitKey(0)