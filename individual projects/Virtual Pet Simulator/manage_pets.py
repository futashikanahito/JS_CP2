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
        #-------- CREATE --------
        if choice == 1:
            print()
            pets.append(Pet())
        
        #-------- SWITCH ACTIVE --------
        elif choice == 2:
            for i, pet in enumerate(pets):
                print(f"[{i + 1}] {pet}")
            choice = input("\nEnter your choice: ")
            while True:
                try:
                    choice = int(choice)
                    if choice > 0 and choice < len(pets) + 1:
                        break
                except:
                    choice = input("\nEnter your choice: ")
            current_pet = choice - 1 
        
        #-------- RELEASE --------
        elif choice == 3:
            confirm = input("Are you absolutely sure? (y/n) ")
            if confirm == "y":
                for i, pet in enumerate(pets):
                    print(f"[{i + 1}] {pet}")
                choice = input("\nEnter your choice: ")
                while True:
                    try:
                        choice = int(choice)
                        if choice > 0 and choice < len(enumerate(pets)) + 1:
                            break
                    except:
                        choice = input("\nEnter your choice: ")
                pets.remove(pets[choice])

        #-------- BACK TO MAIN --------
        elif choice == 4:
            return current_pet, pets