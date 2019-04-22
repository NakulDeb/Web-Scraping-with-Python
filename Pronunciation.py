import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#search = "Unity"
search = input("Enter what you Want : ")
driver = webdriver.Chrome()



driver.get("https://translate.google.com")
assert "Google" in driver.title

elem = driver.find_element_by_id("sugg-item-en").click()
elem = driver.find_element_by_id("source")
elem.send_keys(search)

elem = driver.find_element_by_class_name("src-tts").click()
time.sleep(10)
driver.close()

