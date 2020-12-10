import cv2 as cv

cap = cv.VideoCapture(0)

try:
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv.imshow('frame', frame)
            if cv.waitKey(1) == 27:break #27 = esc

except:
    pass

finally:
    cap.release()
    cv.destroyAllWindows()
