import cv2


squre = cv2.imread('squre.png')
gray = cv2.cvtColor(squre, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
new_squre = squre.copy()
final = cv2.drawContours(new_squre, contours, -1, (255,0,0), 2)
cv2.imshow('final', final)
cv2.imshow('squre', squre)
cv2.waitKey(0)

x = 0
for i in contours:
    cnt = i
    print(cv2.contourArea(cnt))
    x += 1


