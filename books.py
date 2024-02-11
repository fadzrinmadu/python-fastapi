from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:
  id: int
  title: str
  author: str
  description: str
  category: str
  rating: float
  published_date: int
  is_read: bool
  
  def __init__(self, id, title, author, description, category, rating, published_date, is_read):
    self.id = id
    self.title = title
    self.author = author
    self.description = description
    self.category = category
    self.rating = rating
    self.published_date = published_date
    self.is_read = is_read


books_data = [
  {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Fiction", "description": "A tale of wealth, love, and the American Dream.", "rating": 4.5, "published_date": 1925, "is_read": False},
  {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Classics", "description": "A powerful exploration of racial injustice in the American South.", "rating": 4.8, "published_date": 1960, "is_read": False},
  {"id": 3, "title": "1984", "author": "George Orwell", "category": "Dystopian", "description": "A dystopian novel depicting a totalitarian society.", "rating": 4.7, "published_date": 1949, "is_read": False},
  {"id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "category": "Coming of Age", "description": "A classic coming-of-age novel capturing teenage angst.", "rating": 4.2, "published_date": 1951, "is_read": False},
  {"id": 5, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "category": "Fantasy", "description": "The first book in the magical Harry Potter series.", "rating": 4.9, "published_date": 1997, "is_read": False},
  {"id": 6, "title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Adventure", "description": "An epic fantasy adventure of Bilbo Baggins.", "rating": 4.6, "published_date": 1937, "is_read": False},
  {"id": 7, "title": "Pride and Prejudice", "author": "Jane Austen", "category": "Classics", "description": "A classic novel exploring love, marriage, and social status.", "rating": 4.4, "published_date": 1813, "is_read": False},
  {"id": 8, "title": "Animal Farm", "author": "George Orwell", "category": "Dystopian", "description": "An allegorical novella depicting a farm's rebellion against humans.", "rating": 4.7, "published_date": 1945, "is_read": False},
  {"id": 9, "title": "Brave New World", "author": "Aldous Huxley", "category": "Dystopian", "description": "A dystopian novel exploring a society obsessed with happiness.", "rating": 4.6, "published_date": 1932, "is_read": False},
  {"id": 10, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "category": "Fantasy", "description": "An epic fantasy trilogy set in the world of Middle-earth.", "rating": 4.9, "published_date": 1954, "is_read": False},
  {"id": 11, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "category": "Coming of Age", "description": "A classic coming-of-age novel capturing teenage angst.", "rating": 4.2, "published_date": 1951, "is_read": False},
  {"id": 12, "title": "The Chronicles of Narnia", "author": "C.S. Lewis", "category": "Fantasy", "description": "A series of seven fantasy novels set in the magical land of Narnia.", "rating": 4.8, "published_date": 1950, "is_read": False},
  {"id": 13, "title": "Jane Eyre", "author": "Charlotte Brontë", "category": "Classics", "description": "A classic novel depicting the life of an orphaned girl.", "rating": 4.5, "published_date": 1847, "is_read": False},
  {"id": 14, "title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "category": "Magical Realism", "description": "A landmark novel blending reality and fantasy in the town of Macondo.", "rating": 4.7, "published_date": 1967, "is_read": False},
  {"id": 15, "title": "The Shining", "author": "Stephen King", "category": "Horror", "description": "A psychological horror novel set in an isolated hotel.", "rating": 4.3, "published_date": 1977, "is_read": False},
  {"id": 16, "title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "category": "Science Fiction", "description": "A humorous science fiction series exploring the galaxy.", "rating": 4.6, "published_date": 1979, "is_read": False},
  {"id": 17, "title": "The Hunger Games", "author": "Suzanne Collins", "category": "Dystopian", "description": "A dystopian novel set in a post-apocalyptic world.", "rating": 4.5, "published_date": 2008, "is_read": False},
  {"id": 18, "title": "The Alchemist", "author": "Paulo Coelho", "category": "Philosophical Fiction", "description": "A philosophical novel following a journey of self-discovery.", "rating": 4.8, "published_date": 1988, "is_read": False},
  {"id": 19, "title": "Wuthering Heights", "author": "Emily Brontë", "category": "Gothic Fiction", "description": "A tale of love and revenge on the Yorkshire moors.", "rating": 4.4, "published_date": 1847, "is_read": False},
  {"id": 20, "title": "Frankenstein", "author": "Mary Shelley", "category": "Gothic Science Fiction", "description": "A classic novel exploring the consequences of playing god.", "rating": 4.6, "published_date": 1818, "is_read": False}
]


BOOKS = [Book(**book_data) for book_data in books_data]


class BookRequest(BaseModel):
  id: Optional[int] = Field(default=None, title="id is not needed")
  title: str = Field(min_length=3)
  author: str = Field(min_length=3)
  description: str = Field(min_length=3, max_length=100)
  category: str = Field(min_length=3)
  rating: float = Field(gt=-1, lt=6)
  published_date: int = Field(gt=1999, lt=2031)
  is_read: bool
  
  class Config:
    json_schema_extra = {
      "example": {
        "title": "A New Book",
        "author": "Fadzrin Madu",
        "description": "Simple description for the best book in the world",
        "category": "Horor",
        "rating": 5,
        "published_date": 2024,
        "is_read": False
      }
    }
  

@app.get("/books", status_code=status.HTTP_200_OK)
async def reads_all_books():
  return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
  for book in BOOKS:
    if book.id == book_id:
      return book
  raise HTTPException(status_code=404, detail="Item not found")
    

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: float = Query(gt=0, lt=6)):
  books_to_return = []
  
  for book in BOOKS:
    if book.rating == book_rating:
      books_to_return.append(book)
  
  return books_to_return


@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(published_date: int = Query(gt=1999, lt=2031)):
  books_to_return = []
  
  for book in BOOKS:
    if book.published_date == published_date:
      books_to_return.append(book)
      
  return books_to_return


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
  new_book = Book(**book_request.model_dump())
  BOOKS.append(find_book_id(new_book))
  

def find_book_id(book: Book):
  book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
  return book


@app.put("/books", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
  book_changed = False
  
  for i in range(len(BOOKS)):
    if BOOKS[i].id == book.id:
      BOOKS[i] = book
      book_changed = True
      
  if not book_changed:
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
  for i in range(len(BOOKS)):
    if BOOKS[i].id == book_id:
      BOOKS.pop(i)
      break
