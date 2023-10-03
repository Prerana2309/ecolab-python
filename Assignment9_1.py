class Book:
    def __init__(self,id,title,author,price,rating):
        self.id=id
        self.title=title
        self.author=author
        self.price=price 
        self.rating=rating
class library:
    def __init__(self):
        self.all_books=[]

    def add_book(self,book):
        self.all_books.append(book)

    def by_ID(self,ID):
        for book in self.all_books:
            if book.id==ID:
                print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
        return f'Wrong ID of book'
    
    def by_author(self,author_name):
        for book in self.all_books:
            if book.author==author_name:
                print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
        return f"Wrong Entry"
    
    def by_rating(self,start,end):
        for book in self.all_books:
            if (book.rating>start and book.rating<end):
                print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
        return 'Book not available in the given range of rating'
    
    def by_price(self,start,end):
        for book in self.all_books:
            if (book.price>start and book.price<end):
                print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
        return None
    
    def info(self):
        for i in self.all_books:
            print(f"ID:{i.id},Title:{i.title},Author:{i.author},Price:{i.price},Rating{i.rating}")


b1=Book(201,"python","Pranav",250,3)
b2=Book(202,"Java","Alisha",130,4)
l=library()
l.add_book(b1)
l.add_book(b2)
print("all_book list:")
l.info()
print("Information of Book with id=102:")
l.by_ID(102)
print("Book written by Pranav:")
l.by_author("Pranav")
print("Book found in range of rating between 3 and 5")
l.by_rating(3,5)
print("Books in price range of 150 and 300")
l.by_price(150,300)