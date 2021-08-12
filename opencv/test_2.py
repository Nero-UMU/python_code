import cv2


vc = cv2.VideoCapture('cat_video.mp4') # 打开一个视屏文件
if vc.isOpened(): # 检测文件是否打开
    can_open, frame = vc.read() # read()会返回两个值，第一个是布尔类型的值，若正确读取帧则返回True，第二个值是每一帧的图像，是个三维矩阵
else:
    can_open = False

while can_open: # 建立循环，遍历每一帧
    ret, frame = vc.read() # read()读取第一帧后再次读取会跳到第二帧，此处用frame获取这一帧
    if frame is None: # 若读取到最后一帧，则结束循环
        break
    if ret == True: # 视频正确打开时执行
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 将每一帧转换为灰度图像
        cv2.imshow('awsl', gray) # 展示每一帧，窗体取名awsl

        # waitKey()在没有任何键盘输入的情况下正常执行返回数值-1，其补码为1111 1111，当有键盘输入时，返回键盘输入的值的ASCII码
        # &符号表示按位相与，键盘输入一个值后与0xFF（1111 1111）相与的返回值是其ASCII码的值
        # esc的ASCII码为27，故键盘按下esc键后会停止播放视频
    if cv2.waitKey(1) & 0xFF == 27:
        break
print(gray)

vc.release()
cv2.destroyAllWindows()
