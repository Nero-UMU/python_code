'''
作者：魏嘉鲲
版本：1.0
日期：2021.5.14
功能：小球碰撞游戏
'''

from tkinter import *
import random
import time


class Ball:
    # 构造方法
    def __init__(self, canvas, paddle, color):
        # canvas表示画布，也就是最外层的窗体
        self.canvas = canvas
        self.paddle = paddle

        # 画一个椭圆并用color涂色，保存其id
        # 小球的初始化
        self.id = canvas.create_oval(10, 10, 35, 35, fill=color)
        # tkinter.create_oval方法可以构造一个椭圆，前四个参数为x, y, a, b；x,y是椭圆的坐标，a,b是椭圆的长轴和短轴

        # 把小球移动到了画布的指定位置
        self.canvas.move(self.id, 245, 100)
        start = [-3, -2, -1, 1, 2, 3]
        # 函数shuffle()功能：随机化列表
        random.shuffle(start)
        self.x = start[0]
        self.y = -3

        # 函数winfo_height()可以获取当前窗体的高度
        # 函数winfo_width()可以获取当前窗体的宽度
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw_ball(self):
        self.canvas.move(self.id, self.x, self.y)
        # coords() 函数可以记录小球的当前坐标（左上角和右上角坐标）
        # pos是一个列表，pos[0]对应小球左上角的x坐标，pos[1]对应小球左上角的y,pos[2]对应小球右上角的x,pos[3]对应小球右上角的y
        # pod是一个列表，pod[0]对应挡板左上角的x坐标，pod[1]对应挡板左上角的y,pod[2]对应挡板右上角的x,pod[3]对应挡板右上角的y
        pos = self.canvas.coords(self.id)
        pad = self.canvas.coords(self.paddle.id)
        # 判断小球是否出界，要求小球不能超出窗口
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height or (pos[3] >= pad[1] and pos[2] >= pad[0] and pos[2] <= pad[2]):
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:
    # 构造方法
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.canvas_width = self.canvas.winfo_width()
        self.l = 0
        self.r = 0

    def draw_rectangle(self):
        # # pos是一个列表，pos[0]对应挡板左上角的x坐标，pos[1]对应挡板左上角的y,pos[2]对应挡板右上角的x,pos[3]对应挡板右上角的y
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.l = 0
        if pos[2] >= self.canvas_width:
            self.r = 0

    # 两个重要操作，左移右移
    def turn_left(self, event):
        self.canvas.move(self.id, self.l, 0)
        self.l = -20

    def turn_right(self, event):
        self.canvas.move(self.id, self.r, 0)
        self.r = 20


# 完成类的实例化，窗体类，挡板类，小球类
tk = Tk()
# 设置窗体的标题
tk.title('Ball Game')
# 设置窗体的大小不可调整，即窗口大小固定
tk.resizable(0, 0)
# 设置窗口总是显示在最前端，即置顶功能
tk.wm_attributes('-topmost', 1)
# 完成画布的绘制，将画好的画布装入窗体中，后两个参数去掉边框
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

# 绑定键盘的方向键
canvas.bind_all('<KeyPress-Left>', paddle.turn_left)
canvas.bind_all('<KeyPress-Right>', paddle.turn_right)

# 程序处于一直运行状态
while True:
    ball.draw_ball()
    paddle.draw_rectangle()
    # 快速重画屏幕
    tk.update_idletasks()
    tk.update()
    time.sleep(0.001)
