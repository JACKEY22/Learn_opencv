import cv2 as cv 
import numpy as np

## perspective - gray - threshhold 


points = list()

def get_points(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN: 
        print(f'{x},{y}')
        points.append([x, y])

def align(img):

    img = cv.imread(f"datas/images/{img}")
    img = cv.resize(img,None,fx = 0.2, fy = 0.2)

    cv.namedWindow('img') 
    cv.setMouseCallback('img', get_points, img) 
    cv.imshow('img', img) 
    
    if cv.waitKey() == ord('q'):
        print("wait a sec...")

    width = points[1][0] - points[0][0]
    height = points[2][1] - points[0][1]

    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

    matrix = cv.getPerspectiveTransform(pts1,pts2)
    img_output = cv.warpPerspective(img, matrix, (width,height))
    img_output_gray = cv.cvtColor(img_output, cv.COLOR_BGR2GRAY)
    
    cv.imshow("image", img_output_gray)

    cv.waitKey(0)
    cv.destroyAllWindows()
    return img_output_gray

img = align("namecard_02.jpg")

# img = cv.imread("datas/images/reciept_kor.png")
# cv.imshow("image",img)
# cv.waitKey(0)

# width, height = 220, 390

# pts1 = np.float32([[65,25],[225,25],[30,405],[253,405]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# matrix = cv.getPerspectiveTransform(pts1,pts2)
# img_output = cv.warpPerspective(img, matrix, (width,height))
# cv.imshow("image", img_output)
# cv.waitKey(0)

