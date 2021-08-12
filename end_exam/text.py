'''
伪装浏览器
'''

import requests
url = 'http://college.gaokao.com/school/5/'
#添加头部，伪装浏览器，字典格式
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
#增加headers参数
response = requests.get(url=url, headers=headers)
html = response.text
print(html)