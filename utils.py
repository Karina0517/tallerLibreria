import json
from datetime import date
from pathlib import Path

# Define the path to the JSON file that stores book data
BOOKS_FILE = Path(__file__).parent / "books.json"
books = []  # Global list to store book records

# Load books from the JSON file into the global 'books' list
def load_books():
    global books
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            books.clear()
            books.extend(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError):
        books.clear()  # Clear list if file is missing or corrupt

# Save books to the JSON file (uses global 'books' if no data is passed)
def save_books(data=None):
    if data is None:
        data = books
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Generate a new unique ID for a book based on the existing list
def get_new_id(book_list):
    if not book_list:
        return 1
    return max(b["id"] for b in book_list) + 1

# Return today's date formatted as a string (YYYY-MM-DD)
def input_date():
    today = date.today()
    return today.strftime("%Y-%m-%d")
