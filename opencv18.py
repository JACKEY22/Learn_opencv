import cv2 as cv
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output
## cv.threshold

img = cv.imread('datas/images/reciept_kor_2.jpg',cv.IMREAD_GRAYSCALE)  
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY) # 127<pixel=0
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV) # 127>pixel=0
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC) # 127<pixel=pixel
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO) # 127>pixel=pixel
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV) # 127<pixel=0

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

custom_config = r'--oem 3 --psm 6 -l kor+eng'
words = pytesseract.image_to_data(thresh4, config = custom_config, output_type=Output.DICT) ## pytesseract

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
