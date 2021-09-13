import requests
from helpers import headers
from bs4 import BeautifulSoup


url = "https://www.google.com/search?q=разработка+сайтов+москва&start=10"
# Make a GET request to fetch the raw HTML content
req = requests.get(url, headers=headers).text
print(req)

with open("./p_google/index.html", "w") as file:
    file.write(req)


# Parse the html content
soup = BeautifulSoup(req, "html")
