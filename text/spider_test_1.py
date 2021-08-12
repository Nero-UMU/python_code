import requests
import bs4


url = 'https://www.bitpush.news/covid19/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
f = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(f.text, features='lxml')
print(soup)