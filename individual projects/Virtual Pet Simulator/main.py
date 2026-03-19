# JS, 1st, Virtual Pet Simulator 

import os
import random
import actions
import load_save
import manage_pets
from pet import Pet

#---------------------- MAIN MENU ----------------------
def main():
    os.system("cls")

    pets = []
    day = 1
    time = 8
    current_pet = 0

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