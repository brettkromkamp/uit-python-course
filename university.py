# Introductory Python Course 2021 - UiT
# By Brett Alistair Kromkamp (brettkromkamp@gmail.com - https://brettkromkamp.com)

from enum import Enum

import uuid


class BaseError(Exception):
    """Base class for exceptions in this module."""

    pass


class BusinessLogicError(BaseError):
    """Raised when an operation attempts to execute invalid business logic."""

    def __init__(self, message):
        self.message = message


class DifficultyLevel(Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0 and value <= 120:
            self.__age = value


class Student(Person):
    def __init__(self, name, age=18, university=None, identifier=None):
        super().__init__(name, age)
        self.university = university
        self.identifier = identifier if identifier else str(uuid.uuid4())
        self.courses = []

    def assign_course(self, course):
        if self.university:  # Is the student enrolled at the university?
            if course in self.university.courses:
                self.courses.append(course)
            else:
                raise BusinessLogicError("Attempt to assign a student to an inexistent course.")
        else:
            raise BusinessLogicError(
                "Attempt to assign a course to a student who has not previously been enrolled into the university."
            )


class Lecturer(Person):
    def __init__(self, name, age=18, university=None, identifier=None):
        super().__init__(name, age)
        self.university = university
        self.identifier = identifier if identifier else str(uuid.uuid4())
        self.courses = []

    def assign_course(self, course):
        if self.university:  # Is the lecturer employed by the university?
            if course in self.university.courses:
                self.courses.append(course)
            else:
                raise BusinessLogicError("Attempt to assign a lecturer to an inexistent course.")
        else:
            raise BusinessLogicError(
                "Attempt to assign a course to a lecturer that is not employed by the university."
            )


class Course:
    def __init__(
        self,
        name,
        university,
        difficulty=DifficultyLevel.BEGINNER,
        year=2021,
        start_week=33,
        end_week=23,
        lecturer=None,
        description="No description provided.",
    ):
        self.name = name
        self.university = university
        self.difficulty = difficulty
        self.year = year
        self.start_week = start_week
        self.end_week = end_week
        self.students = {}
        self.lecturer = lecturer
        self.description = description

        self.university.courses.append(self)

    def enroll_student(self, student):
        if student.university:
            if student.identifier in self.university.students:
                self.students[student.identifier] = student
                student.assign_course(self)
            else:
                raise BusinessLogicError("Attempt to enroll an inexistent university student.")
        else:
            raise BusinessLogicError(
                "Attempt to enroll a student to a course that has not previously been enrolled to the university."
            )

    def assign_lecturer(self, lecturer: Lecturer):
        if lecturer.university:
            if lecturer.identifier in self.university.lecturers:
                self.lecturer = lecturer
                lecturer.assign_course(self)
            else:
                raise BusinessLogicError("Attempt to assign an inexistent lecturer")
        else:
            "Attempt to assign a lecturer to a course that is not employed by the university."


class University:
    def __init__(self, name):
        self.name = name
        self.students = {}
        self.lecturers = {}
        self.courses = []

    def enroll(self, student: Student):
        student.university = self
        self.students[student.identifier] = student

    def employ(self, lecturer):
        lecturer.university = self
        self.lecturers[lecturer.identifier] = lecturer


if __name__ == "__main__":
    # University
    uit_university = University("UiT - Norges Arktiske Universitet")

    # Lecturers
    lucky_luke = Lecturer("Lucky Luke", 27, uit_university)
    marilyn_monroe = Lecturer("Marilyn Monroe", 33, uit_university)

    # Employ the lecturers
    uit_university.employ(lucky_luke)
    uit_university.employ(marilyn_monroe)

    # Courses
    python_intro = Course("Python Programming Introduction", university=uit_university, lecturer=lucky_luke)
    ml_ai = Course(
        "Machine Learning and Artificial Intelligence With Python", university=uit_university, lecturer=marilyn_monroe
    )

    # Students
    albert_einstein = Student("Albert Einstein", 57, university=uit_university)
    isaac_newton = Student("Isaac Newton", 34, uit_university)
    leonardo_da_vinci = Student("Leonardo da Vinci", 47, uit_university)
    niccolo_machiavelli = Student("Niccolò Machiavelli", 39)
    uit_university.enroll(niccolo_machiavelli)

    # Enroll students to the university
    uit_university.enroll(albert_einstein)
    uit_university.enroll(isaac_newton)
    uit_university.enroll(leonardo_da_vinci)

    # Enroll students to courses
    python_intro.enroll_student(albert_einstein)
    python_intro.enroll_student(leonardo_da_vinci)
    python_intro.enroll_student(niccolo_machiavelli)

    ml_ai.enroll_student(albert_einstein)
    ml_ai.enroll_student(isaac_newton)
    ml_ai.enroll_student(leonardo_da_vinci)

    # ========== Queries ==========

    # University
    print("=" * 80)
    print("Starting [University]...")
    for key, student in uit_university.students.items():
        print(f"Student identifier: {key}, name: {student.name}")
    print("-" * 80)
    for key, lecturer in uit_university.lecturers.items():
        print(f"Lecturer name: {lecturer.name}")
    print("-" * 80)
    for course in uit_university.courses:
        print(f"Course name: {course.name}")
    print("=" * 80)

    # Students
    print("=" * 80)
    print("Starting [Students]...")
    for course in albert_einstein.courses:
        print(course.name)
        print(course.lecturer.name)
    print("=" * 80)
    print("Done")
