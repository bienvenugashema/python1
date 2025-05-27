class Book:
    books = dict()
    def __init__(this, title, author, pages:int):
        this.title = title
        this.author = author
        this.pages = pages

    @classmethod
    def add_book(cls, title, author, pages):
        book = dict()
        obj = cls(title,author,pages)
        book['author'] = obj.author
        book['pages'] = obj.pages
        cls.books[obj.title] = book

        for key, values in  cls.books.items():
            return f"Book name is: {key}, Author: { (x for x in cls.books.items())}"

obj = Book.add_book("Mathematics", "Mwimule Bienvenu", 90)
print(obj)    
        