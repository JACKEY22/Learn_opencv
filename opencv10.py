import cv2 as cv
import os

dir_name = "./datas/images/imageframes" 
files = os.listdir(dir_name)

file_name = dir_name + "/image_1.png"
img = cv.imread(file_name)
height, width, layers = img.shape
size = (height, width)
fps = 0.5

out_file_path = dir_name + "/output_video.avi"
out_file = cv.VideoWriter(out_file_path, cv.VideoWriter_fourcc(*'DIVX'), fps, size) 

for count in range(len(files)):
    filename = dir_name + "/image_" + str(count) + ".png"
    frames = cv.imread(filename)
    if frames is not None:
        cv.imshow("image_" + str(count), img)
        out_file.write(frames)
        
        #cv.waitKey(1)

