import cv2 as cv 
import numpy as np

frameWidth = 240
frameHeight = 240

img = cv.imread("datas/images/lena.png")
img_resized = cv.resize(img, (frameWidth, frameHeight))

img_gray = cv.cvtColor(img_resized, cv.COLOR_BGR2GRAY)
grayToBGR = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)
# print(grayToBGR.shape)

cap_vid0 = cv.VideoCapture("datas/videos/Armbot.mp4")
cap_vid1 = cv.VideoCapture("datas/videos/roadway_01.mp4")
cap_cam0 = cv.VideoCapture(0)
cap_cam1 = cv.VideoCapture(2)

try:
    while cap_cam0.isOpened or cap_cam1.isOpened:
            ret0, cam0 = cap_cam0.read()
            ret1, cam1 = cap_cam1.read()
            ret2, vid0 = cap_vid0.read()
            ret3, vid1 = cap_vid1.read()

            cam0 = cv.resize(cam0, (frameWidth, frameHeight))
            cam1 = cv.resize(cam1, (480, frameHeight)) ## this cam has two lens so needs doubleed width
            vid0 = cv.resize(vid0, (frameWidth, frameHeight))
            vid1 = cv.resize(vid1, (frameWidth, frameHeight))
            # print(cam0.shape)
            # print(cam1.shape)

            cam1_split1 = cam1[0:240,0:240,0:3] ## split stereo cam
            cam1_split2 = cam1[0:240,240:480,0:3]
            # print(cam1_split1.shape)
            # print(cam1_split2.shape)

            test1 = np.hstack((grayToBGR,img_resized,vid0))
            test2 = np.hstack((cam1_split1,cam0,cam1_split2))
            test3 = np.vstack((test1,test2))
            
            
            cv.imshow("test",test3)
            if cv.waitKey(30) == ord('q'):break

except:
    pass

finally:
    cap_vid0.release()
    cap_vid1.release()
    cap_cam0.release()
    cap_cam1.release()

