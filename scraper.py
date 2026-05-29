import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

#save it to file
with open("quotes.txt", "w", encoding="utf-8") as f:
    for quote, author in zip(quotes, authors):
        f.write(f"{quote.text} - {author.text}\n")