import cv2 as cv 
import numpy as np

def make_canny(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray,(3,3),0)
    canny = cv.Canny(blur,50,150)
    return canny   

def make_ROI(image, vertices):
    mask = np.zeros_like(image)

    if len(image.shape) > 2:
        channel = iamge.shape[2]
        ignore_mask_color = (255,) * channel
    else:
        ignore_mask_color = 255

    cv.fillPoly(image, vertices, ignore_mask_color)
    masked_image = cv.bitwise_and(image, mask)
    return masked_image
    
def main():
    cap = cv.VideoCapture("datas/videos/roadway_01.mp4")

    while cap.isOpened():
        ret, image = cap.read()
        canny = make_canny(image)
        vertices = canny[[(0,360),(1280,360),(0,720),(1280,720)]]
        mask = make_ROI(canny, vertices)

        cv.imshow("canny", mask)

        if cv.waitKey(0) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

main()








