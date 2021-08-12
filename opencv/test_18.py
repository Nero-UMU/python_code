import cv2


lenna = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
median = cv2.medianBlur(lenna, 7)
cv2.imshow('lenna', lenna)
cv2.imshow('median', median)
cv2.waitKey(0)