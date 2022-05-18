from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(
                                        title ="Description of the book",
                                        max_length=100,
                                        min_length=1,
                                        )
    rating: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "example": {
                "id": "c07764f6-63a9-47d9-b21f-7eaea16e7f7a",
                "title": "Advetures of Python developer",
                "author": "Carlos Paiva",
                "description": "Its a QA that changing to a developer.",
                "rating": 75
            }
        }

BOOKS = []

@app.get("/")
async def Get_All_Books(books_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        Create_Books_No_Api()

    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i - 1])
            i += 1
        return new_books
    return BOOKS

@app.get("/book/{boo_id}")
async def Get_Specific_Book_By_UUID(book_id:UUID):
    current_book = "Book not found! :("
    for book in BOOKS:
        if book.id == book_id:
            current_book = book
            return current_book

    return current_book

@app.post("/")
async def Create_Book(book: Book):
    BOOKS.append(book)
    return book

def Create_Books_No_Api():
    book_1 = Book(id="fe7424b3-6782-4b5f-85a9-a1278756fe66",
                  title="Title 1",
                  author="Author 1",
                  description="Description 1",
                  rating=60)

    book_2 = Book(id="fe2424b3-6782-4b5f-85a9-a1278756fe67",
                  title="Title 2",
                  author="Author 2",
                  description="Description 2",
                  rating=70)

    book_3 = Book(id="fe3424b3-6782-4b5f-85a9-a1278756fe68",
                  title="Title 3",
                  author="Author 3",
                  description="Description 3",
                  rating=80)
    book_4 = Book(id="fe4424b3-6782-4b5f-85a9-a1278756fe69",
                  title="Title 4",
                  author="Author 4",
                  description="Description 4",
                  rating=90)

    book_5 = Book(id="fe5424b3-6782-4b5f-85a9-a1278756fe70",
                  title="Title 5",
                  author="Author 5",
                  description="Description 5",
                  rating=100)

    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
    BOOKS.append(book_5)












