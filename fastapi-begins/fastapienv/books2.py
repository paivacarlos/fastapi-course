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

BOOKS = []

@app.get("/")
async def Get_All_Books():
    return BOOKS


@app.post("/")
async def Create_Book(book: Book):
    BOOKS.append(book)
    return book





























