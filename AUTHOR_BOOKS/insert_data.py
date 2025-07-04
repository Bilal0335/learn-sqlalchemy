# # insert_data.py
# from sqlalchemy.orm import Session
# from db import engine
# from models.author import Author
# from models.book import Book

# # Insert one author with two books
# with Session(engine) as session:
#     author = Author(
#         name="J.K. Rowling",
#         books=[
#             Book(title="Harry Potter and the Philosopher's Stone"),
#             Book(title="Harry Potter and the Chamber of Secrets")
#         ]
#     )
#     session.add(author)
#     session.commit()


from sqlalchemy.orm import Session
from db import engine
from models.author import Author
from models.book import Book

# Insert multiple authors, each with multiple books
with Session(engine) as session:
    authors = [
        Author(
            name="J.K. Rowling",
            books=[
                Book(title="Harry Potter and the Philosopher's Stone"),
                Book(title="Harry Potter and the Chamber of Secrets")
            ]
        ),
        Author(
            name="J.R.R. Tolkien",
            books=[
                Book(title="The Hobbit"),
                Book(title="The Lord of the Rings")
            ]
        ),
        Author(
            name="George R.R. Martin",
            books=[
                Book(title="A Game of Thrones"),
                Book(title="A Clash of Kings")
            ]
        )
    ]

    session.add_all(authors)
    session.commit()
