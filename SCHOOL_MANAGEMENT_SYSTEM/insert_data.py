from models import Student, SchoolClass
from db import engine
from sqlalchemy.orm import Session

with Session(engine) as session:
    # Create a new class
    cs_class = SchoolClass(subject="Computer Science")
    session.add(cs_class)
    session.flush()  # Makes cs_class.id available

    # List of students
    student_list = [
        Student(
            unique_id="STD-001",
            name="Ahmed Khan",
            father_name="Zafar Khan",
            age=21,
            address="123 Main St, Lahore",
            email="ahmed.khan@example.com",
            class_id=cs_class.id,
        ),
        Student(
            unique_id="STD-002",
            name="Sara Ali",
            father_name="Nadeem Ali",
            age=22,
            address="456 Park Rd, Karachi",
            email="sara.ali@example.com",
            class_id=cs_class.id,
        ),
        Student(
            unique_id="STD-003",
            name="Usman Tariq",
            father_name="Tariq Mehmood",
            age=20,
            address="789 Canal Rd, Faisalabad",
            email="usman.tariq@example.com",
            class_id=cs_class.id,
        ),
    ]

    # 👇 This part prevents duplicate insert
    for student in student_list:
        existing_student = session.query(Student).filter_by(unique_id=student.unique_id).first()
        if not existing_student:
            session.add(student)
        else:
            print(f"{student.unique_id} already exists, skipping.")

    session.commit()
