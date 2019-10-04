import requests
import time
from bs4 import BeautifulSoup

url = 'http://103.79.117.242/ru_profile/public/teacher/227/profiles'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


x = soup.find_all('p',class_="lead")

for i in x:
	print(i.strong.text)

