from sqlalchemy import Column, Integer, Boolean, Float, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR
from database import Base

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(VARCHAR(length=255), unique=True)
    username = Column(VARCHAR(length=255), unique=True)
    first_name = Column(VARCHAR(length=255))
    last_name = Column(VARCHAR(length=255))
    hashed_password = Column(VARCHAR(length=255))
    is_active = Column(Boolean, default=True)
    role = Column(VARCHAR(length=255))
    

class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(length=255))
    author = Column(VARCHAR(length=255))
    description = Column(VARCHAR(length=255))
    category = Column(VARCHAR(length=255))
    rating = Column(Float)
    published_date = Column(Integer)
    is_read = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

