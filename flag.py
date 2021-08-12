import cv2


img = cv2.imread('fivestar.jpeg')
new = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(new, 200, 255, cv2.THRESH_BINARY)

cv2.imshow('flag', thresh)
cv2.waitKey(0)
cv2.imwrite('ok.jpg', thresh)