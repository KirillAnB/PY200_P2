from book_gen import get_random_book

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 100,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book():
    """Класс-конструктор экземпляра книги"""

    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError(f"Check book id(id should be {int}")
        self.id_ = id_
        if not isinstance(name, str):
            raise TypeError(f"Check book name(book name should be {str}")
        self.name = name
        if not isinstance(pages, int):
            raise TypeError(f"Check pages number(Should be {int}")
        if pages < 0 or pages == 0:
            raise ValueError("Pages number should not be negative or equal to 0")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id_={self.id_}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    random_books_generator = get_random_book()
    BOOKS_DATABASE_2 = [next(random_books_generator) for _ in range(3)]
    list_books = [
        Book(id_=book_dict["pk"], name=book_dict["fields"]['title'], pages=book_dict["fields"]['pages']) for book_dict in BOOKS_DATABASE_2
    ]

    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
