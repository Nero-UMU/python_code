import bs4
import requests


def main():
    url = 'https://www.jju.edu.cn/'
    rq = requests.get(url=url, timeout=30)
    rq.encoding = 'utf-8'
    if rq.status_code != 200:
        print('网页爬取失败')
    else:
        html_word = rq.text
        texts = bs4.BeautifulSoup(html_word, features='lxml')
        title = texts.find('title').text
        print(title)


if __name__ == '__main__':
    main()