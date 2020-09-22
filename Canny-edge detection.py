#noise reduction
#gradient calculation
#non-maximum suppression
#double threshold
#edge tracking by hysteresis

import cv2
from matplotlib import pyplot as plt



img =cv2.imread('messi5.jpg',0)
canny =cv2.Canny(img,100,200)

titles=['messi','canny']
images =[img,canny]

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
