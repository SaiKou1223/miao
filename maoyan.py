import requests
from requests.exceptions import RequestException
from multiprocessing import Pool
import lxml.etree
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

def get_one_page(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except:
        return None

def parse_one_page(html):
    soul = lxml.etree.HTML(html)
    items = soul.xpath('//dl[@class="board-wrapper"]/dd')
    for item in items:
        num = item.xpath('./i/text()')[0]
        title = item.xpath('./div//p[@class="name"]/a/text()')[0]
        actor = item.xpath('./div//p[@class="star"]/text()')[0][17:-9]
        releasetime = item.xpath('./div//p[@class="releasetime"]/text()')[0]
        score1 = item.xpath('./div//p[@class="score"]/i[1]/text()')[0]
        score2 = item.xpath('./div//p[@class="score"]/i[2]/text()')[0]
        print("num:",num,"title:",title,"actor:",actor,"releasetime:",releasetime,"score:",score1+score2,)

def main(offset):
    url = 'https://maoyan.com/board/4?offset={}'.format(offset)
    html = get_one_page(url)
    parse_one_page(html)

if __name__ == "__main__":
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])