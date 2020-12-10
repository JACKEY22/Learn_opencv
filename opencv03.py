import cv2 as cv

cap = cv.VideoCapture(0) # /dev/video0

while cap.isOpened():

    success, img = cap.read()
    cv.imshow("live webcam", img)

    if cv.waitKey(1) == ord('q'): break

cap.release()
