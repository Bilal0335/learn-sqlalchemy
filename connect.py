from dotenv import load_dotenv
from sqlalchemy import create_engine,text
import os

# Step 1: Load the .env file
load_dotenv()

# Step 2: Get the connection string
key = os.getenv("db_url")

engine = create_engine(key,echo=True)


# with engine.connect() as conn:
#     res = conn.execute(text("select 'hello world'"))
#     print(res.all())

# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE my_table (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO my_table (x, y) VALUES (:x, :y)"),
#         [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
#     )
#     conn.commit()


# with engine.begin() as conn:
#     conn.execute(
#         text("INSERT INTO my_table (x, y) VALUES (:x, :y)"),
#         [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
#     )

# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE IF NOT EXISTS myfirst_table (x int, y int)"))

#     conn.execute(text("DELETE FROM myfirst_table"))

#     conn.execute(
#         text("INSERT INTO myfirst_table (x, y) VALUES (:x, :y)"),
#         [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
#     )
#     conn.commit()

#   # Fetch and print inserted data
#     result = conn.execute(text("SELECT * FROM myfirst_table"))
#     for row in result:
#         print(row)


# with engine.connect() as conn:
#     conn.execute(
#         text("CREATE TABLE IF NOT EXISTS first_project (x INt,y INT)")
#     )
#     conn.commit()


# with engine.begin() as conn:
#     conn.execute(
#         text("INSERT INTO first_project (x, y) VALUES (:x, :y)"),
#         [{"x": 16, "y": 8}, {"x": 19, "y": 10}],
#     )

# with engine.connect() as conn:
#     result = conn.execute(
#         text("SELECT * FROM first_project")
#     )
#     print("\nData in my_table:")
#     for row in result:
#         print(row)

