from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/list_books/")
def read_root():
    return BOOKS

@app.get("/filter_books/{title}")
def read_root(title: str):
    for book in BOOKS:
        if title == book['title']:
            return book
        
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

@app.get("/books/{author}/")
def fetch_all_books_author(author:str):
  b=[]
  for book in BOOKS:
      if author == book['author']:
          b.append(book)
  return b

@app.post("/add_book/")
def create_book(title: str, author: str, category: str):
    book = {'title': title, 'author': author, 'category': category}
    BOOKS.append(book)
    return book

@app.put("/update_book/{title}")
def update_book(title: str, author: str, category: str):
    for book in BOOKS:
        if title == book['title']:
            book['author'] = author
            book['category'] = category
            return book
        
@app.delete("/delete_book/{title}")
def delete_book(title: str):
    for book in BOOKS:
        if title == book['title']:
            BOOKS.remove(book)
            return book