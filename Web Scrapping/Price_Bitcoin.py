#Instalar las siguientes librerias
#1. pip install beautifulsoup4
#2. pip install requests

from bs4 import BeautifulSoup
import requests 

def Scrape_Price():
    url = "https://finance.yahoo.com/quote/BTC-USD/"

    page_response = requests.get(url)

    page_content = BeautifulSoup(page_response.content,"html.parser")

    return page_content.find("span", {"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text


print(Scrape_Price() + " USD")