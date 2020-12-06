''' Use of class method '''
class Book:

    TYPE = ('Hardcover', 'Paperback')
    def __init__(self,name,book_type,weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls,name,page_weight):
        return Book(name, Book.TYPE[0],page_weight+100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPE[1], page_weight)

book = Book('Harry Potter', 'PaperBack', 1000)
print(book)

book = Book.hardcover('Harry',300)
light = Book.paperback('python',100)

print(book)
print(light)







