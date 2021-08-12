import jieba # 导入结巴库
import matplotlib.colors
import wordcloud # 导入词云库
from matplotlib import pyplot as plt
import numpy
from PIL import Image

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    # 以r的方式读取文件，编码格式为utf-8
    f = open('中华人民共和国民法典.txt', 'r', encoding='utf-8')
    # 获取文件中的所有文字
    passage = f.read()
    # 养成关闭文件的好习惯
    f.close()

    color_mask = numpy.array(Image.open('party_flag.png'))

    # 利用结巴库将passage分割成一个个词组
    each_words = jieba.lcut(passage)

    # 以空格分隔各词语
    new_str = ' '.join(each_words)

    # 颜色列表
    color = matplotlib.colors.ListedColormap(['indigo', 'brown', 'gold', 'blue', 'green', 'yellow', 'red', 'orange', 'pink', 'gray', 'black'])

    # 生成词云对象
    cloud = wordcloud.WordCloud(max_words=800, font_path='C:\Windows\Fonts\simkai.ttf', mask=color_mask, colormap=color, background_color='white', width=2000, height=1800).generate(new_str)
    # 展示词云图片
    plt.imshow(cloud)
    plt.show()

    # 保存图片
    cloud.to_file('中华人民共和国民法典高频词云.png')


if __name__ == '__main__':
    main()

