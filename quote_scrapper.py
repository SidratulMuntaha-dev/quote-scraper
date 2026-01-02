from bs4 import BeautifulSoup as soup
import requests


url = "https://quotes.toscrape.com/"
 
web = requests.get(url)
doc = soup(web.text, "html.parser")

quotes = doc.find_all("span", itemprop = "text")
authors = doc.find_all("small",  itemprop ="author")

for i, (quote,author) in enumerate(zip(quotes, authors), start = 1):
  print(f'{i}."{quote.text[1:-1]}" ')
  print("by -", author.text, "\n\n")
