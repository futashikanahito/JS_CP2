# JS, 1st, Virtual Pet Simulator 

import os
import actions
import load_save
from classes import Student

#---------------------- MAIN MENU ----------------------
def main():
#-------- Initialization --------
    os.system("cls")

    students = []
    stu_index = 0

    print("""
===========================================================
                --- SIMPLE GRADE BOOK ---
===========================================================

Welcome to the Class Grade Book!
""")
    
#-------- MAIN LOOP --------
    while True:
        current = students[stu_index]
        os.system("cls")
        print(f"""
===========================================================
                   --- MAIN MENU ---
===========================================================        
--- | --- | --- | ---
""")

#-------- CHOICES --------
        while True:
            choice = input("""\nACTIONS:
[1] Add New Student
[2] Add Grade to Student
[3] View Student Record
[4] View All Students
[5] Class Summary
---
[6] Save (Permanent!)
[7] Load (Permanent!)
[8] Clear (Permanent!)
---
[9] Exit

Enter your choice (1-6): """)
            try:
                choice = int(choice)
                if 1 <= choice <= 9:
                    break
            except:
                os.system("cls")

#-------- CALLS --------
        if choice == 1:
            actions.add_student()
        elif choice == 2:
            actions.add_grade()
        elif choice == 3:
            actions.view_student()
        elif choice == 4:
            actions.view_all()
        elif choice == 5:
            actions.summary()
        elif choice == 6:
            load_save.save()
        elif choice == 7:
            load_save.load()
        elif choice == 8:
            load_save.clear()
        elif choice == 9:
            exit()

main()