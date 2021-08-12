import cv2


cat = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
cat = cv2.resize(cat, (500, 500))
ret, thresh1 = cv2.threshold(cat, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(cat, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(cat, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(cat, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(cat, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('cat', cat)
cv2.imshow('THRESH_BINARY', thresh1)
cv2.imshow('THRESH_BINARY_INV', thresh2)
cv2.imshow('THRESH_TRUNC', thresh3)
cv2.imshow('THRESH_TOZERO', thresh4)
cv2.imshow('THRESH_TOZERO_INV', thresh5)


cv2.waitKey(0)