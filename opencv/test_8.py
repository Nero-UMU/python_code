import cv2


dog = cv2.imread('doge.jpg')
dog = cv2.resize(dog, (300, 300))
box = cv2.boxFilter(dog, -1, (3, 3), normalize=False)
gaussian = cv2.GaussianBlur(dog, (5, 7), 2)
cv2.imshow('dog', dog)
cv2.imshow('box', box)
cv2.imshow('gaussian', gaussian)
cv2.waitKey(0)