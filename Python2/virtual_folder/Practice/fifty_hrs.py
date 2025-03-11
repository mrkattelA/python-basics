import requests
from bs4 import BeautifulSoup

NUM = 0
PLAYER = 1
HRS = 2
YEAR = 3
BIRTH_YEAR = 4

def get_content():
    url = "https://static.webucator.com/media/public/documents/hrleaders.html"
    r = requests.get(url)
    return r.text

def get_soup(content):
    return BeautifulSoup(content, "lxml")

def get_players(soup):
    data_container = soup.find("tbody")

    rows = data_container.find_all("tr")

    players = []
    for row in rows:
        hrs = int(row.find_all("td")[HRS].text)
        if hrs >= 50:
            player = row.find_all("td")[PLAYER].text
            if player not in players:
                players.append(player)
        if hrs < 50:
            return players
    return players

def main():
    content = get_content()
    soup = get_soup(content)
    players = get_players(soup)

    for i, player in enumerate(players, 1):
        print(f"{i}.{player}")

main()
