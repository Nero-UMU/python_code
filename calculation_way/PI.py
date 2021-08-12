import time


def calculate_pi(number):
    number_1 = number * 20
    flag = 1
    first = 0
    second = 0
    for i in range(1, number_1, 2):
        first += flag * (1 / (i * (5**i)))
        second += flag * (1 / (i * (239**i)))
        flag *= -1
    sum = 16*(first) - 4*(second)
    return sum


def main():
    long = input('需要输出圆周率小数点后多少位:')
    time1 = time.time()
    number = calculate_pi(int(long))
    time2 = time.time()
    word = '{:.' + long + '}'
    print('小数点后{}位如下:'.format(long) + word.format(number))
    time_long = time2 - time1
    print('用时:{}s'.format(time_long))


if __name__ == '__main__':
    main()