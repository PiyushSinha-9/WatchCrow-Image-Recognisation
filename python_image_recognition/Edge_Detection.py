# -*- coding: utf-8 -*-
# @Author: piyush
# @Date:   2020-04-10 16:29:15
# @Last Modified by:   piyush
# @Last Modified time: 2020-04-10 16:31:20


# import cv2
# import numpy as np

# cap = cv2.VideoCapture(0)

# while(1):

#     # Take each frame
#     _, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#     lower_red = np.array([30,150,50])
#     upper_red = np.array([255,255,180])
    
#     mask = cv2.inRange(hsv, lower_red, upper_red)
#     res = cv2.bitwise_and(frame,frame, mask= mask)

#     laplacian = cv2.Laplacian(frame,cv2.CV_64F)
#     sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
#     sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

#     cv2.imshow('Original',frame)
#     cv2.imshow('Mask',mask)
#     cv2.imshow('laplacian',laplacian)
#     cv2.imshow('sobelx',sobelx)
#     cv2.imshow('sobely',sobely)

#     # k = cv2.waitKey(5) & 0xFF
#     # if k == 27:
#     #     break

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()
# cap.release()


import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('Original',frame)
    edges = cv2.Canny(frame,100,200)
    cv2.imshow('Edges',edges)

    # k = cv2.waitKey(5) & 0xFF
    # if k == 27:
    #     break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
cap.release()