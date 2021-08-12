import cv2


cat = cv2.imread('cat.jpg')

cat_b = cat.copy()
cat_b[:, :, 1] = 0
cat_b[:, :, 2] = 0

cv2.imshow('cat_blue', cat_b)
cv2.waitKey(0)

