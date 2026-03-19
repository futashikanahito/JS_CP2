# JS, 1st, Virtual Pet Simulator 

import os
import random
import actions
import load_save
import manage_pets

#---------------------- CLASSES ----------------------
class Pet:
    def __init__(self):
        self.name = input("Pet Name: ")

        choice = input("[1] Cat\n[2] Dog\n[3] Lizard\n[4] Snake\n[5] Fish\n[6] Rabbit\n[7] Bird\n[8] Turtle\n\nEnter your choice: ")
        species = ("Cat" if choice == 0 else "Dog" if choice == 1 else "Lizard" if choice == 2 else "Snake" if choice == 3 else "Fish" if choice == 4 else "Rabbit" if choice == 5 else "Bird" if choice == 6 else "Turtle")
        self.species = species

        age = input("Age (in yrs): ")
        while True:
            try:
                age = float(age)
                break
            except:
                age = input("That was not a valid age! \nAge (in yrs): ")
        self.age = age

        self.level = 1
        self.health = 100
        self.hunger = 100
        self.happiness = 100
        self.energy = 100
        self.skills = []

        print("\nPet created successfully!")
    
    def __str__(self):
        return f"{self.name} ({self.species}, {self.age}yrs)"
    
    def details(self):
        return f"{self.name} ({self.species}, {self.age}yrs)"

#---------------------- MAIN MENU ----------------------
def main():
    os.system("cls")

    pets = []
    day = 1
    time = 8

    print("""
===========================================================
              --- VIRTUAL PET SIMULATOR ---
===========================================================

Welcome! Let's create your first pet!
""")
    pets.append(Pet())

#-------- MAIN LOOP --------
    while True:
        print(f"""
===========================================================
                   --- MAIN MENU ---
===========================================================        
Current Pet: {pets[0].details()} | Time: Day {day}, {f"{time}" + " AM" if time < 12 else f"{time / 2}" + " PM"}
""")

#-------- CHOICES --------
        while True:
            choice = input("""ACTIONS:
[1] Feed Pet
[2] Play with Pet  
[3] Put Pet to Sleep
[4] Check Status
[5] Pet Management
[6] Save Game
[7] Load Game
[8] Quit

Enter your choice (1-8): """)
            try:
                choice = int(choice)
                if choice > 0 and choice < 9:
                    break
            except:
                pass

#-------- CALLS --------
        if choice == 1:
            actions.feed()
        elif choice == 2:
            actions.play()
        elif choice == 3:
            actions.sleep()
        elif choice == 4:
            print()
        elif choice == 5:
            current_pet, pets = manage_pets.managment(current_pet, pets)
        elif choice == 6:
            load_save.save()
        elif choice == 7:
            load_save.load()
        elif choice == 8:
            exit()
        
main()