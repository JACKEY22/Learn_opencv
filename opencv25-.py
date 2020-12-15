import cv2 as cv 
import numpy as np

points = list()

def nothing():
    pass

def get_points(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN: 
        print(f'{x},{y}')
        points.append([x, y])

def set_ROI(image):
    cv.namedWindow('view') 
    cv.setMouseCallback('view', get_points, image) 
    cv.imshow('view', image) 
    if cv.waitKey(0) == ord('q'):
        print("start detection...")

        
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
    area = np.array([[(points[0][0],points[0][1]),(points[1][0],points[1][1]),(points[2][0],points[2][1]),(points[3][0],points[3][1])]], np.int32)
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
    try:

        cap = cv.VideoCapture("datas/videos/roadway_01.mp4")
        ret, image = cap.read()
        canny = make_canny(image)
        set_ROI(canny)

        while cap.isOpened():
            ret, image = cap.read()
            canny = make_canny(image)
            
            
            cv.namedWindow("view")
            cv.createTrackbar('low threshold', 'view', 0, 1000, nothing)
            cv.createTrackbar('high threshold', 'view', 0, 1000, nothing)

            low = cv.getTrackbarPos('low threshold', 'view')
            high = cv.getTrackbarPos('high threshold', 'view')
            thresh = cv.Canny(canny, low, high)
            cv.imshow('view', thresh)
            cv.waitKey(15)
                

            ROI = make_ROI(canny)
            line = get_lines(ROI)
            image_with_line = cv.addWeighted(image, 0.7, line, 0.6, 0.2) 
            cv.imshow("detection", image_with_line)
            
            if cv.waitKey(15) == ord('q'):
                break

    except:
        pass
    finally:
        cap.release()
        cv.destroyAllWindows()

if __name__ == '__main__':
    main()















#https://pinkwink.kr/1264







