import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 640) # width
cam.set(4, 480) # height
cam.set(10, 100)  # brightness adjustment


while True:
    success, camera = cam.read()
    cv2.imshow('camera', camera)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break