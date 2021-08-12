import requests
import bs4
import csv


head = []
for number in range(2665, 2668):
    url = 'http://college.gaokao.com/school/' + str(number) + '/'
    #添加头部，伪装浏览器，字典格式
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
    #增加headers参数
    response = requests.get(url=url, headers=headers)

    if response.status_code != 200:
        break

    soup = bs4.BeautifulSoup(response.text, features='lxml')
    school_name = soup.find('h2').text[14:-19]

    new_list = [school_name, number]
    head.append(new_list)


file = open('学校对应关系.csv', 'a', newline='', encoding='utf-8')
writer = csv.writer(file)
for row in head:
    writer.writerow(row)
file.close()

