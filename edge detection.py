import cv2
import numpy as np

import sys
import video
try:
    fn = sys.argv[1]
except IndexError:
    fn = 0
cap = video.create_capture(fn)


while(True):
 _,img =cap.read()

 gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 blur = cv2.medianBlur(gray,5)
 canny = cv2.Canny(blur,200,300,apertureSize= 3)
 sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
 sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
 sobelX = np.uint8(np.absolute(sobelX))
 sobelY = np.uint8(np.absolute(sobelY))
 sobelCombined = cv2.bitwise_or(sobelY, sobelX)
 cv2.imshow('camera', canny)

 img = cv2.medianBlur(img, 3)
 gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
 lap = cv2.Laplacian(gray, cv2.CV_8U, ksize=5)
 channels = cv2.split(img)
 normalizedInversealpha = (1 / 255) * (255 - gray)
 for channel in channels:
     channel[:] = channel * normalizedInversealpha

 cv2.merge(channels, img)





 cv2.imshow('src',img)


 if  cv2.waitKey(1)==27:
     break
cap.release()
cv2.destroyAllWindows()



