'''
作者：魏嘉鲲
日期：2021.4.2
版本：2.0
功能：v1.0 输入某年某月，判断它是这一年的第几天
v2.0 输入某年某月，利用列表判断它是这一年的第几天
'''

# 导入datetime模块
import datetime


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


# 主函数
def main():
    # 从键盘获得日期数据
    input_date = input('从键盘输入日期，形式为yyyy/mm/dd:')

    # 将日期数据进行切片，获得年、月、日
    after_day = datetime.datetime.strptime(input_date, '%Y/%m/%d')

    year = after_day.year
    month = after_day.month
    day = after_day.day

    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_list[1] = 29

    days = sum(days_list[:month - 1]) + day

    print('这一天是{}年的第{}天'.format(year, days))


if __name__ == '__main__':
    main()
