# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os

# Load environment variable
load_dotenv()
db_url = os.getenv("db_url")

# Create engine
engine = create_engine(db_url, echo=True)

# Base class
class Base(DeclarativeBase):
    pass
