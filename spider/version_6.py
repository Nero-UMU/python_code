import bs4
from bs4 import BeautifulSoup
import requests
import csv

def main():
    province_pinyin = input('请输入省份的拼音')
    city_pinyin = input('请输入城市的拼音')
    url_weather = 'https://tianqi.8684.cn/' + province_pinyin + '_' + city_pinyin # 城市天气的URL
    url_air_quality = 'https://tianqi.8684.cn/air_' + province_pinyin + '_' + city_pinyin  # 城市空气质量URL

    weather = requests.get(url_weather)
    weather.encoding = 'utf-8'
    weather_bs = BeautifulSoup(weather.text, features='lxml')
    city_name = weather_bs.find('p', class_ = 'title').text # 城市名字
    print(city_name)

    city_weather_15 = weather_bs.find('ol', class_ = 'day-15')

    each_day_weather = city_weather_15.find_all('div', class_ = 'info')
    date = city_weather_15.find_all('div', class_ = 'date')

    each_date = []
    day_weather = []

    # 日期的列表
    for i in date:
        i_date = i.text
        each_date.append(i_date)
    # 天气的列表
    for each in each_day_weather:
        new_each = ','.join(each.text.split())
        day_weather.append(new_each)

    date_weather = [] # 日期与天气的列表
    for i in range(15):
        new_data = each_date[i] + ',' + day_weather[i]
        date_weather.append(new_data)

    # 生成日期和天气的csv文件
    head = ['日期', '气温', '白昼', '天气', '白昼', '天气', '风向']
    lines = []
    lines.append(head)
    for line in date_weather:
        lines.append(list(line.split(',')))
    file_name = city_name + '.csv'
    f = open(file_name, mode='w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for row in lines:
        writer.writerow(row)
    f.close()

    air_quality = requests.get(url_air_quality)
    air_quality.encoding = 'utf-8'
    quality_bs = bs4.BeautifulSoup(air_quality.text, features='lxml')
    quality = quality_bs.find('div', class_ = 'score air-color level-2')
    if quality == None:
        print('该城市没有天气质量检查')
    else:
        print(quality.text)

if __name__ == '__main__':
    main()

