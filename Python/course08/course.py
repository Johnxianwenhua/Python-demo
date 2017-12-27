import cv2
import numpy as np

img = cv2.imread("gaus.png")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#blur = cv2.GaussianBlur(img2,(15,15),0)
#median = cv2.medianBlur(img2,15)
#bilateral = cv2.bilateralFilter(img2,15,75,75)

kernel = np.ones((3,3),np.uint8)

erosion = cv2.erode(img2,kernel,iterations = 1)
dilation = cv2.dilate(img2,kernel,iterations = 1)
opening = cv2.morphologyEx(img2,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(img2,cv2.MORPH_CLOSE,kernel)

#cv2.imwrite("blur.png",blur)
#cv2.imwrite("median.png",median)
#cv2.imwrite("bilateral.png",bilateral)

cv2.imwrite("erosion.png",erosion)
cv2.imwrite("dilation.png",dilation)
cv2.imwrite("open.png",dilation)
cv2.imwrite("close.png",dilation)

