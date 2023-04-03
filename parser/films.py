import re
from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL = "https://jut.su/anime/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
              "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/108.0.0.0 Safari/537.36"
}


def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    return response


def get_data_from_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_=re.compile("^all_anime_global"))
    films = []
    soup.find()
    for item in items:
        film = {
            "title": item.find("div", class_="aaname").string,
        }
        films.append(film)
    pprint(films)


html = get_html(URL)
get_data_from_page(html.text)

#
# def parser():
#     html = get_html(URL)
#     if html.status_code == 200:
#         films = []
#         for i in range(1, 2):
#             html = get_html(f"{URL}page/{i}/")
#             current_page = get_data_from_page(html.text)
#             films.extend(current_page)
#         return films
#     else:
#         raise Exception("Error in parser")
