import requests
from bs4 import BeautifulSoup
import csv

URL = "https://books.toscrape.com/"
response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Book Name", "Price"])
    for book in books:
        name = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        writer.writerow([name, price])

print("Web scraping completed successfully!")
