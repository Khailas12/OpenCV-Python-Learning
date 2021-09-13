import cv2

# img = cv2.imread(
#     "OpenCV-Learning\images\lena.png"
# )

# cv2.imshow('Output', img)
# cv2.waitKey(0)


vid = cv2.VideoCapture(
    'OpenCV-Learning/images/test_video.mp4'
)

while True:
    success, video = vid.read()
    cv2.imshow('video', video)
    if cv2.waitKey(1) & 0xFF == ord('q'):   # q = Press q to close
        break



# cv2.waitkey(1) returns a 32-bit integer corresponding to the pressed key. & 0xFF is a bit mask which sets the left 24 bits to zero, because ord() returns a value betwen 0 and 255, since your keyboard only has a limited character set