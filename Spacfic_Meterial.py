from bs4 import BeautifulSoup
import requests

a = requests.get("https://nataliarslan.com/blog/2017/3/15/python-beautifulsoup-for-data-scraping")
soup = BeautifulSoup(a.text, 'lxml')

rows = soup.find_all("div", class_="entry clearfix post")
data = [["District","Name","Address","Phone"]]

for row in rows:
    district = ""
    for elem in row.find_all():
        if elem.name == "h2":
            district = elem.text.replace(" Veteriner Klinikleri, CITY_NAME","")
        elif elem.name == "tr" and len(elem.find_all("td")) > 0:
            data.append([district])
            for td in elem.find_all("td"):
                data[-1].append(td.text)

for item in data:
    print(", ".join(item))