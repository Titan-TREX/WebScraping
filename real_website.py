from bs4 import BeautifulSoup
import requests
# 'verify=False' add karein
html_text = requests.get("https://www.libertybooks.com/index.php?route=product/search&sort=p.date_added&order=DESC&search=", verify=False).text
soup = BeautifulSoup(html_text, "lxml")
book_cards = soup.find_all("div", class_="ls-featured-book")

print(f"Total Books Found: {len(book_cards)}")

for book in book_cards:

    name_tag = book.find("a", class_="heading-books")
    book_link = name_tag['href'] if name_tag else "No Link"
    author_tag = book.find("h3")

    price_box = book.find("div", class_="ls-featured-book-price")
    price_tag = price_box.find("h2" , class_="regular")

 
    name = name_tag.text.strip() if name_tag else "No Name"
    price = price_tag.text.strip() if price_tag else "No Price"
    author = author_tag.text.strip() if author_tag else "No Author"

    print(f"Book: {name}")
    print(f"Link: {book_link}")
    print(f"Author: {author}")

    print(f"Price: {price}")

    print("-" * 20)
