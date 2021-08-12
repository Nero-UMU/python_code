import cv2
import numpy


kernel = numpy.ones((10, 10))
circle = cv2.imread('circle.jpg')
gradient = cv2.morphologyEx(circle, cv2.MORPH_GRADIENT, kernel, iterations=1)
cv2.imshow('gradient', gradient)
cv2.imshow('circle', circle)
cv2.waitKey(0)