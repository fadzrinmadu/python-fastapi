from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

MYSQL_USERNAME = os.getenv("MYSQL_USERNAME", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "root")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "db_booksapp")

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
