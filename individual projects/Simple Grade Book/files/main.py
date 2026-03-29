# JS, 1st, Virtual Pet Simulator 

import os
import actions
import load_save
from classes import Student, GradeBook

#---------------------- MAIN MENU ----------------------
def main():
#-------- INITIALIZE --------
    os.system("cls")

    book = GradeBook()

    print("""
===========================================================
                --- SIMPLE GRADE BOOK ---
===========================================================

Welcome to the Class Grade Book!
""")
    
    actions.add_student(book)
    
#-------- MAIN LOOP & CHOICES --------
    while True:
        while True:
            os.system("cls")
            choice = input("""
===========================================================
                   --- MAIN MENU ---
===========================================================

ACTIONS:
[1] Add New Student
[2] Add Grade to Student
[3] View Student Record (NOT FINISHED)
[4] View All Student
[5] Class Summary (NOT FINISHED)
[6] Search Students
---
[7] Save (Permanent!)
[8] Load (Permanent!)
[9] Clear (Permanent!)
---
[10] Exit

Enter your choice (1-10): """)
            try:
                choice = int(choice)
                if 1 <= choice <= 10:
                    break
            except:
                os.system("cls")

#-------- CALLS --------
        if choice == 1:
            actions.add_student(book)
        elif choice == 2:
            actions.add_grade(book)
        elif choice == 3:
            actions.view_student() # NOT DONE
        elif choice == 4:
            actions.view_all(book)
        elif choice == 5:
            actions.summary() # NOT DONE
        elif choice == 6:
            actions.search(book)
        elif choice == 7:
            confirm = input("This will overwrite your previous information. Are you sure? (y/n) ")
            if confirm == "y":
                load_save.save(book)
                for student in book.list:
                    student.update()
        elif choice == 8:
            confirm = input("This will overwrite your previous information. Are you sure? (y/n) ")
            if confirm == "y":
                book = load_save.load()
                if not book:
                    main()
        elif choice == 9:
            confirm = input("Are you absolutely sure? (y/n) ")
            if confirm == "y":
                book = load_save.clear(book)
                main()
        elif choice == 10:
            os.system("cls")
            exit()

main()