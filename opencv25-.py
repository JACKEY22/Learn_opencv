import cv2 as cv 
import numpy as np

def make_canny(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray,(3,3),0)
    canny = cv.Canny(blur,50,150)
    return canny   

def make_ROI(image):
    if len(image.shape) > 2: ## dimension
        channel = image.shape[2]
        ignore_mask_color = (255,) * channel
    else:
        ignore_mask_color = 255

    mask = np.zeros_like(image)
    area = np.array([[(500,360),(650,360),(1020,719),(270,719)]], np.int32)
    cv.fillPoly(mask, area, ignore_mask_color) ## filling ROI of mask with white
    ROI = cv.bitwise_and(image, mask)
    return ROI

def draw_lines(image, lines, color = [255,0,0], thickness = 3):
    for line in lines:
            for x1,y1,x2,y2 in line:
                cv.line(image, (x1,y1), (x2,y2), color, thickness)   
    
def get_lines(image):
    lines = cv.HoughLinesP(image, rho = 2, theta = np.pi/180, threshold = 90, minLineLength = 120, maxLineGap = 150)
    line_image = np.zeros((image.shape[0],image.shape[1],3), np.uint8) 
    draw_lines(line_image, lines)
    return line_image

def main():               
    cap = cv.VideoCapture("datas/videos/roadway_01.mp4")

    while cap.isOpened():
        ret, image = cap.read()
        canny = make_canny(image)
        ROI = make_ROI(canny)
        line = get_lines(ROI)

        image_with_line = cv.addWeighted(image, 0.7, line, 0.6, 0) 

        cv.imshow("canny", image_with_line)
        if cv.waitKey(20) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

main()
#https://pinkwink.kr/1264







