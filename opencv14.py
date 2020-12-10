import cv2 as cv 

cascade = cv.CascadeClassifier("datas/haar_cascade_files/haarcascade_frontalface_default.xml")
img = cv.imread('datas/images/faces.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = cascade.detectMultiScale(imgGray, 1.1, 4)
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    img_crop = img[]
cv.imshow("Result", img)
cv.waitKey(0)