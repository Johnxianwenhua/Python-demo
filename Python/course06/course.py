import cv2
import numpy as np

img = cv2.imread("bookpage.jpg")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

retval, threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)
retval2, threshold2 = cv2.threshold(img2,12,255,cv2.THRESH_BINARY)

img3 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imwrite("threshold.png",threshold)
cv2.imwrite("threshold2.png",threshold2)
cv2.imwrite("gaus.png",img3)
