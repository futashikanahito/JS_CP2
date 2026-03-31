# [1] Add New Student, [2] Add Grade to Student, [3] View Student Record, [4] View All Students, [5] Class Summary
from classes import Student
import os

#---------------------- [1] Add New Student ----------------------
def add_student(book):
    name = input("""
=====================================
          ADD NEW STUDENT 
=====================================
                 
Enter student name: """)
    stu_id = input("Enter student ID: ")
    while not stu_id.isdigit() or any(stu_id == p.id for p in book.list):
        if not stu_id.isdigit():
            stu_id = input("Make sure the ID is an integer. Enter student ID: ")
        else:
            stu_id = input("That ID is already taken. Enter student ID: ")
    
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
            current = student
    grade = input(f"Enter grade (0 - 100): ")
    while True:
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                break
        except:
            grade = input(f"That was not valid. Enter grade (0 - 100): ")

    current.add_grade(grade)

    print(f"""
Grade added successfully!
   {current.name} now has {len(current.grades)} grade(s)
   Current average: {current.avg} ({current.letter})
""")
    
    current.update()
    return book

#---------------------- [3] View Student Record ----------------------
def view_student(book):
    method = input("Search by (id/name): ").strip().lower()
    while method != "id" and method != "name":
        method = input("Please enter 'id' or 'name': ").strip().lower()

    query = input(f"Enter {method}: ").strip()
    found = None

    for student in book.list:
        if method == "id" and student.id == query:
            found = student
            break
        elif method == "name" and query.lower() in student.name.lower():
            found = student
            break

    if not found:
        print(f"No student found with that {method}.")
    else:
        print(f"""
=====================================
 STUDENT RECORD
=====================================
 Name: {found.name}
 ID: {found.id}
 Average: {found.avg} ({found.letter})
 Grades: {found.grades}
=====================================
""")

    input("Press Enter to continue...")

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
def summary(book):
    if not book.list:
        print("No students in the gradebook.")
        input("Press Enter to continue...")
        return

    all_grades = []
    for student in book.list:
        all_grades.extend(student.grades)

    avgs = [student.avg for student in book.list if student.avg is not None]
    class_avg = round(sum(avgs) / len(avgs), 1) if avgs else 0

    if class_avg >= 90: class_letter = "A"
    elif class_avg >= 80: class_letter = "B"
    elif class_avg >= 70: class_letter = "C"
    elif class_avg >= 60: class_letter = "D"
    else: class_letter = "F"

    print(f"""
===============================
       CLASS STATISTICS
===============================
 Total Students: {len(book.list)}
 Class Average: {class_avg} ({class_letter})
 Highest Average: {max(avgs) if avgs else 'N/A'}
 Lowest Average: {min(avgs) if avgs else 'N/A'}
 Highest Assignment: {max(all_grades) if all_grades else 'N/A'}
 Lowest Assignment: {min(all_grades) if all_grades else 'N/A'}
===============================
""")

    input("Press Enter to continue...")

#---------------------- [6] Search Students ----------------------
def search(book):
    method = input("How would you like to search? (id/name) ")
    while method != "id" and method != "name":
        method = input("Make sure your answer is either id or name. How would you like to search? (id/name) ")
    search = input("What would you like to search? ")
    book.find_student(search, method)
    input("Press Enter to continue...")