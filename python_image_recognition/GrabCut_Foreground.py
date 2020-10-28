# -*- coding: utf-8 -*-
# @Author: piyush
# @Date:   2020-04-10 16:44:59
# @Last Modified by:   piyush
# @Last Modified time: 2020-04-10 17:00:14



import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('images/Piyush_Sinha.jpeg')

# img = cv2.imread('images/opencv-python-foreground-extraction-tutorial.jpg')

mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (370,100,300,400)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()