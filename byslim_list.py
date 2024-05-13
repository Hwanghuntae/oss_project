import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_autoinstaller

url = "https://www.byslim.com/category/top/6/"


chromedriver_autoinstaller.install()
driver = webdriver.Chrome()


name_list, img_list, link_list = [], [], []

driver.get(url)
driver.implicitly_wait(time_to_wait=5)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

sizes = soup.select(".prdList.grid3")


for size in sizes:
  divs = size.find_all(attrs={'class': "thumbnail"})
  for div in divs:
    prd_div = div.find('div', class_='prdImg')
    if prd_div:
      link_list.append(prd_div.find('a')['href'])
      name_list.append(prd_div.find('img')['alt'])
      img_list.append(prd_div.find('img')['src'])
    # link = div.attrs["href"]
    # link_list.append("https://www.byslim.com/" + link)

    # imgs = div.find('img')
    
    # img = imgs["src"]
    # img_list.append(imgs)

    # name = imgs["alt"]
    # name_list.append(name)
    

print(name_list)