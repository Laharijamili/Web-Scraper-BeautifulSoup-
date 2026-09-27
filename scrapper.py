import requests
from bs4 import BeautifulSoup
import csv

# Website to scrape
url = "https://books.toscrape.com/"

# Send request to website
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books
    books = soup.find_all("article", class_="product_pod")

    # Create CSV file
    with open("scraped_books.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # CSV headings
        writer.writerow(["Book Title", "Price", "Availability"])

        # Extract information
        for book in books:

            title = book.h3.a["title"]

            price = book.find("p", class_="price_color").text

            availability = book.find(
                "p", class_="instock availability"
            ).text.strip()

            writer.writerow([title, price, availability])

            print("Title:", title)
            print("Price:", price)
            print("Availability:", availability)
            print("-" * 50)

    print("Data successfully saved to scraped_books.csv")

else:
    print("Failed to access the website")





to run the project
