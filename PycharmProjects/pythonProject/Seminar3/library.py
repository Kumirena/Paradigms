import book


class Library:
    def __init__(self):
        self.books = []

    # Функция для добавления книги в библиотеку
    def add_book(self, book):
        self.books.append(book)
        print("Книга добавлена в библиотеку.")

    def get_books(self):
        return self.books