need = []
def fibonacci(first, second, i, number):
    third = first + second
    if i != number:
        fibonacci(second, third, i + 1, number)
        need.append(third)
    return need


if __name__ == '__main__':
    number = int(input('请输入要输出的那一位斐波那契数'))
    answer = fibonacci(0, 1, 1, number)
    print('结果为' + str(answer[0]))