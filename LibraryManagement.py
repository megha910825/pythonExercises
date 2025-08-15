# 2. Library Management
# Scenario: A library wants to digitize its book records.

# Task:

# Create a Book class with attributes: title, author, isbn, and status (available/borrowed).
# Add methods to change the status of a book (borrow/return).
# Create a list of books and implement functionality to search for a book by title or author.

class Book:
    def __init__(self,title,author,isbn,status):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.status=status
    def changestatus(self,task):
        if task=="borrow":
          self.status="borrowed"
        elif task=="return":
          self.status="available"
    def searchbook(self,title,author):
       return self.isbn
    
b1=Book("ABC","Megha",123,"borrowed")
b2=Book("CDE","Deepak",101,"available")
b3=Book("EFG","Akshay",121,"available")
book_list=[b1,b2,b3]

user_title=input("Enter title of the book::")
user_author=input("Enter the book author::")

for key in book_list:
   isbn=key.searchbook(user_title,user_author)
   if isbn==key.isbn:
    print("Book found")
    break
