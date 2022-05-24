from fastapi import FastAPI, HTTPException, Request, status, Form, Header
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from starlette.responses import JSONResponse

app = FastAPI()

class Negative_Number_Exception(Exception):
    def __init__(self, books_to_return):
        self.books_to_return = books_to_return

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

class BookNoRating(BaseModel):
    id:UUID
    title: str = Field(min_lenght=1)
    author: str
    description: Optional[str] = Field(
        None,
        title="Descripton of the books",
        max_lenght=100,
        min_lenght=1
    )

BOOKS = []

@app.exception_handler(Negative_Number_Exception)
async def Negative_Number_Exception_Handler(request: Request,
                                            exception: Negative_Number_Exception):
    return JSONResponse(
        status_code= 418,
        content={"message": f"There is no id for this {exception.books_to_return}"}
    )

@app.post("/books/login")
async def Book_Login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}

@app.get("/header")
async def Read_Header(random_header: Optional[str] = Header(None)):
    return {"Random-Header":random_header}

@app.get("/")
async def Get_All_Books(books_to_return: Optional[int] = None):
    if books_to_return and books_to_return < 0:
        raise Negative_Number_Exception(books_to_return=books_to_return)

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
            return book

    raise HTTPException(status_code=404, detail="Book not found! :(")

@app.get("/book/rating/{boo_id}", response_model=BookNoRating)
async def Get_Specific_Book_By_UUID_No_Rating(book_id:UUID):
    current_book = "Book not found! :("
    for book in BOOKS:
        if book.id == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found! :(")

@app.put("/{book_id}")
async def Update_Book_By_UUID(book_id: UUID, book: Book):
    counter = 0
    for current_book in BOOKS:
        counter += 1
        if current_book.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]

    raise raise_item_cannot_be_found_exception()

@app.post("/", status_code=status.HTTP_201_CREATED)
async def Create_Book(book: Book):
    BOOKS.append(book)
    return book

@app.delete("/{book_id}")
async def Delete_Book_By_UUID(book_id: UUID):
    counter = 0

    for current_book in BOOKS:
        counter += 1
        if current_book.id == book_id:
            del BOOKS[counter - 1]
            return f'ID:{book_id} deleted!'

    raise raise_item_cannot_be_found_exception()


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


def raise_item_cannot_be_found_exception():
    return HTTPException(status_code=404, detail="Book not found! :(",
                  headers={"X-Header-Error": "Nothing to be seen at the UUID."})









