import requests
from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


search = "Unity"
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys(search)
elem.send_keys(Keys.RETURN)
time.sleep(1)




url = driver.find_elements_by_xpath('//*[@id]')

for i in url:
	print(i)


driver.close()