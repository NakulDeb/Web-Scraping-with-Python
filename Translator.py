import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


search = "Unity"
#search = input("Enter what you Want : ")
driver = webdriver.Chrome()



driver.get("https://translate.google.com")
assert "Google" in driver.title

#elem = driver.find_element_by_id("sugg-item-en").click()
#d = driver.find_element_by_class_name("tl-more").click()
t1 =   driver.find_element_by_class_name("language-list-unfiltered-langs-tl_list")
t2 =   t1.find_element_by_class_name("language_list_item_wrapper")
elem =t2.find_element_by_class_name("language_list_item_icon")

#elem = t2.find_element_by_link_text("Bengali").click()
# elem = driver.find_element_by_id("source")
# elem.send_keys(search)
# elem.send_keys(Keys.RETURN)
# time.sleep(5)
# driver.close()


# html_doc = driver.page_source
# soup = BeautifulSoup(html_doc,'lxml')

# all_tag = soup.find_all('a')
# print(all_tag)
