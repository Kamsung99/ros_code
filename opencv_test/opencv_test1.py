import cv2
import numpy as np

print(cv2.__version__)
img = cv2.imread('/home/psh/ros_code/opencv_test/img/face.jpg',cv2.IMREAD_GRAYSCALE)

#transpose
img_flip = cv2.flip(img,0)

#roi
img_rotate= cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('imagewindow1',img)
cv2.imshow('imagewindow2',img_rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
