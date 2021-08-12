import cv2 # opencv读取的格式是BGR格式


def cv_show(file_name, windows_name): # 定义一个函数，以后可以直接调用显示图片
    img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE) # 使用cv2.imread方法读取文件,第二个参数可选择[cv2.IMREAD_GRAYSCALE(灰度图像），cv2.IMREAD_COLOR（彩色图像）]
    cv2.imshow(windows_name, img) # 显示文件，前面的是窗口的名字，后面的是读取的文件
    cv2.waitKey(0) # 等待时间，毫秒级，0表示任意键终止 1000 = 1s

img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('lol', img)
cv2.waitKey(0)
print(img.shape) # shape返回图像的长和宽，第三个是颜色通道，3表示有三个颜色通道，没有表示是灰度图像

cv2.imwrite('mycat.png', img) # 保存图像

