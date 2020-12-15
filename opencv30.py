import cv2 as cv 
import os

cascade = cv.CascadeClassifier("datas/haar_cascade_files/haarcascade_frontalface_default.xml")

cwd = os.getcwd()
dir_name = cwd + "/datas/images/faces"

if not os.path.exists(dir_name):
    os.mkdir(dir_name)


cap = cv.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(frame_gray, 1.1, 4)
    
    put_text = "Face not Found!"
    cv.putText(frame, put_text, (50,50), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0), 1)
    cv.imshow("Face Cropper", frame)
    if cv.waitKey(10) ==  ord('q'):
        break

    count = 0
    if len(faces) != 0:
        for (x, y, w, h) in faces:
            count = count + 1
            cropped_area = frame[y:y+h,x:x+w]
            area = cv.resize(cropped_area, (200,200))
        

            file_name = dir_name + '/user' + str(count) + '.jpg'
            cv.imwrite(file_name, cropped_area)

            put_text = "Face Found!"
            cv.putText(area, put_text, (50,50), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0), 1)
            cv.imshow("Face Cropper", area)
            if cv.waitKey(1) == ord('q') or count == 1000:
                break
    
cap.release()