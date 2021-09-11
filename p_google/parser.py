from bs4 import BeautifulSoup

with open("./p_google/index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")


result = []


def get_body_cards():
    all_cards = soup.find_all(class_="g")

    for card in all_cards:
        payload = {}

        urls = card.find_all(class_="tjvcx")
        descriptions = card.find_all(class_="lEBKkf")

        payload["url"] = urls[0].contents[0]
        payload["descriptions"] = descriptions[0].contents[1].text

        result.append(payload)


def get_advertising_cards():
    all_cards = soup.find_all(class_="uEierd")

    for card in all_cards:
        payload = {}
        urls = card.find_all(class_="qzEoUe")
        descriptions = card.find_all(class_="lyLwlc")
        phone = card.find_all(class_="WZ8Tjf")

        payload["url"] = urls[0].contents[0]
        payload["descriptions"] = descriptions[0].contents[0].text

        print('     ')

        if phone and phone[0]:
            payload["phone"] = phone[0].text
        else:
            payload["phone"] = None

        result.append(payload)


get_advertising_cards()
print(result[0])
