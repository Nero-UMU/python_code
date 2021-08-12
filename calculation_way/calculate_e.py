import time


def calculate_e(number):
    e = 1
    for i in range(1, number*10000):
        e = e + 1.0 / i ** 2
    return e


def main():
    long = input('需要输出自然底数e的小数点后多少位:')
    time1 = time.time()
    number = calculate_e(int(long))
    time2 = time.time()
    word = '{:.' + long + '}'
    print('小数点后{}位如下:'.format(long) + word.format(number))
    time_long = time2 - time1
    print('用时:{}s'.format(time_long))


if __name__ == '__main__':
    main()