from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from database import Base

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
    

class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    category = Column(String)
    rating = Column(Float)
    published_date = Column(Integer)
    is_read = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

