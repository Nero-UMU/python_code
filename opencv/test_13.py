import cv2
import numpy


fish = cv2.imread('salty_fish.jpg')
kernel = numpy.ones((10, 10))
top_hat = cv2.morphologyEx(fish, cv2.MORPH_TOPHAT, kernel, iterations=1)
black_hat = cv2.morphologyEx(fish, cv2.MORPH_BLACKHAT, kernel, iterations=1)
cv2.imshow('fish', fish)
cv2.imshow('top_hat', top_hat)
cv2.imshow('black_hat', black_hat)
cv2.waitKey(0)
