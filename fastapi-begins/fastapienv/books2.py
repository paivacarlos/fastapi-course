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
async def Get_All_Books():
    if len(BOOKS) < 1:
        return {"message":"There is no book avalible"}
    return BOOKS


@app.post("/")
async def Create_Book(book: Book):
    BOOKS.append(book)
    return book












