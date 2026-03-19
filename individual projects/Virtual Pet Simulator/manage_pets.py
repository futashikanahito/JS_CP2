# [5] Pet Management
from pet import Pet

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
            pets.append(Pet())
        elif choice == 2:
            for i, pet in enumerate(pets):
                print(f"[{i}] {pet}")
            
        elif choice == 3:
            pass
        elif choice == 4:
            pass