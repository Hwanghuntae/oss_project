import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_autoinstaller

main_url = "https://lookple.com/category/top/26/"


chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

name_list, img_list, link_list, size_list, size_dic_list = [], [], [], [], []

def get_list(url):
  driver.get(url)
  driver.implicitly_wait(time_to_wait=5)
  page = driver.page_source
  soup = BeautifulSoup(page, "html.parser")
  list_page = soup.select(".prdList.grid3")

  for li in list_page:
    divs = li.find_all(attrs={'class': "thumbnail"})
    for div in divs:
      prd_div = div.find('div', class_='prdImg')
      if prd_div:
        link_list.append("https://lookple.com" + prd_div.find('a')['href'])
        name_list.append(prd_div.find('img')['alt'])
        img_list.append(prd_div.find('img')['src'])
  
  return "complete getting list data"

def get_size(link_list,name_list):
  url = link_list
  driver.get(url)
  driver.implicitly_wait(time_to_wait=5)
  page = driver.page_source
  soup = BeautifulSoup(page, "html.parser")

  div_tags = soup.find_all('div', style=lambda value: value and 'text-align: center;' in value)
  for div in div_tags:
    if "총장" in div.text.strip():
      size_list.append(div.text.strip())  
  return "complete getting size data"



print('test getting products list data')
print(get_list(main_url))
print()
print('상품 이름 리스트 출력')
for name in name_list:
  print(name)

print()
print()

print('상품 이미지 사진 링크 출력')
for img_link in img_list:
  print(img_link)
  
print()
print()

print('상품 링크 출력')
for link in link_list:
  print(link)

print()
print() 

print('상품 사이즈 데이터 기져오기')
print(get_size(link_list[0], name_list[0]))
print(get_size(link_list[1], name_list[1]))
print(get_size(link_list[2], name_list[2]))
print(size_list)

print()
print()
   
test_dic = {name_list[2]: None}
temp_size_list = list()
for i in size_list:
  temp_size_list.append(i)
test_dic = {name_list[2]:temp_size_list}
size_dic_list.append(test_dic)



print(size_dic_list)

# 








