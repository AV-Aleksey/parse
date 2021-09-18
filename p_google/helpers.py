import re
import requests
import time
from bs4 import BeautifulSoup


# Заголовки для парсера
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "Accept-language": "ru-RU,ru;q=0.9"
}


# Метод поиска телефона в строке
def findPhone(text):
    data = re.findall(
        r"(?:\B\+ ?|\b0)(?: *[(-]? *\d(?:[ \d:(-]*\d)?)? *(?:[)-] *)?\d+ *(?:[/)-] *)?\d+ *(?:[/)-] *)?\d+(?: *- *\d+)?", text)
    result = []

    if(len(data)):
        for phone in data:
            cleanPhone = filterPhoneNumber(phone)

            if len(cleanPhone) == 11:
                result.append(cleanPhone)

    return result


# Фильтр для удлаения не нужных символов из строки
def filterPhoneNumber(text):
    filter = [' ', '-', '(', ')', '+']
    result = text

    for pattern in filter:
        result = result.replace(pattern, '')

    return result


def connectPage(url, tryCount=1, delay=1, ):
    limit = tryCount

    try:
        req = requests.get(url, headers=headers).text
        soup = BeautifulSoup(req, "lxml")

        return soup
    except:
        if limit <= 5:
            print(f'Ошибка соединения с url:{url}, попытка {tryCount}')
            time.sleep(delay)
            connectPage(url, tryCount + 1)
        else:
            return None
