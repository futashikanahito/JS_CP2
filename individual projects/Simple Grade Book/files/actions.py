# [1] Add New Student, [2] Add Grade to Student, [3] View Student Record, [4] View All Students, [5] Class Summary
from classes import Student
import os

#---------------------- [1] Add New Student ----------------------
def add_student(book):
    name = input("""=====================================
          ADD NEW STUDENT 
=====================================
                 
Enter student name: """)
    stu_id = input("Enter student ID: ")
    while isinstance(stu_id, int) and stu_id != "":
        stu_id = input("Make sure id is an integer. Enter student ID: ")
    print(f"""
Student added successfully!
    Name: {name}
    ID: {stu_id}
    Grades: None
""")
    input("Press Enter to continue...")

    book.add_student(Student(name, stu_id, grades=[]))
    return book

#---------------------- [2] Add Grade to Student ----------------------
def add_grade(book):
    os.system("cls")
    print("""
=====================================
            ADD GRADE
=====================================
Current Students: """)
    for student in book.list:
        print(f"- {student}")
    
    current = None
    check = input("Enter student ID: ")
    for student in book.list:
        if student.id == check:
            student = current
    grade = input(f"Enter grade (0 - 100): ")

    current.add_grade(grade)

    print(f"""
Grade added successfully!
   {current.name} now has {len(current.grades)} grade(s)
   Current average: {current.avg} ({current.letter})
""")
    
    student.update()
    return book

#---------------------- [3] View Student Record ----------------------
def view_student():
    pass

#---------------------- [4] View All Students ----------------------
def view_all(book):
    print("""
┌─────────────────────────────────────┐
│ ID │ Name │ Avg │ Grade             │
├─────────────────────────────────────┤""")
    for student in book.list:
        print(f"│ {student.id} │ {student.name} │ {student.avg} │ {student.letter} │") 
    print(f"└─────────────────────────────────────┘\nTotal Students: {len(book.list)}")
    input("Press Enter to continue...")

#---------------------- [5] Class Summary ----------------------
def summary():
    pass
"""===============================
       CLASS STATISTICS 
===============================
Total Students: 5
Class Average: 84.2 (B)
Highest Average: 98
Lowest Average: 67
Highest Assignment: 100
Lowest Assignment: 0
==============================="""

#---------------------- [6] Search Students ----------------------
def search(book):
    method = input("How would you like to search? (id/name) ")
    if method != "id" and method != "name":
        method = input("Make sure your answer is either id or name. How would you like to search? (id/name) ")
    search = input("What would you like to search? ")
    book.find_student(search, method)
    input("Press Enter to continue...")