'''
作者：魏嘉鲲
日期：2021.6.20
版本：4.0
功能：
1.0:爬取网站的信息并筛选数据
2.0:生成数据文件，并使程序循环运行获得大量数据文件
3.0:对数据文件进行进一步的分析，并使数据可视化
4.0:修改网站URL的爬取方式，增加数据可视化的显示方式
'''



import requests
import bs4
import csv
import time
import random
import matplotlib.pyplot as plt
from numpy import *
import turtle


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def draw_line(draw):
    if draw:
        turtle.forward(15)
        turtle.pendown()
        turtle.forward(100)
        turtle.penup()
        turtle.fd(15)
        turtle.right(90)
    else:
        turtle.forward(15)
        turtle.forward(100)
        turtle.fd(15)
        turtle.right(90)


def draw_number(num):
    if num in [2, 3, 4, 5, 6, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if num in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if num in [0, 2, 3, 5, 6, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if num in [0, 2, 6, 8]:
        draw_line(True)
    else:
        draw_line(False)

    turtle.left(90)

    if num in [0, 4, 5, 6, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if num in [0, 2, 3, 5, 6, 7, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if num in [0, 1, 2, 3, 4, 7, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)

    turtle.setheading(0)
    turtle.forward(100)

def draw_rate(rate):
    turtle.speed(0)
    turtle.setup(1500, 700)
    turtle.penup()
    turtle.goto(-700, 300)
    turtle.pendown()
    turtle.pencolor('red')
    turtle.write('您考入该大学的概率为:', font=("楷体", 16))
    turtle.penup()
    turtle.goto(-700, 0)
    turtle.pensize(15)
    turtle.pencolor('yellow')

    number = str(rate * 1000000)[:4]
    for i in number:
        draw_number(int(i))

    turtle.penup()
    turtle.goto(-300, -120)
    turtle.pendown()
    turtle.pencolor('blue')
    turtle.pensize(20)
    turtle.fd(1)
    turtle.penup()
    turtle.goto(250, -120)
    turtle.pencolor('black')
    turtle.pendown()
    turtle.left(60)
    turtle.fd(300)
    turtle.penup()
    turtle.goto(270, 100)
    turtle.pensize(10)
    turtle.pendown()
    turtle.circle(radius=20, extent=360)
    turtle.penup()
    turtle.goto(400, -100)
    turtle.pendown()
    turtle.circle(radius=20, extent=360)
    turtle.mainloop()



# 通过打开文件查询学校的id再爬取网站的函数
def get_massage(name):
    school_id = open('学校对应关系.csv', encoding='utf-8')
    name_id = school_id.read().split('\n')
    for each in name_id:
        school, id = each.split(',')
        if school == name:
            break

    url = 'http://college.gaokao.com/school/' + str(id) + '/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
    f = requests.get(url=url, headers=headers)
    return f


def spider(school_name):
    f = get_massage(school_name)

    # 当http的状态码为200才进行爬取工作
    if f.status_code == 200:
        # 利用bs4模块打开爬取到的数据
        passage_bs = bs4.BeautifulSoup(f.text, features='lxml')
        each_massage = passage_bs.find('table', bgcolor="#E1E1E1")

        each_massage_szw = each_massage.find_all('tr', class_= 'szw')
        each_massage_sz = each_massage.find_all('tr', class_='sz')

        # 学校名字
        school_name = passage_bs.find('font').text

        # 获取需要获得的数据
        line_szw = []
        line_sz = []
        for each_line in each_massage_szw:
            line_szw.append(each_line.find_all('td')[:3])
        for each_line in each_massage_sz:
            line_sz.append(each_line.find_all('td')[:3])

        year_grade = []
        for i in range(len(each_massage_sz)):
            for x in range(3):
                year_grade.append(line_szw[i][x].text)
            for y in range(3):
                year_grade.append(line_sz[i][y].text)



        # 将所有每一年的最低分和最高分为一个单位形成一个含有每一年最低分和最高分的列表
        each_year_grade = []
        flag = 3
        for i in range(0, len(year_grade), 3):
            each_year_grade.append(year_grade[i:flag])
            flag += 3

        # 将没有数据的成绩改为750
        for each in range(len(each_year_grade)):
            for i in range(len(each_year_grade[each])):
                if each_year_grade[each][i] == '------':
                    each_year_grade[each][i] = 750

        # 生成CSV文件
        head = ['年份', '最低分', '最高分']
        each_year_grade.insert(0, head)

        file_name = school_name + '.csv'
        file = open(file_name, 'w', newline='', encoding='utf-8')
        writer = csv.writer(file)
        for row in each_year_grade:
            writer.writerow(row)
        file.close()

    else:
        print('出问题了o(╥﹏╥)o')
        print(f.status_code)
        return 0
    return 1

def picture(school_name):
    line_year = [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008]
    first_class_line = [535, 522, 527, 503, 529, 540, 526, 517, 547, 531, 515, 518, 512]
    second_class_line = [463, 449, 447, 422, 445, 490, 471, 456, 486, 474, 462, 466, 461]


    file_name = school_name + '.csv'

    data = open(file_name, encoding='utf-8')
    reader = csv.reader(data)

    # 获得csv文件的第一行
    header_row = next(reader)
    years, highs, lows = [], [], []
    for row in reader:
        year = int(row[0])
        high = int(row[2])
        low = int(row[1])
        if year in years:
            continue
        else:
            years.append(year)
            highs.append(high)
            lows.append(low)

    fig = plt.figure(figsize=(15, 7))
    title_name = school_name + '历年分数统计图'
    plt.title(title_name, fontsize=24)

    low_line_name = school_name + '最低分'
    high_line_name = school_name + '最高分'
    first_class_line_name = '一本线'
    second_class_line_name = '二本线'

    # 生成该学校历年的最高分和最低分折线以及一二本分数线
    plt.plot(years, highs, label = high_line_name, color='red')
    plt.plot(years, lows, label = low_line_name, color='blue')
    plt.plot(line_year, first_class_line, label = first_class_line_name, color='black')
    plt.plot(line_year, second_class_line, label = second_class_line_name, color='green')
    plt.fill_between(years, highs, lows, facecolor='yellow', alpha=0.2)
    plt.fill_between(line_year, first_class_line, second_class_line, facecolor='purple', alpha=0.2)

    # 设置x,y轴所代表的意思
    plt.xlabel('年份')
    plt.ylabel('分数')
    plt.legend()

    seconds = random.randint(4, 8)
    print('请稍等', end='')
    for i in range(seconds):
        print('.', end='')
        time.sleep(1)
    # 保存并展示图片
    save_name = school_name + '分数折线统计图.png'
    plt.savefig(save_name)
    plt.show()


def calculate(school, grade):
    first_class_line = [535, 522, 527, 503, 529, 540, 526, 517, 547, 531, 515, 518, 512]
    second_class_line = [463, 449, 447, 422, 445, 490, 471, 456, 486, 474, 462, 466, 461]

    file_name = school + '.csv'

    data = open(file_name, encoding='utf-8')
    reader = csv.reader(data)

    # 获得csv文件的第一行
    header_row = next(reader)
    years, highs, lows = [], [], []
    for row in reader:
        year = int(row[0])
        high = int(row[2])
        low = int(row[1])
        if year in years:
            continue
        else:
            highs.append(high)
            lows.append(low)

    ave_first = int(mean(first_class_line))
    ave_second = int(mean(second_class_line))
    ave_high = int(mean(highs))
    ave_low = int(mean(lows))

    surprise = random.uniform(0.5, 0.9)
    rate = ((4 * int(grade))/(ave_low + ave_high + ave_second + ave_first)) * surprise
    if rate >= 1:
        rate = 1
    return rate


def main():
    print('==================================')
    print('开始爬取数据请输入start')
    print('退出程序请输入quit')
    print('==================================')
    command = input('我要做:')
    if command == 'start':
        school_name = input('请输入学校的名字:')
        if spider(school_name) == 1:
            picture(school_name)
            grade = input('\n请输入您今年的成绩:')

            rate = calculate(school_name, grade)
            draw_rate(rate)

    if command == 'quit':
        pass

if __name__ == '__main__':
    main()

