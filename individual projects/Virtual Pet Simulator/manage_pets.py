# [5] Pet Management
from pet import Pet
import random

def managment(current_pet, pets, money):
    while True:

#-------- CHOICES --------
        while True:
            choice = input("""
[1] Buy New Pet (Costs $50)
[2] Switch Active Pet
[3] Release Active Pet (Permanent!)
[4] Back to Main Menu

Enter your choice: """)
            try:
                choice = int(choice)
                if 1 <= choice <= 5:
                    break
            except:
                pass
        
#-------- CALLS --------
        #-------- BUY --------
        if choice == 1:
            if money < 50:
                print("\nYou do not have the funds to buy a new pet.")
            else:
                print("\nYou spent $50\n")
                money -= 50

                name = input("Pet Name: ")
                print()

                choice = input("[1] Cat\n[2] Dog\n[3] Lizard\n[4] Snake\n[5] Fish\n[6] Rabbit\n[7] Bird\n[8] Turtle\n\nEnter your choice: ")
                while True:
                    try:
                        choice = int(choice)
                        break
                    except:
                        choice = input("That was not a valid choice! Enter your choice: ")
                species = ("Cat" if choice == 1 else "Dog" if choice == 2 else "Lizard" if choice == 3 else "Snake" if choice == 4 else "Fish" if choice == 5 else "Rabbit" if choice == 6 else "Bird" if choice == 7 else "Turtle")

                age = input("\nAge (in yrs): ")
                while True:
                    try:
                        age = float(age)
                        break
                    except:
                        age = input("That was not a valid age! \nAge (in yrs): ")

                level = 1
                health = 100
                hunger = 100
                happiness = 100
                energy = 100
                xp = 0
                pet_inv = [False, False, False]
                attributes = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

                pets.append(Pet(name, species, age, level, health, hunger, happiness, energy, xp, pet_inv, attributes))
        
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
                        if 1 <= choice <= len(pets):
                            break
                    except:
                        choice = input("\nEnter your choice: ")
                pets.remove(pets[choice - 1])
                if current_pet >= len(pets):
                    current_pet = len(pets) - 1
                if len(pets) == 0:
                    print("\nYou have no pets left! Returning to main menu to start over.")
                    return current_pet, pets

        #-------- BACK TO MAIN --------
        elif choice == 4:
            return current_pet, pets