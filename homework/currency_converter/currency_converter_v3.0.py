'''
作者：魏嘉鲲
时间：2021.3.19
版本：V3.0
功能：v2.0判断输入的货币是人民币还是美元，并输出对应的金额
v3.0:程序的运行次数由用户决定
'''
# 汇率
USD_VS_RMB = 6.77

# 输入带单位的货币金额
money = input('请输入带单位的货币金额（若退出程序，输入Q）：')
while money != 'Q':
    # 获取输入的是人民币还是美元
    # 获取输入的金额数
    money_unit = money[-3:]
    money_value = money[:-3]

    # 判断输入的是美元还是人民币，并输出对应的金额
    # 若输入的是非美元或人民币，则输出无法计算
    if money_unit == "USD":
        rmb = eval(money_value) * USD_VS_RMB
        print(money_value, "美元可兑换的人民币的金额为：", '%.1f' % rmb, '元人民币')
    elif money_unit == 'RMB':
        usd = eval(money_value) / USD_VS_RMB
        print(money_value, '人民币可兑换的美元金额为：', '%.1f' % usd, '美元')
    else:
        print('暂时不支持该货币的兑换^_^')

    # 每完成一次兑换，判断是否需要继续输入
    money = input('是否继续输入带单位的货币金额（若退出程序，输入Q）：')

print('程序已退出！')
