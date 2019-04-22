import requests
import time
from bs4 import BeautifulSoup

url = 'https://simple.wikipedia.org/wiki/List_of_fruits'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


x = soup.find(id="mw-content-text").find_all('a')

for i in x:
	if i.text[0]=='P':
		print(i.text)

