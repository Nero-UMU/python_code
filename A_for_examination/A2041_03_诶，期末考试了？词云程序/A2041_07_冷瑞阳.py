'''
   作者：冷瑞阳
   日期：2021.6.10-2021.6.
   功能：
'''


from wordcloud import WordCloud, STOPWORDS
from os import path
import matplotlib.pyplot as plt
import PIL .Image as image

import numpy as np
import jieba


d = path.dirname(__file__)


def main():

    #读取文本
    f = open('鲁迅文集.txt','r',encoding='utf-8')
    f_ = f.read()
    #读取图片
    alice_mask = np.array(image.open(path.join(d,'luxun.png')))
    stopwords = set(STOPWORDS)
    stopwords.add("said")

    word_list = jieba.cut(f_)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)

    #生成一个词云图像,并设置词云属性
    wc = WordCloud(max_font_size=20000,font_path='C:\Windows\Fonts\simkai.ttf',background_color='white',\
                   max_words=20000000, mask=alice_mask,
               stopwords=stopwords,random_state=40).generate(result)

    #保存生成的词云
    wc.to_file("zhou.png")

    # matplotlib的方式展示生成的词云图像
    plt.imshow(wc,interpolation='lanczos')
    # 不显示坐标尺寸
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()