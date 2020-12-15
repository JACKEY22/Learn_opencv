import cv2 as cv 
import numpy as np

drawing = False 
ix, iy = -1, -1

def draw_shape(event, x, y, flags, param):
    global ix, iy, drawing
    
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True: 
            cv.rectangle(img, (ix, iy), (x,y), (0, 255, 0), 0)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.rectangle(img, (ix, iy), (x,y), (0, 255, 0), -1)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_shape)

while 1:
    cv.imshow('image', img)
    cv.waitKey(1)