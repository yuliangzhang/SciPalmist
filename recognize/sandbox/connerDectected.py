import numpy as np
import cv2
from matplotlib import pyplot as plt

#img = cv2.imread('input.jpeg')
#img = cv2.imread('input_1.png')
#img = cv2.imread('input_2.jpeg')
#img = cv2.imread('input_3.jpg')
img = cv2.imread('input_4.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray,35,0.01,10)
cv2.imwrite("output.png", gray)
corners = np.int0(corners)

print(len(corners))
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),4,(0,0,255),-1)
#cv2.imwrite("output.png", img)
#plt.imshow(img),plt.show()
