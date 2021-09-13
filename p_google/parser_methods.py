def get_body_cards(soup, logs=False):
    all_cards = soup.find_all(class_="g")
    result = []

    err_count = 0

    for card in all_cards:
        payload = {}

        urls = card.find_all(class_="tjvcx")
        descriptions = card.find_all(class_="lEBKkf")

        try:
            payload["url"] = urls[0].contents[0]
        except:
            payload["url"]
            err_count += 1

        try:
            payload["descriptions"] = descriptions[0].contents[0].text
        except:
            payload["descriptions"] = 'не удалось получить данные'
            err_count += 1

        result.append(payload)

    if logs:
        print('--  --  --')
        print("Количество найденных узлов в DOM:", len(all_cards))
        print("Количество спаршеных: ", len(result))
        print("Количество спаршеных с ошибками: ", err_count)
        print('--  --  --')

    return result


def get_advertising_cards(soup, logs=False):
    all_cards = soup.find_all(class_="uEierd")
    result = []

    err_count = 0

    for card in all_cards:

        payload = {}
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
        except:
            payload["descriptions"] = None
            err_count += 1

        try:
            payload["phone"] = phone[0].text
        except:
            payload["phone"] = None
            err_count += 1

        result.append(payload)

    if logs:
        print('--  --  --')
        print("Количество найденных узлов в DOM:", len(all_cards))
        print("Количество спаршеных: ", len(result))
        print("Количество спаршеных с ошибками: ", err_count)
        print('--  --  --')

    return result
