from bs4 import BeautifulSoup
import requests
import time
print("print book that you are not familiar with")
unfamiliar_books = input(">")

print(f"Filtering out books: {unfamiliar_books}")
def print_book_details():

    html_text = requests.get("https://www.libertybooks.com/index.php?route=product/search&sort=p.date_added&order=DESC&search=", verify=False).text
    soup = BeautifulSoup(html_text, "lxml")
    book_cards = soup.find_all("div", class_="ls-featured-book")

    print(f"Total Books Found: {len(book_cards)}")

    for index, book in enumerate(book_cards):

        name_tag = book.find("a", class_="heading-books")
        book_link = name_tag['href'] if name_tag else "No Link"
        author_tag = book.find("h3")

        price_box = book.find("div", class_="ls-featured-book-price")
        price_tag = price_box.find("h2" , class_="regular")

    
        name = name_tag.text.strip() if name_tag else "No Name"
        price = price_tag.text.strip() if price_tag else "No Price"
        author = author_tag.text.strip() if author_tag else "No Author"

        if unfamiliar_books.lower() not in name.lower():
            with open(f"post/{index}.txt", "w") as f:
                f.write(f"{name}\n")
                f.write(f"Book: {name}")
                f.write(f"Link: {book_link}")
                f.write(f"Author: {author}")
                f.write(f"Price: {price}")
                print("file are saved")

if __name__ == "__main__":
    while True:
        print_book_details()
        time_wait = 10
        print(f"Waiting for {time_wait} minutes...")
        time.sleep(time_wait * 60)