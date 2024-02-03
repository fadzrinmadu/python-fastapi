from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
  {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Fiction"},
  {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Classics"},
  {"title": "1984", "author": "George Orwell", "category": "Dystopian"},
  {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "category": "Coming of Age"},
  {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "category": "Fantasy"},
  {"title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Adventure"},
  {"title": "Pride and Prejudice", "author": "Jane Austen", "category": "Classics"},
  {"title": "Animal Farm", "author": "George Orwell", "category": "Dystopian"},
  {"title": "Brave New World", "author": "Aldous Huxley", "category": "Dystopian"},
  {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "category": "Fantasy"},
  {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "category": "Coming of Age"},
  {"title": "The Chronicles of Narnia", "author": "C.S. Lewis", "category": "Fantasy"},
  {"title": "Jane Eyre", "author": "Charlotte Brontë", "category": "Classics"},
  {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "category": "Magical Realism"},
  {"title": "The Shining", "author": "Stephen King", "category": "Horror"},
  {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "category": "Science Fiction"},
  {"title": "The Hunger Games", "author": "Suzanne Collins", "category": "Dystopian"},
  {"title": "The Alchemist", "author": "Paulo Coelho", "category": "Philosophical Fiction"},
  {"title": "Wuthering Heights", "author": "Emily Brontë", "category": "Gothic Fiction"},
  {"title": "Frankenstein", "author": "Mary Shelley", "category": "Gothic Science Fiction"}
]

@app.get("/books")
async def reads_all_books():
  return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
  for book in BOOKS:
    if book.get("title").casefold() == book_title.casefold():
      return book


@app.get("/books/")
async def read_category_by_query(category: str):
  books_to_return = []
  
  for book in BOOKS:
    if book.get("category").casefold() == category.casefold():
      books_to_return.append(book)
      
  return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
  books_to_return = []
  
  for book in BOOKS:
    if book.get("author").casefold() == book_author.casefold() and \
        book.get("category").casefold() == category.casefold():
      books_to_return.append(book)
  
  return books_to_return


@app.post("/books")
async def create_book(new_book=Body()):
  BOOKS.append(new_book)


@app.put("/books")
async def update_book(updated_book=Body()):
  for i in range(len(BOOKS)):
    if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
      BOOKS[i] = updated_book


@app.delete("/books/{book_title}")
async def delete_book(book_title: str):
  for i in range(len(BOOKS)):
    if BOOKS[i].get("title").casefold() == book_title.casefold():
      BOOKS.pop(i)
      break
