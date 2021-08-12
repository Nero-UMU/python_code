import cv2
import numpy


# 定义一个函数可以直接展示图片
def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 读取模板图像
number = cv2.imread('number.png')
# cv_show('number', number)
List = []
# 图片转灰度图
gray = cv2.cvtColor(number, cv2.COLOR_BGR2GRAY)
# cv_show('gray', gray)

# 图像转为二值图像
ret, gray = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
# cv_show('gray', gray)

# 使用findContours获得轮廓，RETR_EXTERNAL获得图像的外轮廓，CHAIN_APPROX_SIMPLE以保留坐标点的形式保留轮廓
contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

each_x = []
new_contours = []
for each in contours:
    x, y, w, h = cv2.boundingRect(each)
    each_x.append(x)

# boundingBoxers = sorted(zip)
cnt = contours[0]
number_new = number.copy()
# cv2.drawContours(number_new, contours, 5, (0, 0, 255), 2)
cv2.drawContours(number_new, [cnt], 0, (0, 0, 255), 2)
cv2.imshow('new', number_new)
cv2.waitKey(0)

