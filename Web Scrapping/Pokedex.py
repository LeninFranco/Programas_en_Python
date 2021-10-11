#Instalar las siguientes librerias
#1. pip install beautifulsoup4
#2. pip install requests

from bs4 import BeautifulSoup
import requests 
from os import system

url = "https://pokemondb.net/pokedex/all"

page_response = requests.get(url)

page_content = BeautifulSoup(page_response.content,"html.parser")

PokemonRows = page_content.find_all("tr")

print("| {:<3} | {:<20} | {:<28} | {:<4} | {:<6} | {:<7} | {:<6} | {:<6} | {:<5} |".format(" # ","Name","Type","HP","Attack","Defense","Sp.Atk","Sp.Def","Speed"))
print("-"*113)

for row in PokemonRows[1:]:
    statsHTML = row.find_all("td")[4:]
    statsArray = list(map(lambda data: data.text,statsHTML))

    typesHTML = row.find_all("a", attrs={"class":"type-icon"})
    typesArray = list(map(lambda data: data.text, typesHTML))

    ID = row.find("span", attrs={"class":"infocard-cell-data"}).text

    name = row.find("a", attrs={"class":"ent-name"}).text

    megaName = row.find("small", attrs={"class":"text-muted"})
    if megaName:
        name = megaName.text

    print("| {:<3} | {:<20} | {:<28} | {:<4} | {:<6} | {:<7} | {:<6} | {:<6} | {:<5} |".format(ID,name,str(typesArray),statsArray[0],statsArray[1],statsArray[2],statsArray[3],statsArray[4],statsArray[5]))
    print("-"*113)

system("Pause")