import matplotlib.pyplot as plt
import cv2
import numpy as np


img = cv2.imread("template.jpg")
mask = np.zeros(img.shape[:2],np.uint8)

bgModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (60, 20, 500, 500)

cv2.grabCut(img,mask,rect,bgModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2)|(mask == 0),0,1).astype("uint8")
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()
