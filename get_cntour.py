import requests
from bs4 import BeautifulSoup

url = "http://www.cntour.cn/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml' )
data = soup.select("#main > div > div.mtop.firstMod.clearfix > div.leftBox > div:nth-child(2) > ul > li:nth-child(4) > a")
print(data)
for item in data:
    result={
        'title': item.get_text(),
        'link': item.get('href')
    }
print(result)