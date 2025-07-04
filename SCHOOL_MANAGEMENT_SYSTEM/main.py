from db import engine
from models import Base, Student, SchoolClass
from sqlalchemy.orm import Session

# Create tables
# Create tables
Base.metadata.drop_all(engine)  # Drop all existing tables
Base.metadata.create_all(engine)  # Then recreate with updated schema


# Read and print
with Session(engine) as session:
    classes = session.query(SchoolClass).all()
    for cls in classes:
        print(cls)
        for student in cls.students:
            print("  →", student)