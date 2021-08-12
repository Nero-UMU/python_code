import numpy as np
from PIL import Image
import wordcloud
import jieba

stopword='stop_words.txt'

def func1():
	file = open('字典.txt',encoding="utf-8")
	result = file.read()
	file.close()
	return result

def func2(words):
	wordList = jieba.lcut(words)
	c = wordcloud.WordCloud(scale=4,stopwords=stopword,font_path="msyh.ttc")
	c.generate(" ".join(wordList))
	c.to_file('./hh.jpg')
words = func1()
func2(words)