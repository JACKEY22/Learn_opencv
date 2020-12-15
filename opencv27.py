import cv2 as cv 
import numpy as np

image = cv.imread("datas/images/shapes.png")
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, image_binary = cv.threshold(image_gray, 219, 255, 0)
compare = np.hstack((image_gray, image_binary))
cv.imshow("compare", compare)
cv.waitKey(0)

contours, hierarchy = cv.findContours(image_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # list
for contour in contours:
    
    x,y,w,h = cv.boundingRect(contour)
    cv.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 1)
    
    if w < 500:

        epsilon = 0.025*cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, epsilon, True)
        cv.drawContours(image, [approx], 0, (255,0,0), 1)

        if len(approx) == 3:
            cv.putText(image, "Tri", (x,y), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)
        elif len(approx) == 4:
            cv.putText(image, "Rec", (x,y), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)
        else:
            cv.putText(image, "Cir", (x,y), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)

cv.imshow("image", image)
cv.waitKey(0)

