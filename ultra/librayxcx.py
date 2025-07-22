class Book:
    def __init__(self, title, author, year):
         self.title = title
         self.author = author
         self.year = year

    def display_info(self):
            print(f"📘 {self.title} by {self.author} {self.year}")

# Create book objects
book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997)
book2 = Book("Charlotte's Web", "E.B. White", 1952)
book3 = Book("The Cat in the Hat", "Dr. Seuss", 1957)

# Print book details
book1.display_info()
book2.display_info()
book3.display_info()
