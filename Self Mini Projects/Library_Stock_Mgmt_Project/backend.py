class Stock:
    def __init__(self, book_list):
        self.instock = book_list

    # TODO: Create function to check availablity of a book when a user inputs
    def check_availability(self):
        """Check availability of user requested book"""
        book_name = input("Enter the book name: ").lower()
        for check in self.instock:
            if check.title.lower() == book_name and check.volume > 0:
                print(f"The searched book is available")
                return True
        print("The searched book is not available")
        return False

    # TODO: Create function to update the volume of relevant book
    def update_stocks(self):
        if self.check_availability():
            book_name = input("Enter the book name again: ").lower()
            user_choice = input(
                "What would like to do? (borrow/return): ").lower()
            for check in self.instock:
                # print(check.volume)
                if book_name == check.title.lower() and user_choice == "borrow":
                    check.volume -= 1
                    print(
                        f"The stocks are updated. Remaining available copies are {check.volume}")
                elif book_name == check.title.lower() and user_choice == "return":
                    check.volume += 1
                    print(
                        f"The stocks are updated. Remaining available copies are {check.volume}")

        # TODO: try to create function where user inputs a part of book name and show books which matches that string

    def search(self):
        """Search the book name by known keywords"""
        search_book = input("Enter a book name/author: ")
        for find in self.instock:
            # print(find)
            if search_book in find.title.lower():
                print(f"'{find.title}' by '{find.author}'")
