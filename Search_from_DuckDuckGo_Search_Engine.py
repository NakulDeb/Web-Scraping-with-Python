import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

search = "Unity"
#search = input("Enter what you Want : ")
driver = webdriver.Chrome()



driver.get("https://duckduckgo.com/")
#assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys(search)
elem.send_keys(Keys.RETURN)
time.sleep(1)

html_doc = driver.page_source
soup = BeautifulSoup(html_doc,'lxml')

# all_tag = soup.find_all('a')
# print(all_tag)


find_all_cite = soup.find_all("span", class_= "result__url__domain")

k = 0;
for i in find_all_cite:
	print(i.text)
	k= k+1
	if k>10:
		break

driver.close()
