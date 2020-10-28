# -*- coding: utf-8 -*-
# @Author: piyush
# @Date:   2020-04-10 14:53:03
# @Last Modified by:   piyush
# @Last Modified time: 2020-04-10 14:54:03


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/watch.jpg',cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()

