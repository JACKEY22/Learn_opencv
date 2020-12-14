import cv2 as cv
import numpy as np
## cv.GaussianBlur

img = cv.imread("datas/images/lena.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_blur = cv.GaussianBlur(img_gray,(7,7),0)   

images = np.hstack((img_gray,img_blur))
cv.imshow("compare", images)
cv.waitKey(0)