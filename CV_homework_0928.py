# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 12:52
# @Author  : Aries
# @Site    : 
# @File    : CV_homework_0928.py
# @Software: PyCharm
import cv2
import numpy as np

#Check if image can be displayed properly
img = cv2.imread('../Beauty.jpg',1)
cv2.imshow('Beauty', img)
key = cv2.waitKey()
if key == 27:
     cv2.destroyAllWindows()

#Color change to make blue color more blue and red color more red.
B,G,R = cv2.split(img)
B[B<=180] = B[B<=180] + 50
B[B>180] = 255
R[R<=180] = R[R<=180] + 50
R[R>180] = 255
img_new = cv2.merge([B,G,R])

#Image crop
x,y,z = img_new.shape
img_new= img_new[int(x*0.1):x,int(y*0.2):y]

# Image rotation first
M = cv2.getRotationMatrix2D((img_new.shape[1]*0.4,img_new.shape[0]*0.2),45,1.5)
img_rotate = cv2.warpAffine(img_new,M,(img_new.shape[1],img.shape[0]))
cv2.imshow('rotated',img_rotate)
cv2.waitKey(0)

#Image perspective transform
x,y,z=img_rotate.shape
pts1 = np.float32([[0,0],[x,0],[0,y],[x,y]] )
pts2 = np.float32([[0,0],[800,0],[0,600],[800,600]])
M_warp = cv2.getPerspectiveTransform(pts1,pts2)
img_warp = cv2.warpPerspective(img_rotate,M_warp,(800,600))
cv2.imshow('Pts',img_warp)
cv2.waitKey(0)