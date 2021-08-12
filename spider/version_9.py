import requests
import bs4
import pandas as pd


def main():
    # 读取需要解析的文件
    aqi_data = pd.read_csv('beijing_aqi.csv')
    # print('基本信息显示如下：')
    # print(aqi_data.info())

    # print('数据预览如下')
    # print(aqi_data.head(8))

    # 基本统计
    # print('AQI最大值', aqi_data['aqi'].max())
    # print('AQI最小值', aqi_data['aqi'].min())
    # print('AQI平均值', aqi_data['aqi'].mean())

    # # 获取AQI值最好的前3个监测点
    # top3_point = aqi_data.sort_values(by=['aqi']).head(3)
    # print(top3_point)
    # # 获取AQI值最差的3个监测点
    # bottom3_point = aqi_data.sort_values(by=['aqi']).tail(3)
    # print(bottom3_point)

    # 数据清洗
    # 设置清洗条件
    filter_condition = aqi_data['aqi'] > 50
    clean_data = aqi_data[filter_condition]
    print(clean_data)


if __name__ == '__main__':
    main()