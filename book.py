class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __str__(self) -> str:
        return f"{self.name} ({self.birth_year})"


class Book:
    def __init__(self, title, author: Author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"{self.title} ({self.year}), by {self.author.name}"


# Example Authors
author1 = Author("George Orwell", 1903)
author2 = Author("Jane Austen", 1775)

# Example Books
book1 = Book("1984", author1, 1949)
book2 = Book("Pride and Prejudice", author2, 1813)

print(author1)
print(author2)
print(book1)
print(book2)
