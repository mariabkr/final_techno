from app.schemas import Book
from app.database import database



def save_book(add_new_book: Book) -> Book:
    database["books"].append(add_new_book)
    return add_new_book



def display_list_of_book_and_number() -> list[Book]:  
    for livre in database["livres"]:
       books_liste= [livre]
    return books_liste


def get_book_by_id(book_id: str) -> Book | None:
    selected_book = [
        book for book in database["books"]
        if book["id"] == book_id
    ]
    if len(selected_book) < 1:
        return None
    selected_book = Book.model_validate(selected_book[0])
    return selected_book