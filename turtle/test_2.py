'''
版本：v1.0
版泵功能：
v1.0 利用海龟作图体系绘画 0 ~ 9 十个数字
v2.0 利用time模块获得准确时间，并用海龟作图出来
'''


import turtle
import time


def get_time():
    t1 = time.asctime()
    t2 = t1.split(' ')
    t3 = t2[4].split(':')
    t4 = ''
    for i in range(3):
        t4 += t3[i]
    return t4


def draw_line(draw):
    if draw:
        turtle.forward(15)
        turtle.pendown()
        turtle.forward(100)
        turtle.penup()
        turtle.fd(15)
        turtle.right(90)
    else:
        turtle.forward(15)
        turtle.forward(100)
        turtle.fd(15)
        turtle.right(90)


def draw_number(num):
    if num in [2, 3, 4, 5, 6, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if num in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if num in [0, 2, 3, 5, 6, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if num in [0, 2, 6, 8]:
        draw_line(True)
    else:
        draw_line(False)

    turtle.left(90)

    if num in [0, 4, 5, 6, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if num in [0, 2, 3, 5, 6, 7, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if num in [0, 1, 2, 3, 4, 7, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)

    turtle.setheading(0)
    turtle.forward(100)


def main():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.setup(1500, 700)
    turtle.penup()
    turtle.goto(-700, 0)
    turtle.pensize(15)
    turtle.pencolor('yellow')

    now_time = get_time()
    for x in range(6):
        draw_number(int(now_time[x]))
        if x == 1:
            turtle.bk(50)
            turtle.write('时', font=('楷体', 30))
            turtle.fd(50)
            turtle.color('green')
        if x == 3:
            turtle.bk(50)
            turtle.write('分', font=('楷体', 30))
            turtle.fd(50)
            turtle.color('blue')
        if x == 5:
            turtle.bk(50)
            turtle.write('秒', font=('楷体', 30))
            turtle.fd(50)



if __name__ == '__main__':
    main()

turtle.mainloop()