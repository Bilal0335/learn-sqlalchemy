from connect import engine
from sqlalchemy import text

with engine.connect() as conn:
    # Create table
    conn.execute(text(
        "CREATE TABLE IF NOT EXISTS students (id SERIAL PRIMARY KEY, name VARCHAR, age INT, marks INT)"
    ))
    conn.commit()

    # Clear table first
    conn.execute(text("DELETE FROM students"))
    conn.commit()

    # Insert multiple rows
    conn.execute(
        text("INSERT INTO students (name, age, marks) VALUES (:name, :age, :marks)"),
        [
            {"name": "Ali", "age": 18, "marks": 85},
            {"name": "Sana", "age": 20, "marks": 90},
            {"name": "Bilal", "age": 17, "marks": 45},
            {"name": "Ayesha", "age": 22, "marks": 72},
        ]
    )
    conn.commit()
