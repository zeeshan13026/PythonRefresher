''' Composition >>>>>>> has a relationship'''
class BookShelf:
    def __init__(self,quantity):
        self.quantity = quantity

    def __str__(self):
        return f"Book shelf with {self.quantity} books"

shelf = BookShelf(500)

#print(shelf)

class Book(BookShelf):
    def __init__(self,name,quantity):
        super().__init__(quantity)
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Potter",500)
print(book)