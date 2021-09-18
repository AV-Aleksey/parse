import json
from helpers import connectPage
from parser_methods import *


# Основная ф-ия дял парсинга google
def parser_google(pages_limit=100, createJson=False):
    currentIdx = 10
    result = []

    while currentIdx <= pages_limit:
        soup = connectPage(
            f'https://www.google.com/search?q=разработка+сайтов+москва&start={str(currentIdx)}')

        if soup == None:
            currentIdx += 10
            continue

        advertising_cards = get_advertising_cards(soup, True)
        body_cards = get_body_cards(soup, True)

        concat = body_cards + advertising_cards

        result += concat
        currentIdx += 10

    if createJson:
        data = {}
        i = 0
        for item in result:
            data[item["url"]] = {
                "url": item["url"],
                "descriptions": item["descriptions"],
                "phone": item["phone"] or "none"
            }
            i += 1

        with open("google_cards.json", "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    print(len(result))

    return result


parser_google(100, True)
