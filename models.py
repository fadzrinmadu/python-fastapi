from sqlalchemy import Column, Integer, Boolean, Float
from sqlalchemy.dialects.mysql import VARCHAR
from database import Base

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
