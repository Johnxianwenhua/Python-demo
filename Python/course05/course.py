import cv2
import numpy as np

img1 = cv2.imread("watch.png",cv2.IMREAD_COLOR)
img2 = cv2.imread("icon.png",cv2.IMREAD_COLOR)

#两图片像素叠加
add = img1+img2
cv2.imwrite("img01.png",add)
#两图片像素叠加
add2 = cv2.add(img1,img2)
cv2.imwrite("img02.png",add2)
#两图片像素叠加
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
cv2.imwrite("img03.png",weighted)

icon = cv2.imread("icon.png",cv2.IMREAD_COLOR)
watch = cv2.imread("watch.png",cv2.IMREAD_COLOR)

rows, cols, channels = icon.shape

roi = watch[0:rows,0:cols]

icon_gray = cv2.cvtColor(icon,cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(icon_gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

watch_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

icon_fg = cv2.bitwise_and(icon,icon,mask=mask)

dst = cv2.add(watch_bg,icon_fg)

watch[0:rows,0:cols] = dst

cv2.imwrite("result_01.png",watch)
cv2.imwrite("result_02.png",mask_inv)
cv2.imwrite("result_03.png",watch_bg)
cv2.imwrite("result_04.png",icon_fg)
cv2.imwrite("result_05.png",dst)
