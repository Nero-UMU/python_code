'''
作者：魏嘉鲲
日期：2021.5.27
版本：2.0
功能：读取已经存在的JSON文件，并获取前5名，存入新的JSON文件中
'''


import json


def main():
    # 1 读取JSON文件
    filepath = input('请输入JSON文件名：')
    f = open(filepath, mode='r', encoding='utf-8')
    # json.load()的含义：解码json文件
    city_list = json.load(f)
    # 2 对数据做处理，排序截取前5名
    city_list.sort(key=lambda city:city['aqi'])
    top5 = city_list[:5]
    # 3 将得到的WIS前5名数据写入一个新的JSON文件中
    f = open('top_aqi.json', mode='w', encoding='utf-8')
    json.dump(top5, f, ensure_ascii=False, indent=1)
    f.close()

if __name__ == '__main__':
    main()
