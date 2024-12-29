import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Teacher, Student, Group, Grade , Subject


fake = Faker('uk-UA')


def insert_group():
    for i in range(1, 4):
        group = Group(
            id = i,
            name = fake.word()
        )
        session.add(group)

def insert_students():
    for i in range(1, 51):
        student = Student(
            fullname=fake.name(),
            id = i,
            group_id = random.randint(1,3)
        )
        session.add(student)


def insert_teachers():
    for i in range(1, 6):
        teacher = Teacher(
            id = i,
            fullname=fake.name(),
        )
        session.add(teacher)


def insert_subjects():
    for i in range(1, 9):
        subject = Subject(
            id = i,
            name = fake.word(),
            teacher_id = random.randint(1, 5)
        )
        session.add(subject)

def insert_grades():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(10, 20)):
                grade = Grade(
                    grade=random.randint(0, 100),
                    grade_date=fake.date_this_year(),
                    student_id=student.id,
                    subjects_id=subject.id
                )
                session.add(grade)


if __name__ == '__main__':
    try:
        insert_group()
        insert_students()
        insert_teachers()
        insert_subjects()
        insert_grades()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
