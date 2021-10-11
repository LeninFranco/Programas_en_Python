#Instalar las siguientes librerias
#1. pip install beautifulsoup4
#2. pip install requests

from bs4 import BeautifulSoup
import requests
import re

url = "http://www.profightdb.com/top-rated-matches.html"

page_response = requests.get(url)

page_content = BeautifulSoup(page_response.content,"html.parser")

box = page_content.find("div", {"class":"left-content"})

list_champions = list(map(lambda data: data.text,box.find_all("a")))

companies = re.findall("(\(.*?\)|{.*?}|<.*?>|\[.*?\])",box.text)

result = dict(zip(list_champions,companies))

for champion, company in result.items():
    print(f"{champion}: {company}")