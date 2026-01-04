from bs4 import BeautifulSoup as soup
import requests

base_url = "https://quotes.toscrape.com/page/{}/"
page = 1
count = 1

while True:
    response = requests.get(base_url.format(page))
    if response.status_code != 200:
        break

    document = soup(response.text, "html.parser")
    quotes = document.find_all("span", itemprop="text")
    authors = document.find_all("small", itemprop="author")

    if not quotes:
        break

    for quote, author in zip(quotes, authors):
        print(f'{count}."{quote.text[1:-1]}"')
        print("by -", author.text, "\n")
        count += 1

    page += 1

