import cv2


lenna = cv2.imread('lenna_color.png')
lenna = cv2.cvtColor(lenna, cv2.COLOR_BGR2GRAY)
lenna_face = cv2.imread('lenna_face.png')
lenna_face = cv2.cvtColor(lenna_face, cv2.COLOR_BGR2GRAY)
lenna_2 = lenna.copy()
res = cv2.matchTemplate(lenna, lenna_face, cv2.TM_SQDIFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = min_loc
bottom_right = (top_left[0] + lenna_face.shape[1], top_left[1] + lenna_face.shape[0])
cv2.rectangle(lenna_2, top_left, bottom_right, (255, 0, 0), 5)
cv2.imshow('lenna', lenna_2)
cv2.waitKey(0)


