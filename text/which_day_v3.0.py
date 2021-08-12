'''
作者：魏嘉鲲
日期：2021.4.2
版本：3.0
功能：v1.0 输入某年某月，判断它是这一年的第几天
v2.0 输入某年某月，利用列表判断它是这一年的第几天
v3.0 利用集合（分大小月的集合）来计算这是这一年的第几天
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

    month_30days_set = [4, 6, 9, 11]
    month_31days_set = [1, 3, 5, 7, 8, 10, 12]

    days = 0
    for each_month in range(1, month):
        if each_month in month_31days_set:
            days += 31
        elif each_month in month_30days_set:
            days += 30
        else:
            days += 28

    days = days + day

    if is_leap_year( year ) and month > 2 :
        days += 1

    print('这一天是{}年的第{}天'.format(year, days))


if __name__ == '__main__':
    main()
