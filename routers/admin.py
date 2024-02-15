from typing import Annotated, Optional
from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

from models import Books
from database import SessionLocal
from starlette import status
from .auth import get_current_user

router = APIRouter(
  prefix="/admin",
  tags=["admin"],
)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
    
    
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/todo", status_code=status.HTTP_200_OK)
async def get_all_books(user: user_dependency, db: db_dependency):
  if user is None or user.get("user_role") != "admin":
    raise HTTPException(status_code=401, detail="Authentication Failed")
  
  books = db.query(Books).all()
  return books


@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_by_id(
  user: user_dependency,
  db: db_dependency, 
  book_id: int = Path(gt=0)
):
  if user is None or user.get("user_role") != "admin":
    raise HTTPException(status_code=401, detail="Authentication Failed")
  
  book_model = db.query(Books)\
    .filter(Books.id == book_id).first()
  
  if book_model is None:
    raise HTTPException(status_code=404, detail="Book not found.")
  
  db.query(Books)\
    .filter(Books.id == book_id).delete()
  db.commit()
