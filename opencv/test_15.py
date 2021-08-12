import cv2


cat = cv2.imread('cat.jpg')
cat_1 = cv2.pyrUp(cat)
cat_2 = cv2.pyrDown(cat_1)
new_cat = cat - cat_2
cv2.imshow('new_cat',  new_cat)
cv2.waitKey(0)
