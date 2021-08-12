"""
程序：一个猜数字的小游戏
时间：2021.3.20
版本：2.0
功能：
v1.0：仅支持简单的猜数字的小游戏，数字由计算机随机设置
v2.0:允许用户退出游戏并发送退出成功消息
"""


import random

# 设置随机答案
answer = random.randint(1, 10)

# 输入猜测的答案
print('I want to play a game with you.')
select = input('Guess me what number I am thinking(you have three chances),if you don\'t want to play with me, please input "stop":')
chance = 3
while select != 'stop':
    guess = eval(select)

    # 开始判断是否输入的数字与答案匹配，并告知错误后偏高还是偏低
    if answer == guess:
        print('WOW excellent!You know what I \'m thinking!!!')
        break

    else:
        print('NO NO NO ,your answer is false')
        if guess > answer:
            print('I can tell you that your answer is higher than my guess.')
        else:
            print('I can tell you that your answer is lower than my guess.')

    chance -=1
    if chance == 0:
        print('Sorry, you have failed ^_^')
        break
    select = input('\nYou haven\'t guess my number, do you want to play with one more time?If you don\'t, please input "stop":')

else:
    print('The game has stopped, hop you can play with me another time!')

