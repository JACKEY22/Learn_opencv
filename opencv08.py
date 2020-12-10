import cv2 as cv

img = cv.imread("datas/images/messy.jpg")

cv.rectangle(img,(50,60),(110,130),(0,0,255),2)

cv.imshow("messy",img)

cv.waitKey(0)

