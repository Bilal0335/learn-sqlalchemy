from connect import engine
from sqlalchemy import text

# with engine.connect() as conn:
#     result = conn.execute(
#         text("SELECT name, marks FROM students WHERE marks > :min_marks"),
#         {"min_marks": 70}
#     )
#     print("Students with marks > 70:\n")
#     for row in result:
#         print(f"Name: {row.name}, Marks: {row.marks}")


#!  pratice # 01
# with engine.connect() as conn:
#     result = conn.execute(
#         text("SELECT name, age FROM students WHERE age <= :max_age"),
#         {"max_age": 20}
#     )
#     print("Students with age less than 20:\n")
#     for row in result:
#         print(f"Name: {row.name}, Age: {row.age}")


# ! Pratice # 02
# with engine.connect() as conn:
#     result = conn.execute(
#         text("SELECT name, marks FROM students WHERE name = :student_name"),
#         {"student_name": "Bilal"}
#     )
#     print("Details of student named Sana:\n")
#     for row in result:
#         print(f"Name: {row.name}, Marks: {row.marks}")

# ! Pratice # 03
with engine.connect() as conn:
    result = conn.execute(
        text("SELECT name, marks, age FROM students WHERE marks > :min_marks AND age < :max_age"),
        {"min_marks": 60, "max_age": 20}
    )
    print("Students with marks > 60 and age < 20:\n")
    for row in result:
        print(f"Name: {row.name}, Marks: {row.marks}, Age: {row.age}")