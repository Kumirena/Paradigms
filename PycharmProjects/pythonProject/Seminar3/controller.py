from Seminar3.book import Book
from Seminar3.library import Library
from Seminar3.view import View


class Controller:
    def __init__(self):
        self.library = Library()
        self.view = View()

    def run(self):
        # Главный цикл программы
        while True:
            print("\n1. Добавить книгу")
            print("2. Показать список книг")
            print("3. Выйти")
            choice = input("Выберите действие: ")

            if choice == "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                book = Book(title, author)
                self.library.add_book(book)
            elif choice == "2":
                books = self.library.get_books()
                self.view.show_books(books)
            elif choice == "3":
                print("Выход из программы.")
                break
            else:
                print("Некорректный выбор. Попробуйте снова.")