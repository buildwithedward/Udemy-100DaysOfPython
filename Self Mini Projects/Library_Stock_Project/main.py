from books import Books
from data import book_data

book_details = []

for books in book_data:
    book_title = books["title"]
    book_author = books["author"]
    available = books["volume"]
    details = Books(book_title, book_author, available)
    book_details.append(details)
