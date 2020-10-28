# -*- coding: utf-8 -*-
# @Author: piyush
# @Date:   2020-04-10 16:25:59
# @Last Modified by:   piyush
# @Last Modified time: 2020-04-10 16:28:07


import cv2
import numpy as np

# cap = cv2.VideoCapture(0)

# while(1):

#     _, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#     lower_red = np.array([30,150,50])
#     upper_red = np.array([255,255,180])
    
#     mask = cv2.inRange(hsv, lower_red, upper_red)
#     res = cv2.bitwise_and(frame,frame, mask= mask)

#     kernel = np.ones((5,5),np.uint8)
#     erosion = cv2.erode(mask,kernel,iterations = 1)
#     dilation = cv2.dilate(mask,kernel,iterations = 1)

#     cv2.imshow('Original',frame)
#     cv2.imshow('Mask',mask)
#     cv2.imshow('Erosion',erosion)
#     cv2.imshow('Dilation',dilation)

#     # k = cv2.waitKey(5) & 0xFF
#     # if k == 27:
#     #     break

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()
# cap.release()
# 




cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    kernel = np.ones((5,5),np.uint8)
    
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('Original',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Opening',opening)
    cv2.imshow('Closing',closing)

    # k = cv2.waitKey(5) & 0xFF
    # if k == 27:
    #     break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()