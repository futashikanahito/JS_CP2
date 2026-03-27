# [1] Add New Student, [2] Add Grade to Student, [3] View Student Record, [4] View All Students, [5] Class Summary
from classes import Student

#---------------------- [1] Add New Student ----------------------
def add_student(students):
    name = input("""
=====================================
          ADD NEW STUDENT 
=====================================
Enter student name: """)
    id = input("Enter student ID: ")
    if id is not int:
        id = input("Make sure id is an integer. Enter student ID: ")
    print(f"""
Student added successfully!
    Name: {name}
    ID: {id}
    Grades: None
""")
    input("Press Enter to continue...")

    students.append(Student(name, id, grades=[]))

#---------------------- [2] Add Grade to Student ----------------------
def add_grade(students):
    print("""
=====================================
            ADD GRADE
=====================================
Current Students: """)
    for student in students:
        print(f"- {student}")
    
    current = None
    check = input("Enter student ID: ")
    for student in students:
        if student.id == check:
            student = current
    grade = input(f"Enter grade (0 - 100): ")

    current.add_grade(grade)

    print(f"""
Grade added successfully!
   {current.name} now has {len(current.grades)} grade(s)
   Current average: # DO THIS ______------------------------
""")

#---------------------- [3] View Student Record ----------------------
def view_student():
    pass

#---------------------- [4] View All Students ----------------------
def view_all():
    pass

#---------------------- [5] Class Summary ----------------------
def summary():
    pass