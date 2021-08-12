import cv2

img = cv2.imread('cat.jpg')
img = cv2.resize(img, (500, 500))
top_size, bottom_size, left_size, right_size = [50, 50, 50, 50]
show = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP, value= 0)
gray = cv2.cvtColor(show, cv2.COLOR_BGR2GRAY)
cv2.imshow('neko', gray)
cv2.waitKey(0)

