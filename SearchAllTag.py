import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#driver = webdriver.Chrome()

#driver.get("http://example.webscraping.com/places/default/index/")
#html_doc = driver.page_source

url = "http://example.webscraping.com/places/default/index/"
html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text,'lxml')

##all_tag = soup.find_all('a')
##print(all_tag)
##print("Number of all ankr tag : " + len(all_tag))

#findClass = soup.find(class_ = "span12")
#print(findClass)

##allClass = soup.find_all(class_ = "row")
##print(allClass)
##print(len(allClass))

#more_spacfic = soup.find_all('a',{'id :results'})
#print(more_spacfic);
#print(len(more_spacfic)) 

matchinString = soup.find_all('a', string = 'Log In')
print(matchinString)
print(len(matchinString))


#driver.quit()