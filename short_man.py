import requests
from bs4 import BeautifulSoup

url = "https://smallman.co.kr/product/list.html?cate_no=5018"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html = response.text


soup = BeautifulSoup(html, 'html.parser')

title = soup.title.text
print("웹 페이지 제목:", title)




