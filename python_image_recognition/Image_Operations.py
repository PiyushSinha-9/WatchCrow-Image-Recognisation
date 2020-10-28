# -*- coding: utf-8 -*-
# @Author: piyush
# @Date:   2020-04-10 15:56:34
# @Last Modified by:   piyush
# @Last Modified time: 2020-04-10 16:16:46

import cv2
import numpy as np

img = cv2.imread('images/watch.jpg',cv2.IMREAD_COLOR)


px = img[55,55]

img[55,55] = [255,255,255]


px = img[55,55]
print(px)

px = img[100:150,100:150]
print(px)

img[100:150,100:150] = [255,255,255]

print(img.shape)
print(img.size)
print(img.dtype)

watch_face = img[37:111,107:194]
img[0:74,0:87] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()