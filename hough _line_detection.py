import cv2
import numpy as np

img=cv2.imread('sudoku.png')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,200,apertureSize=3)
cv2.imshow('canny',edges)

lines =cv2.HoughLines(edges,1,np.pi/180,250)


for line in lines:
    rho,theta= line[0]
    x0= rho * np.cos(theta)
    y0= rho *np .sin(theta)

    x1=int(x0+1000*(-np.sin(theta)))
    y1=int(y0+1000*(np.cos(theta)))

    x2 = int(x0 - 1000 * (-np.sin(theta)))
    y2 = int(y0 - 1000 * (np.cos(theta)))
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()