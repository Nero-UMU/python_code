'''
作者：魏嘉鲲
日期：2021.5.28
版本：3.0
功能：读取已经存在的JSON文件，并获取前5名，存入新的JSON文件中
读取已经存在的JSON文件，将其转成CSV格式
'''


import json
import csv


def main():
    # 读取JSON文件
    filepath = input('请输入JSON文件名：')
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)

    # 将读取的JSON列表转换成CSV格式
    lines = []
    # 首先进入CSV的应该是表头，也就是JSON中某一个元素额的所有键
    lines.append(list(city_list[0].keys()))

    # 遍历JSON文件，得到每个元素的所有值，依次存入CSV中
    # city表示遍历得到的每一个元素，键:值
    for city in city_list:
        lines.append(list(city.values()))

    # 将得到的CSV格式数据写入到CSV文件中
    f1 = open('top5_aqi.csv', mode='w', encoding='utf-8', newline='')
    # csv.writer()含义：写csv文件， csv.reader含义：读csv文件
    writer = csv.writer(f1)
    # writerow()含义：写一行数据
    for line in lines:
        writer.writerow(line)

    f.close()



if __name__ == '__main__':
    main()
