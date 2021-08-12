import requests
import bs4
import csv
import time
import random


def spider():
    for number in range(1, 100):
        url = 'http://college.gaokao.com/school/' + str(number) + '/'
        # 添加头部，伪装浏览器，字典格式
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
        # 增加headers参数
        f = requests.get(url=url, headers=headers)

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

            # 为防止爬虫过快导致被封ip地址，故每爬完一个网站就等待0-0.5s
            wait_time = random.randint(0, 1)
            time.sleep(wait_time)
        else:
            continue


def main():
    print('==================================================================')
    print('开始爬取数据请输入spider')
    print('生成数据视图请输入picture')
    print('==================================================================')
    command = input()
    if command == 'spider':
        spider()
    if command == 'picture':
        pass


if __name__ == '__main__':
    main()

