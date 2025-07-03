from connect import engine
from models import Base

# ! Create all tables in the database
Base.metadata.create_all(engine)





# ! Example 01
# from sqlalchemy import text

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x, y FROM first_project"))
#     for row in result:
#         print(f"x: {row.x}  y: {row.y}")


# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x, y FROM first_project WHERE y > :y"), {"y": 2})
#     for row in result:
#         print(f"x: {row.x}  y: {row.y}")