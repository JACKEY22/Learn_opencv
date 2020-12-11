import cv2 as cv 
import pytesseract
from pytesseract import Output

img = cv.imread("datas/images/3.png")
# def threshold(img):
#     return cv.threshold(img, 50,255,cv.THRESH_BINARY+cv.THRESH_OTSU)[1] ## based on 50 -> 0 / 255
print(img.shape)
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# img_gray = threshold(img_gray)

custom_config = r'--oem 3 --psm 6 -l kor+eng'
words_string = pytesseract.image_to_string(img_gray)
words = pytesseract.image_to_data(img_gray, config = custom_config, output_type=Output.DICT)

print(words.keys())
n_boxes = len(words['text'])
print(n_boxes)
for i in range(n_boxes):
    if int(words['conf'][i]) > 60:
        (x,y,w,h) = (words['left'][i], words['top'][i], words['width'][i], words['height'][i])
        cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
        cv.putText(img, words['text'][i],(x,y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1)
        img_crop = img[y:y+h,x:x+w] 
        cv.imshow('img_crop', img_crop)
        cv.imshow('Resource', img)
        cv.waitKey(0)

