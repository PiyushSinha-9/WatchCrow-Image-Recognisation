# -*- coding: utf-8 -*-
# @Author: piyush
# @Date:   2020-04-10 16:05:42
# @Last Modified by:   piyush
# @Last Modified time: 2020-04-10 16:11:12


# import cv2
# import numpy as np

# img = cv2.imread('images/bookpage.jpg')
# retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
# cv2.imshow('original',img)
# cv2.imshow('threshold',threshold)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np


img = cv2.imread('images/bookpage.jpg')
# retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('original',img)
cv2.imshow('Adaptive threshold',th)
cv2.waitKey(0)
cv2.destroyAllWindows()