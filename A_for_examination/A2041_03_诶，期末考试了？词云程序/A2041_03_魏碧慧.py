'''
作者：魏碧慧
日期：2021、6、10
功能：词云图——沟通与礼仪内容的概述
'''
import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np


font = r'C:/windows/Fonts/simfang.ttf'  #文本路径
filename = '沟通与礼仪.txt'
#打开文件
text = open(r'沟通与礼仪.txt','r',encoding = 'utf-8') .read()
#分词
cut = jieba.cut(text)
#将词语连接起来，以空格为连接词
string = ' '.join(cut)
#打开背景图
img = Image.open(r'background.jpg')
#将图片装换为数组
img_array = np.array(img)
#设置停止词
stopword = ['xa0']
wc = WordCloud(background_color = 'white',width = 300,
                height =800 ,mask=img_array,font_path=font)


#绘制图片
wc.generate_from_text(string)
plt.imshow(wc)
plt.axis('off')
#显示图片
plt.show()
#保存图片
wc.to_file(r'new.png')