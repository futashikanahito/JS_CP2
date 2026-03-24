# JS, 1st, Virtual Pet Simulator 

import os
import random
import actions
import load_save
import manage_pets
import pet_races
import helpers
from pet import Pet

#---------------------- MAIN MENU ----------------------
def main():
    os.system("cls")

    pets = []
    day = 1
    time = 8
    current_pet = 0
    money = 100
    user_inv = [0, 0, 2]

    print("""
===========================================================
              --- VIRTUAL PET SIMULATOR ---
===========================================================

Welcome! Let's create your first pet!
""")
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
    pet_inv = [None, None, None]
    attributes = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    # Speed, Stamina, Form

    pets.append(Pet(name, species, age, level, health, hunger, happiness, energy, xp, pet_inv, attributes))

#-------- MAIN LOOP --------
    while True:
        os.system("cls")
        pet = pets[current_pet]
        print(f"""
===========================================================
                   --- MAIN MENU ---
===========================================================        
Current Pet: {pet} | Time: Day {day}, {f"{time}" + " AM" if time < 12 else f"{time // 2}" + " PM"} | Money: ${money} | Your Inventory: {user_inv[0]} Premium dog food, {user_inv[1]} Mediocre dog food, {user_inv[2]} Trash dog food
""")
        #-------- RANDOM EVENT --------
        money, user_inv = helpers.random_event(pets, current_pet, money, user_inv)
        input("\nPress Enter to continue... ")

#-------- CHOICES --------
        while True:
            choice = input("""\nACTIONS:
[1] Feed Pet
[2] Play with Pet  
[3] Put Pet to Sleep
[4] Check Status
[5] Pet Management
[6] Shop
[7] Save Game (Permanent!)
[8] Load Game (Permanent!)
[9] Clear Save Data & Restart (Permanent!)
[10] Quit
[11] RACE

Enter your choice (1-11): """)
            try:
                choice = int(choice)
                if 1 <= choice <= 11:
                    break
            except:
                os.system("cls")

#-------- CALLS --------
        if choice == 1:
            inv_index = actions.feed(pet, user_inv)
            if inv_index is not None:
                user_inv[inv_index] -= 1
        elif choice == 2:
            actions.play(pet)
        elif choice == 3:
            actions.sleep(pet)
        elif choice == 4:
            print(pet.status())
            input("Press Enter to continue... ")
        elif choice == 5:
            current_pet, pets = manage_pets.managment(current_pet, pets, money)
            if len(pets) == 0:
                main()
        elif choice == 6:
            user_inv, money = actions.shop(pet, user_inv, money)
        elif choice == 7:
            confirm = input("This will overwrite your previous information. Are you sure? (y/n) ")
            if confirm == "y":
                load_save.save(pets, day, time, money, user_inv)
        elif choice == 8:
            confirm = input("This will overwrite your previous information. Are you sure? (y/n) ")
            if confirm == "y":
                pets, day, time, money, user_inv = load_save.load()
                if pets == []:
                    main()
        elif choice == 9:
            confirm = input("Are you absolutely sure? (y/n) ")
            if confirm == "y":
                load_save.clear()
                main()
        elif choice == 10:
            os.system("cls")
            exit()
        elif choice == 11:
            pet_races.race(pets, current_pet, money)
        
        #-------- STAT CHANGES / DAY END --------
        if time == 20:
            print("\nYou head to bed for the night.")
            input("Press Enter to continue... ")
            time = 4
        time += 4 

        if money == 0:
            print("\nYou went broke and ended up on the streets, having to sell all your pets to stay alive.\nGAME OVER")
            exit()
        
        exp = pet.exp()
        if exp > 100:
            pet.level_up()
            pet.xp = 0
            print("You leveled up.")
            input("Press Enter to continue... ")

main()