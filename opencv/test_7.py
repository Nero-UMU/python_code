import cv2


cat = cv2.imread('cat.jpg')
cat = cv2.resize(cat, (500, 500))
blur = cv2.blur(cat, (10, 10))

cv2.imshow('cat', cat)
cv2.imshow('blur', blur)
cv2.waitKey(0)
