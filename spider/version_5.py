'''
作者：魏嘉鲲
日期：2021.5.28
版本：5.0
功能：读取已经存在的JSON文件，并获取前5名，存入新的JSON文件中
读取已经存在的JSON文件，将其转成CSV格式
网络爬虫实时获取空气质量信息
'''


import requests


def main():
    # 根据URL发出get请求
    url = 'https://www.jju.edu.cn/info/1047/80052.htm'
    r = requests.get(url, timeout=30)
    r.encoding = 'utf-8'
    # if r.status_code == 200:
    #     print(r.text)
    # else:
    #     print('连接失败，无法获取网页的信息')

    # all_text表示访问网页的所有内容
    all_text = r.text
    div_text = '''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" type="text/css" href="../../css/css.css">
        <script type="text/javascript" src="../../js/bdtxt.min.js"></script>
        <script type="text/javascript" src="../../js/bdtxt.js"></script>
       <script type="text/javascript" src="../../js/jwplayer.js"></script>
        <title>'''

    # 实现字符串的精确定位
    title_index = all_text.find(div_text)
    begin = title_index + len(div_text)
    end = begin + 50
    title_text = all_text[begin: end]
    print(title_text)


if __name__ == '__main__':
    main()