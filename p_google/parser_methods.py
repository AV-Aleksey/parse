from helpers import findPhone

# Метод для парсинга карточек из центральной части страницы выдачи


def get_body_cards(soup, logs=False):
    result = []
    err_count = 0

    all_cards = soup.find_all(class_="g")

    for card in all_cards:
        payload = {
            "phone": []
        }

        urls = card.find_all(class_="tjvcx")
        descriptions = card.find_all(class_="lEBKkf")

        try:
            payload["url"] = urls[0].contents[0]
        except:
            payload["url"]
            err_count += 1

        try:
            payload["descriptions"] = descriptions[0].contents[0].text
            payload["phone"] = findPhone(descriptions[0].contents[0].text)
        except:
            payload["descriptions"] = 'не удалось получить данные'
            err_count += 1

        result.append(payload)

    if logs:
        print('--  Карточки  --')
        print("Количество найденных узлов в DOM:", len(all_cards))
        print("Количество спаршеных: ", len(result))
        print("Количество спаршеных с ошибками: ", err_count)
        print('--  --  --')

    return result


# Метод для парсинга карточек из рекламной части страницы выдачи
def get_advertising_cards(soup, logs=False):
    result = []
    err_count = 0

    all_cards = soup.find_all(class_="uEierd")

    for card in all_cards:
        payload = {
            "phone": []
        }

        urls = card.find_all(class_="qzEoUe")
        descriptions = card.find_all(class_="lyLwlc")
        phone = card.find_all(class_="WZ8Tjf")

        try:
            payload["url"] = urls[0].contents[0]
        except:
            payload["url"] = None
            err_count += 1

        try:
            payload["descriptions"] = descriptions[0].contents[0].text
            payload["phone"] = findPhone(descriptions[0].contents[0].text)
        except:
            payload["descriptions"] = None
            err_count += 1

        try:
            payload["phone"].append(phone[0].text)
        except:
            err_count += 1

        result.append(payload)

    if logs:
        print('--  Карточки рекламы  --')
        print("Количество найденных узлов в DOM:", len(all_cards))
        print("Количество спаршеных: ", len(result))
        print("Количество спаршеных с ошибками: ", err_count)
        print('--  --  --')

    return result
