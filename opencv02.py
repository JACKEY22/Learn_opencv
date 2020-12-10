import cv2 as cv

frameWidth = 640 
frameHeight = 480

cap = cv.VideoCapture("datas/videos/Armbot.mp4")

while 1:
    current_frame = cap.get(cv.CAP_PROP_POS_FRAMES)
    total_frame = cap.get(cv.CAP_PROP_FRAME_COUNT)
    print(f"{current_frame}/{total_frame}")

    success, img = cap.read() # <class 'tuple'> (True, array([[[231, 250, 2...ype=uint8)) shape 328 568 3
    img_resized = cv.resize(img, (frameWidth, frameHeight)) # 480 640 3
    cv.imshow("result", img_resized)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
