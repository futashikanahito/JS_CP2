# [5] Pet Management

def managment(current_pet, pets):
    while True:

#-------- CHOICES --------
        while True:
            choice = input("""
[1] Create New Pet
[2] Switch Active Pet
[3] Release Pet (Permanent!)
[4] Back to Main Menu

Enter your choice: """)
            try:
                choice = int(choice)
                if choice > 0 and choice < 5:
                    break
            except:
                pass
        
#-------- CALLS --------
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass