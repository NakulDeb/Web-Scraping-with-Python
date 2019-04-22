import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.set_page_load_timeout("20")
driver.get("https://www.google.com/")
driver.find_element_by_name('q').send_keys("What is Random number")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[3]/center/input[1]").send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()
