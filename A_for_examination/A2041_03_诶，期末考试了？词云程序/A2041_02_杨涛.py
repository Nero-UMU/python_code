'''
    作者：杨涛
    日期：2021/6/10
    功能：制作一个词云。
'''

from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba
from matplotlib import pyplot as plt


def trans_CN(text):
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result


with open("诗经.txt ", encoding='utf-8') as fp:
    text = fp.read()
    text = trans_CN(text)
    # 输出文字
    mask = np.array(image.open("房子.jpg"))
    wordcloud = WordCloud(
        mask=mask,
        font_path="C:\Windows\Fonts\simkai.ttf",
        # 定义背景色
        background_color='black',
        max_words=100,
    ).generate(text)
    #生成词云并保存
    plt.imshow(wordcloud)
    plt.show()
    wordcloud.to_file('star.jpg')


