'''
功能：计算斐波那契数列（使用递归计算）
日期：2021.3.22
'''

result = 0
def recursive( x ):
    if x <= 2:
        return 1
    else:
        result = recursive( x - 1 ) + recursive( x - 2 )
    return result
number = input('请输入一个整数：')
number = eval( number )
end = recursive( number )
print('第%d个斐波那契数列是%d'%(number, end))
