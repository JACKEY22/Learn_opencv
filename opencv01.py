import cv2 as cv

img = cv.imread("datas/images/lena.png") #<class 'numpy.ndarray'>
cv.imshow("Lena Soderberg", img)

cv.waitKey(0)