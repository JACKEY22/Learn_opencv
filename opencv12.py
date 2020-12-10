import cv2 as cv 

img = cv.imread("datas/images/lambo.png")
cv.imshow("img",img)
print(img.shape)

img_resized = cv.resize(img, (1000,500))
cv.imshow("img_resized",img_resized)


wheel_cropped_01 = img[200:260,90:160]
cv.imshow("wheel_cropped_01", wheel_cropped_01)

wheel_cropped_02 = img[300:370,280:350]
cv.imshow("wheel_cropped_02", wheel_cropped_02)

# img_cropped_03 = img[0:500,400:600]
# cv.imshow("img_cropped_03", img_cropped_03)


cv.waitKey(0)