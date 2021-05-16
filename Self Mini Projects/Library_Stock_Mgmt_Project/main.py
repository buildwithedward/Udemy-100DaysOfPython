from books import Books
from data import book_data
from backend import Stock
book_details = []

for books in book_data:
    book_title = books["title"]
    book_author = books["author"]
    available = books["volume"]
    details = Books(book_title, book_author, available)
    book_details.append(details)

lib = Stock(book_details)

proceed = True


while proceed:
    user = input("Do you know the book name (y/n): ").lower()
    if user == 'n':
        lib.search()
    elif user == 'y':
        lib.update_stocks()
    if input("Do you want to update stock for another book (y/n): ") == 'n':
        proceed = False
    else:
        proceed = True
