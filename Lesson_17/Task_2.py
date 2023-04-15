class Author:
    def __init__(self, name, country, birthday, books = []):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()

class Book:
    number_of_books = 0

    def __init__(self, name, year, author:Author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'{self.name} - {self.year} - {self.author}'

    def __repr__(self):
        return self.__str__()

class Library:

    def __init__(self, name, books = [], authors = []):
        self.name = name
        self.books = books
        self.authors = authors

    def new_book(self, name: str, year: int, author):
        book = Book(name, year, author)
        Book.number_of_books += 1
        self.books.append(book)
        self.authors.append(author)
        return book

    def group_by_author(self, author):
        books_by_author = []
        if self.authors == []:
           return 'Library is empty'
        else:
           for i in range(len(self.authors)):
              if self.authors[i] == author:
                 books_by_author.append(self.books[i])
           if  books_by_author == []:
              return 'There are no books by the '+str(author)
           else:
              return books_by_author

    def group_by_year(self, year: int):
        books_by_year = []
        if self.books == []:
           return 'Library is empty'
        else:
           for i in range(len(self.authors)):
              if self.books[i].year == year:
                 books_by_year.append(self.books[i])
           if  books_by_year == []:
              return 'There are no books from a '+str(year)
           else:
              return books_by_year

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()


author1 = Author('Arthur Conan Doyle', 'UK', '22 May 1859', ['The Memoirs of Sherlock Holmes','The Hound of the Baskervilles', 'The Valley of Fear'])
author2 = Author('Agatha Christie', 'UK', '15 Sen 1890', ['The Murder of Roger Ackroyd','The Big Four', 'The Mystery of the Blue Train'])
author3 = Author('Rex Stout', 'USA', '15 Sen 1890', ['Fer-De-Lance','The League of Frightened Men', 'Some Buried Caesar'])
library1 = Library('City Library', [],[])
#new_book('The Memoirs of Sherlock Holmes', 1983, author1)
print(library1.new_book('The Memoirs of Sherlock Holmes', 1983, author1))
print(library1.new_book('The League of Frightened Men', 1935, author3))
print(library1.books)
print(library1.group_by_author(author3))
print(Book.number_of_books)
print(library1.group_by_year(1935))
print(library1)