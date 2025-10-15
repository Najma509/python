
class Publisher:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Publisher Name: {self.name}")
class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)  
        self.title = title
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
class PythonBook(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)  
        self.price = price
        self.no_of_pages = no_of_pages
    def display_info(self):
        super().display_info()
        print(f"Price: {self.price}")
        print(f"Number of Pages: {self.no_of_pages}")


python_book = PythonBook("Subharamaniyan", "Learning Python", "Mark Antony", 100, 780)


python_book.display_info()
