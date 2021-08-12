'''
功能：计算斐波那契数列（使用迭代计算）
日期：2021.3.22
'''

number = eval(input("请输入一个整数："))
n1 = 1
n2 = 1
n3 = 1
if number <= 2:
    print('第%d个斐波那契数是1'%number)
else:
    while number > 2:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        number -=1
    print("第%d个斐波那契数是%d"%(number, n3))
