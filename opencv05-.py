import cv2 as cv

img = cv.imread("datas/images/lena.png")
cap1 = cv.VideoCapture("datas/videos/Armbot.mp4")
cap2 = cv.VideoCapture(0)

try:
    while 1:
        cv.imshow("untitled", img)

        if cv.waitKey(0) == ord('v'):
            while cap1.isOpened():
                ret, frame = cap1.read()
                cv.imshow("untitled", frame)
                if cv.waitKey(10) == ord('i'):
                    break
                    
        elif cv.waitKey(0) == ord('w'):
            while cap2.isOpened():
                ret, frame = cap2.read()
                cv.imshow("untitled", frame)
                if cv.waitKey(1) == ord('i'):
                    break

        elif cv.waitKey(0) == ord('q'):
            break

except:
    pass

finally:
    cap1.release()
    cap2.release()
    cv.destroyAllWindows()
