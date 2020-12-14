import cv2 as cv 
## cv.VideoWriter_fourcc
## cv.VideoWriter

cap = cv.VideoCapture(0)
#cap.set() 640 480 fps
print(c, c1)
codec = cv.VideoWriter_fourcc(*'XVID')
out_avi = cv.VideoWriter('datas/videos/output.avi', codec, 20.0, (640,480))
codec = cv.VideoWriter_fourcc(*'MP4V')
out_mp4 = cv.VideoWriter('datas/videos/output.mp4', codec, 20.0, (640,480))

while 1:
    ret, frame = cap.read()
    out_avi.write(frame)
    out_mp4.write(frame)
    cv.imshow('frame', frame)

    if cv.waitKey(10) == ord('q'):
        break

cap.release()
out_mp4.release()
out_avi.release()
