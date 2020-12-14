import cv2 as cv 
import numpy as np

img = cv.imread("datas/images/lena.png")
img_Canny = cv.Canny(img, 150, 200)
cv.imshow("Canny Image", img_Canny)

kernel = np.ones((9,9), np.uint8)
img_Dialation = cv.dilate(img_Canny, kernel, iterations=1)
cv.imshow("Dialation Image", img_Dialation)

img_Eroded = cv.erode(img_Dialation, kernel, iterations=1)
cv.imshow("Eroded Image", img_Eroded)

cv.waitKey(0)
cv.destroyAllWindows()