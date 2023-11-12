from seminar3.library import Library


class View:

    # Функция для вывода списка книг в библиотеке

    def show_books(self, books):
        if not books:
            print("Библиотека пуста.")
        else:
            print("Список книг в библиотеке:")
            for book in books:
                print(f"Название: {book.title}, Автор: {book.author}")