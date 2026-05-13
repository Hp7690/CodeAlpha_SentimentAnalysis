# ─────────────────────────────────────────────────────────
# Author  : Harsh Pandey
# Project : Web Scraping — CodeAlpha Internship Task 1
# Goal    : Build a custom books dataset from scratch
# ─────────────────────────────────────────────────────────

import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

# Map word ratings to numbers so they're easier to analyze later
RATING_MAP = {
    "One": 1, "Two": 2, "Three": 3,
    "Four": 4, "Five": 5
}

def extract_books_from_page(page_num):
    """Fetch one page and return list of book dicts."""
    url = BASE_URL.format(page_num)
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print(f"  Warning: Page {page_num} returned status {response.status_code}, skipping.")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    page_books = []

    for item in soup.select("article.product_pod"):
        title    = item.h3.a["title"]
        price    = float(item.select_one(".price_color").text[1:])
        rating   = RATING_MAP.get(item.p["class"][1], 0)
        in_stock = "In stock" in item.select_one(".availability").text

        page_books.append({
            "title"    : title,
            "price_gbp": price,
            "rating"   : rating,
            "in_stock" : in_stock,
            "page"     : page_num
        })

    return page_books

# ── Scrape first 10 pages (500 books total) ──────────────
all_books = []
for p in range(1, 11):
    books = extract_books_from_page(p)
    all_books.extend(books)
    print(f"Page {p} done — {len(books)} books collected")
    time.sleep(0.5)  # be polite to the server

# ── Sanity check & save ──────────────────────────────────
if not all_books:
    print("\n⚠ No books collected. Check your internet connection.")
else:
    df = pd.DataFrame(all_books)

    print(f"\nTotal books scraped : {len(df)}")
    print(f"Average price       : £{df['price_gbp'].mean():.2f}")
    print(f"Highest rated books :\n{df[df['rating']==5]['title'].head(5).to_string(index=False)}")
    print(f"Books in stock      : {df['in_stock'].sum()} / {len(df)}")

    df.to_csv("books_dataset.csv", index=False)
    print("\n✓ Dataset saved as books_dataset.csv")