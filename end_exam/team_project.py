import requests
import bs4
import csv


def main():
    # school_url = 'http://college.gaokao.com/school/2/'
    # f = requests.get(url=school_url)
    f = open('test_file.txt')

    # 利用bs4模块打开爬取到的数据
    passage_bs = bs4.BeautifulSoup(f, features='lxml')
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





if __name__ == '__main__':
    main()

