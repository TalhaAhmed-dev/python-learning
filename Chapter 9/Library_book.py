class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.checked_out = False

    def checkout(self):
        self.checked_out = True

    def return_book(self):
        self.checked_out = False

    def book_status(self):
        if self.checked_out:
            print("Book is checked out")
        else:
            print("Book is available")

book1 = Book("PCC","Eric Matthes")
book1.book_status()
book1.checkout()
book1.book_status()

