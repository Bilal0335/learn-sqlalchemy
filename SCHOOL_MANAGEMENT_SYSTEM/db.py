
# ! ==============================
# !         1. db.py
# ! ==============================
from dotenv import load_dotenv
import os
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine


# Load environment variables from .env file
load_dotenv()
db_url = os.getenv("db_key")
engine = create_engine(db_url,echo=True)

class Base(DeclarativeBase):
    pass