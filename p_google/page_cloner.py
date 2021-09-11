import requests
from helpers import headers
from bs4 import BeautifulSoup


url = "https://www.google.com/search?q=%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0+%D1%81%D0%B0%D0%B9%D1%82%D0%BE%D0%B2&tbs=qdr:y&sxsrf=AOaemvKOax-5QDf8mm10SUOHgaqNhsrR6A:1631388443123&source=lnt&sa=X&ved=2ahUKEwiPxpHF0_fyAhVmoosKHUTNBLcQpwV6BAgCECo&biw=1373&bih=920"
# Make a GET request to fetch the raw HTML content
req = requests.get(url, headers=headers).text
print(req)

with open("./p_google/index.html", "w") as file:
    file.write(req)


# Parse the html content
soup = BeautifulSoup(req, "html")

