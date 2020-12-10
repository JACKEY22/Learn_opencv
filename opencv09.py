import cv2 as cv 
import os

dir_name = "./datas/images/imageframes" 

def writeFrame(videocapture, second, count):
    videocapture.set(cv.CAP_PROP_POS_MSEC, second*1000)
    hasFrames, image = videocapture.read()
    if hasFrames:
        cv.imwrite(dir_name + "/image_" + str(count) + ".png", image)
    return hasFrames

def main():
    if not os.path.exists(dir_name): os.mkdir(dir_name)

    file_name = 'datas/videos/Armbot.mp4'
    cap = cv.VideoCapture(file_name)
    sec = 0
    cnt = 0
    framerate = 0.5
    success =  cap.isOpened()

    while success:
        sec = sec + framerate
        success = writeFrame(cap, sec, cnt) 
        cnt = cnt + 1 

main()



