
# ! ==============================
# !   2. models/school_class.py
# ! ==============================

from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String
from typing import TYPE_CHECKING
from typing import List
from db import Base

if TYPE_CHECKING:
    from .students import Student

class SchoolClass(Base):

    __tablename__ = "classes"

    id:Mapped[int] = mapped_column(primary_key=True)
    subject:Mapped[str] = mapped_column(String(50))

    students:Mapped[List["Student"]] = relationship(back_populates="school_class")

    def __repr__(self)->str:
        return f"Class(id={self.id}, subject='{self.subject}')"

