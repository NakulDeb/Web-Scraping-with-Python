import requests
import time
from bs4 import BeautifulSoup

url = 'https://history.state.gov/countries/all'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


x = soup.find(id="content-inner").find_all('a')

for i in x:
	if i.text[0]=='P':
		print(i.text)

