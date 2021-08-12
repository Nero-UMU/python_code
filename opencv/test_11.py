import cv2
import numpy


fish = cv2.imread('salty_fish.jpg')
kernel = numpy.ones((50, 50))
open_fish = cv2.morphologyEx(fish, cv2.MORPH_OPEN, kernel, iterations=1)
close_fish = cv2.morphologyEx(fish, cv2.MORPH_CLOSE, kernel, iterations=1)
cv2.imshow('fish', fish)
cv2.imshow('open_fish', open_fish)
cv2.imshow('close_fish', close_fish)
cv2.waitKey(0)