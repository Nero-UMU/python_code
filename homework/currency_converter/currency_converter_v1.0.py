'''
作者：魏嘉鲲
日期：2021.3.18
版本：1.0
功能：汇率兑换，输入人民币，得到对应的美元金额
'''

# 美元兑人民币汇率
USD_VS_RMB = 6.77

# 输入人民币的金额
# eval（）函数可以将其他类型转换为数值类型

rmb = input("请输入要兑换的人民币金额：")
rmb_value = eval(rmb)

# 进行人民币兑美元金额
usd = rmb_value / USD_VS_RMB

# 输出人民币兑换美元的金额
print(rmb, "元人民币可兑换", usd, "美元")
