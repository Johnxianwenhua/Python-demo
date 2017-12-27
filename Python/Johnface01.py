#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:25:31 2017

@author: holdtime
"""

import cv2
import numpy as np
#from vc2 import cv

img = cv2.imread("lena.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imshow("demo1",img)
#图像处理
kernels = [(u"低通滤波器", np.array([[1, 1, 1], [1, 2, 1], [1, 1, 1]])*0.1),
           (u"高通滤波器", np.array([[0.0, -1, 0],[-1, 5, -1],[0, -1, 0]])),
           (u"边缘检测", np.array([[-1.0, -1, -1],[-1, 8, -1],[-1, -1, -1]]))]
index = 0
fig, axes = pl.subplots(1, 3, figsize=(12, 4.3))


#print(img.dtype)
#print(img.shape)
#print(img)
#
#while(1):
#  k = cv2.waitKey(27)
#  if k== 27:
#      break
#  elif k==-1:
#      continue
#  else:
#      print(k)

#图像保存
#for quality in [90,60,30]:
#    cv2.imwrite("lena_q{:02d}.jpg".format(quality),img,[cv2.IMWRITE_JPEG_CHROMA_QUALITY,quality])
#    

    
    
    
    
    
    
    
    