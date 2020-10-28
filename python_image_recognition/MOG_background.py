# -*- coding: utf-8 -*-
# @Author: piyush
# @Date:   2020-04-10 17:14:21
# @Last Modified by:   piyush
# @Last Modified time: 2020-04-10 17:15:10


import numpy as np
import cv2

cap = cv2.VideoCapture('videos/people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
 
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)

    
    # k = cv2.waitKey(30) & 0xff
    # if k == 27:
    #     break
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()