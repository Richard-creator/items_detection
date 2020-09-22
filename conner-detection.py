import cv2
import numpy as np

img =cv2.imread('left01.jpg')

gray =cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#find corner

dst = cv2.cornerHarris(gray,2,3,0.04)# src,neighbor oconsidered means 2*2,size of sobel kernal,free param in equation

#dilate it
dst =cv2.dilate(dst,None)

# mark it
img[dst>0.01*dst.max() ]=[0,255,0]

cv2.imshow('corner',img)

cv2.waitKey(0)
cv2.destroyAllWindows()