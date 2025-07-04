# main.py
from db import engine
from models import Base, Author, Book
from sqlalchemy.orm import Session

# Create tables
Base.metadata.create_all(engine)

# Read and print all authors and books
with Session(engine) as session:
    authors = session.query(Author).all()
    for author in authors:
        print(author)
        for book in author.books:
            print("  →", book)
