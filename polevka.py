from bs4 import BeautifulSoup
import json
# from recept.json import recept
import requests


def main():
    url = "https://souhrada.github.io/bsoup-exam/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser") #html.parser = jednoduché označení pro response.text

    pokus_1 = soup.select("h2")[0]
    pokus_2 = soup.select("h2")[1]
    pokus_3 = soup.select("h2")[2]
    pokus_4 = soup.select("h2")[3]
    finalni_produkt = pokus_1.text, pokus_2.text, pokus_3.text, pokus_4.text

    print(pokus_1.text, pokus_2.text, pokus_3.text, pokus_4.text)

    # json.dump(finalni_produkt, recept, indent=4)
    # json.load(recept)

if __name__ == "__main__":
    main()
