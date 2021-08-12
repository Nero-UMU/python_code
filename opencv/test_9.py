import cv2
import numpy

circle = cv2.imread('circle.jpg')
kernel = numpy.ones((30, 30))
new_circle = cv2.erode(circle, kernel, iterations=2)
res = numpy.hstack((circle, new_circle))
cv2.imshow('different', res)
cv2.waitKey(0)