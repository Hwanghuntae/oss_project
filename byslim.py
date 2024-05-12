import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_autoinstaller

url = "https://www.byslim.com/product/코튼-레이어드-트임-에어쿨-반팔티/26726/category/6/display/1/"


chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

driver.get(url)
driver.implicitly_wait(time_to_wait=5)
page = driver.page_source
soup = BeautifulSoup(page, "html.parser")

td_tags = soup.find_all("td")


for td in td_tags:
    if 'style' in td.attrs: 
        content = td.text.strip()  
        print(content)
