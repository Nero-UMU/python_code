import pandas as pd
import matplotlib.pyplot as plt

# 解决中文无法正确显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    aqi_data = pd.read_csv('beijing_aqi.csv')
    top10_point = aqi_data.sort_values(by=['aqi']).head(10)
    # 图形可视化显示
    top10_point.plot(kind='bar', x='position_name', y='aqi', title='空气质量最好的十个监测点', figsize=(20, 10))
    plt.savefig('top10_point_bar.png')
    plt.show()




if __name__ == '__main__':
    main()




