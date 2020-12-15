import cv2 as cv 
import numpy as np
import pytesseract
from pytesseract import Output

image = cv.imread("datas/images/plate_kor.jpg")
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, image_binary = cv.threshold(image_gray, 253, 255, 0)

compare = np.hstack((image_gray,image_binary))
# cv.imshow("compare", compare)
# cv.waitKey(0)

contours, hierarchy = cv.findContours(image_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) 

for contour in contours:
    
    area = cv.contourArea(contour)
    epsilon = 0.025*cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, epsilon, True)
    
    if len(approx) == 4 and area > 200:

        cv.drawContours(image, [approx], 0, (0,0,255), 3)
        cv.imshow("image", image)
        cv.waitKey(0)

        print(approx)
        points = approx[0:4,0,0:2]

        width = points[3][0] - points[0][0]
        height = points[1][1] - points[0][1]

        pts1 = np.float32(points)
        pts2 = np.float32([[0,0],[0,height],[width,height],[width,0]])
        matrix = cv.getPerspectiveTransform(pts1,pts2)
        image_perspective = cv.warpPerspective(image, matrix, (width,height))

        cv.imshow("image_perspective", image_perspective)
        cv.waitKey(0)
        # cv.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 3)
        # cv.putText(image, "Rec", (x,y), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 1)


        custom_config = r'--oem 3 --psm 6 -l kor+eng'
        words = pytesseract.image_to_data(image_perspective, config = custom_config, output_type=Output.DICT) ## pytesseract
        print(words['text'])


