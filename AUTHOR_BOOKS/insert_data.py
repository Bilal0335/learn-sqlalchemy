# insert_data.py
from sqlalchemy.orm import Session
from db import engine
from models.author import Author
from models.book import Book

# Insert one author with two books
with Session(engine) as session:
    author = Author(
        name="J.K. Rowling",
        books=[
            Book(title="Harry Potter and the Philosopher's Stone"),
            Book(title="Harry Potter and the Chamber of Secrets")
        ]
    )
    session.add(author)
    session.commit()
