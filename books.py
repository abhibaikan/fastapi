from fastapi import FastAPI,Body
import logging
from pydantic import BaseModel

app = FastAPI()
logging.basicConfig(level=logging.INFO)


class Book:
    def __init__(self, id: int, title: str, author: str):
        self.id = id
        self.title = title
        self.author = author

class BookModel(BaseModel):
    id: int
    title: str
    author: str
        

BOOKS = [ Book(1, "1984", "George Orwell"),
          Book(2, "To Kill a Mockingbird", "Harper Lee"),
          Book(3, "The Great Gatsby", "F. Scott Fitzgerald") ]

@app.get("/books")
async def get_books():
    return BOOKS

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for i in BOOKS:
        if i.id == book_id:
            return i    
    return {"error": "Book not found"}, 404

@app.post("/create-books")
async def create_book(book: BookModel):
    if any(b.id == book.id for b in BOOKS):
        logging.error(f"Book with id {book.id} already exists.")
        return {"error": "Book with this ID already exists"}, 400
    id = max(b.id for b in BOOKS) + 1 if BOOKS else 1
    book.id = id
    new_book = Book(id=book.id, title=book.title, author=book.author)
    BOOKS.append(new_book)
    logging.info(f"Book created: {new_book}")
    return new_book



