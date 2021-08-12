'''
版本：v1.0
版泵功能：
v1.0 利用海龟作图体系绘画 0 ~ 9 十个数字
'''


import turtle


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
    turtle.setup(1200, 700)
    turtle.penup()
    turtle.goto(-500, 0)
    turtle.pensize(15)
    turtle.pencolor('yellow')


if __name__ == '__main__':
    main()

turtle.mainloop()