import requests
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for i in range(36,len(soup.findAll('a'))+1):
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    print(link)
    time.sleep(1)