# -*- coding: utf-8 -*-
# @Author: piyush
# @Date:   2020-04-10 14:55:45
# @Last Modified by:   piyush
# @Last Modified time: 2020-04-10 16:16:42




# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)

# while(True):
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()




import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)

# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('videos/output.mp4',fourcc, 20.0, (640,480))

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret==True:
#         frame = cv2.flip(frame,0)

#         # write the flipped frame
#         out.write(frame)

#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break

# cap.release()
# out.release()
# cv2.destroyAllWindows()