import cv2


lenna = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
lenna = cv2.resize(lenna, (600, 600))
lenna = cv2.GaussianBlur(lenna, (5, 5), 8)
lenna_1 = cv2.Canny(lenna, 80, 150)
cv2.imshow('lenna_1', lenna_1)
cv2.imshow('lenna', lenna)
cv2.waitKey(0)

