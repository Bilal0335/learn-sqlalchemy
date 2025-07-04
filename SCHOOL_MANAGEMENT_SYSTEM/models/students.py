
# ! ==============================
# !   2. models/school_class.py
# ! ==============================

# models/student.py

from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from db import Base

if TYPE_CHECKING:
    from .school_class import SchoolClass

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    unique_id: Mapped[str] = mapped_column(String(20), unique=True)
    name: Mapped[str] = mapped_column(String(50))
    father_name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer)
    address: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))

    school_class: Mapped["SchoolClass"] = relationship(back_populates="students")

    def __repr__(self) -> str:
        return f"Student(id={self.id}, name={self.name}, email={self.email})"

