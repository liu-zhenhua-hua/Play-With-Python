

import cv2
import PyQt5.QtCore
import cv2


img = cv2.imread('lena.jpg',1)

print(img)
cv2.imshow('image',img)
cv2.waitKey(10000)
cv2.destroyWindow('image')