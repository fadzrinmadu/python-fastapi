from typing import Annotated, Optional
from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

from models import Books
from database import SessionLocal
from starlette import status
from .auth import get_current_user

router = APIRouter()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
    
    
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


class BookRequest(BaseModel):
  id: Optional[int] = Field(default=None, title="id is not needed")
  title: str = Field(min_length=3)
  author: str = Field(min_length=3)
  description: str = Field(min_length=3, max_length=100)
  category: str = Field(min_length=3)
  rating: float = Field(gt=-1, lt=6)
  published_date: int = Field(gt=1999, lt=2031)
  is_read: bool = Field(default=False)
  
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


@router.get("/books/")
async def get_all_books(
  user: user_dependency,
  db: db_dependency,
):
  if user is None:
    raise HTTPException(status_code=401, detail="Authentication Failed")
  
  books = db.query(Books).filter(Books.owner_id == user.get("id")).all()
  return books


@router.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(
  user: user_dependency,
  db: db_dependency, 
  book_id: int = Path(gt=0)
):
  if user is None:
    raise HTTPException(status_code=401, detail="Authentication Failed")
  
  book_model = db.query(Books)\
    .filter(Books.id == book_id)\
    .filter(Books.owner_id == user.get("id")).first()
  
  if book_model is not None:
    return book_model
  raise HTTPException(status_code=404, detail="Book not found.")


@router.post("/books/", status_code=status.HTTP_201_CREATED)
async def create_book(
  user: user_dependency,
  db: db_dependency, 
  book_request: BookRequest
):
  if user is None:
    raise HTTPException(status_code=401, detail="Authentication Failed")
  
  book_model = Books(
    **book_request.model_dump(),
    owner_id=user.get("id"),
  )
  
  db.add(book_model)
  db.commit()


@router.put("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_book_by_id(
  user: user_dependency,
  db: db_dependency, 
  book_request: BookRequest,
  book_id: int = Path(gt=0), 
):
  if user is None:
    raise HTTPException(status_code=401, detail="Authentication Failed")
  
  book_model = db.query(Books)\
    .filter(Books.id == book_id)\
    .filter(Books.owner_id == user.get("id")).first()
  
  if book_model is None:
    raise HTTPException(status_code=404, detail="Book not found.")
  
  book_model.title = book_request.title
  book_model.author = book_request.author
  book_model.description = book_request.description
  book_model.category = book_request.category
  book_model.rating = book_request.rating
  book_model.published_date = book_request.published_date
  book_model.is_read = book_request.is_read
  
  db.add(book_model)
  db.commit()


@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_by_id(
  user: user_dependency,
  db: db_dependency, 
  book_id: int = Path(gt=0)
):
  if user is None:
    raise HTTPException(status_code=401, detail="Authentication Failed")
  
  book_model = db.query(Books)\
    .filter(Books.id == book_id)\
    .filter(Books.owner_id == user.get("id")).first()
  
  if book_model is None:
    raise HTTPException(status_code=404, detail="Book not found.")
  
  db.query(Books)\
    .filter(Books.id == book_id)\
    .filter(Books.owner_id == user.get("id")).delete()
  db.commit()
