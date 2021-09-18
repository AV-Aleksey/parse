import re

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "Accept-language": "ru-RU,ru;q=0.9"
}


text = "Создание сайтов от компании ВебРост, узнать стоимость и заказать сайт по : +7 (863) 333-52-48, +7 (499) 450-65-43."


def findPhone(text):
    data = re.findall(
        r"(?:\B\+ ?|\b0)(?: *[(-]? *\d(?:[ \d:(-]*\d)?)? *(?:[)-] *)?\d+ *(?:[/)-] *)?\d+ *(?:[/)-] *)?\d+(?: *- *\d+)?", text)
    result = []

    if(len(data)):
        for phone in data:
            cleanPhone = filterPhoneNumber(phone)

            if len(cleanPhone) == 11:
                result.append(cleanPhone)
    else:
        print('не найдены')

    return result


def filterPhoneNumber(text):
    filter = [' ', '-', '(', ')', '+']
    result = text

    for pattern in filter:
        result = result.replace(pattern, '')

    return result
