import requests
import time
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


x = soup.find_all('h3') # book name
y = soup.find_all('p',class_ = "price_color") # books price

for i in x:
	print(i.text)





