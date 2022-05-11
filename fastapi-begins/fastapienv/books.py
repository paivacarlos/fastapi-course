from fastapi import FastAPI

app = FastAPI()

books = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'}
}

@app.get("/")
async def first_api():
    return {"message": "Hello, Mr Paiva, our new Sofware Engineer!"}

@app.get("/all-books")
async def Get_All_Books():
    return books

@app.get("/specific-book/{book_id}")
async def Get_Specific_Book(book_id: str):
    book_id_found = "Book not found!"
    for current_book in books:
        if current_book == book_id:
            book_id_found = books[book_id]
    return book_id_found

@app.get("/by-name-book/{name_book}")
async def Get_Book_By_Name(name_book: str):
    book_name_found = "Book not found!"
    for current_name_book in books.values():
        print(current_name_book)
        if current_name_book["title"] == name_book:
            book_name_found = current_name_book
    return book_name_found

@app.get("/by-author-book/{author_book}")
async def Get_Book_By_Author(author_book: str):
    author_book_found = "Book not found!"
    for current_author_book in books.values():
        print(current_author_book["author"])
        if current_author_book["author"] == author_book:
            author_book_found = current_author_book
    return author_book_found

@app.post("/")
async def Create_Book(book_title, book_author):
    current_book_id = 0

    if len(books) > 0:
        for book in books:
            x = int(book.split('_')[-1])
            print("Aqui", x)
            if x > current_book_id:
                current_book_id = x

    books[f'book_{current_book_id + 1}'] = {'title': book_title, 'author': book_author}

    return books[f'book_{current_book_id + 1}']






























































