import cv2 as cv 
import os 

cwd = os.getcwd()
cascade = cv.CascadeClassifier(cwd + "/datas/haar_cascade_files/haarcascade_eye.xml")

img = cv.imread(cwd + "/datas/images/people.jpg") 
print(img.shape)
# img = cv.resize(img,None, fx=0.25,fy=0.25)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
eyes = cascade.detectMultiScale(img_gray, 1.1, 4)
count=0
print(eyes.shape)
for (x, y, w, h) in eyes:
    
    count = count + 1
    dir_name = cwd + "/datas/images/cropped_images_eyes"
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    img_cropped = img[y:y+h,x:x+w]
    
    cv.imshow("Result", img)
    cv.imshow("cropped", img_cropped)

    if not os.path.exists(dir_name):os.mkdir(dir_name)
    
    cv.imwrite(dir_name + "/image_" + str(count) + ".jpg", img_cropped)

    cv.waitKey(0)