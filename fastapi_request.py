from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category


BOOKS = [
    Book('Title One', 'Author One', 'science'),
    Book('Title Two', 'Author Two', 'science'),
    Book('Title Three', 'Author Three', 'history'),
    Book('Title Four', 'Author Four', 'math'),
    Book('Title Five', 'Author Five', 'math'),
    Book('Title Six', 'Author Two', 'math'),
    Book('Title Six', 'Author Two', 'math')
]

class BookRequest(BaseModel):
    tile: str = Field(..., description="Title of the book")
    author: str = Field(..., description="Author of the book")
    category: str = Field(..., description="Category of the book")
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category



@app.get("/list_books/")
def read_root():
    return BOOKS

@app.post("/add_book/")
def add_book(book: BookRequest):
    BOOKS.append(**book.dict())
    return BOOKS