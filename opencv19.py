import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('datas/images/shaded.jpg',cv.IMREAD_GRAYSCALE)

ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,15,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,1)

titles = ['Original img', 'Global Th', 'Adaptive Mean Th', 'Adaptive Gaussian Th']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(1,4,i+1)
    plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()