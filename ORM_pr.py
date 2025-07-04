from typing import List, Optional
from sqlalchemy import ForeignKey, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()
db_url = os.getenv("db_url")

# Create engine for Supabase/Postgres
engine = create_engine(db_url, echo=True)

# 🔹 Base class
class Base(DeclarativeBase):
    pass

# 🔹 User model
class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

# 🔹 Address model
class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

# 🔹 Create tables
Base.metadata.create_all(engine)

# 🔹 Insert Data
with Session(engine) as session:
    ali = User(
        name="Ali",
        fullname="Ali Raza",
        addresses=[
            Address(email_address="ali@gmail.com"),
            Address(email_address="ali.office@example.com"),
        ],
    )
    session.add(ali)
    session.commit()

# 🔹 Read Data
with Session(engine) as session:
    users = session.query(User).all()
    for user in users:
        print(user)
        for addr in user.addresses:
            print("  →", addr)
