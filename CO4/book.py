class Publisher:
    def __init__(self, name):
        print("Publisher class activated")
        self.name = name

    def display(self):
        print(f"Name: {self.name}")


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        print("Book class activated")
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


class Python(Book):
    def __init__(self, name, title, author, price, no_pages):
        super().__init__(name, title, author)
        print("Python class activated")
        self.price = price
        self.no_pages = no_pages

    def display(self):
        super().display()
        print(f"Price: {self.price}")
        print(f"No of pages: {self.no_pages}")


# Creating an object
book1 = Python("DC", "Aadujeevitham", "Basheer", 540, 250)
book1.display()
