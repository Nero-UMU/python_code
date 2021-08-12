"""
程序：一个猜数字的小游戏
时间：2021.3.18
版本：1.0
功能：v1.0：仅支持简单的猜数字的小游戏，数字由计算机随机设置
"""


import random

# 设置随机数
answer = random.randint(1, 10)

# 输入猜测的答案
print('I want to play a game with you.')
guess = int(input('Guess me what number I am thinking(you have three chances):'))

# 开始判断是否输入的数字与答案匹配，并告知错误后偏高还是偏低
number = 1
if answer == guess:
    print('WOW excellent!You know what I \'m thinking!!!')
    number = 1000
else:
    print('NO NO NO ,your answer is false')
    print('And you have 2 chances')
    if guess > answer:
        print('I can tell you that your answer is higher than my guess.')
    else:
        print('I can tell you that your answer is lower than my guess.')

# 进入循环，每次游戏共有三次机会
while number < 3:
    guess = int(input('please input a new number:'))
    if answer == guess:
        print('WOW excellent!You know what I \'m thinking!!!')
        number = 1000
    else:
        print('NO NO NO ,your answer is false')
        print('And you have %d chances' % (2 - number))
        if guess > answer:
            print('I can tell you that your answer is higher than my guess.')
        else:
            print('I can tell you that your answer is lower than my guess.')
    number += 1
    if number == 3:
        print('sorry ,you have failed ^_^')

