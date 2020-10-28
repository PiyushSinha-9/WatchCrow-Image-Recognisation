# -*- coding: utf-8 -*-
# @Author: piyush
# @Date:   2020-04-10 16:00:00
# @Last Modified by:   piyush
# @Last Modified time: 2020-04-10 16:05:00


import cv2
import numpy as np

img1 = cv2.imread('images/3D-Matplotlib.jpg')
img2 = cv2.imread('images/mainlogo.jpg')

rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# adding a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()