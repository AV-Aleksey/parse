import requests
from bs4 import BeautifulSoup

from helpers import headers
from parser_methods import *


def parser_google(pages_limit=10):
    limit = str(pages_limit)
    url = 'https://www.google.com/search?q=разработка+сайтов+москва&start=10}'
    req = requests.get(url, headers=headers).text
    soup = BeautifulSoup(req, "lxml")

    advertising_cards = get_advertising_cards(soup, True)
    body_cards = get_body_cards(soup, True)

    result = [*body_cards, *advertising_cards]

    print(result)
    print(len(result))


parser_google()
