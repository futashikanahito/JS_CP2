# [1] Feed Pet, [2] Play with Pet, [3] Put Pet to Sleep

def feed(pets, current_pet):
    pets[current_pet].feed()

def play(pets, current_pet):
    pets[current_pet].play()

def sleep(pets, current_pet):
    pets[current_pet].sleep()

def shop(pets, current_pet, user_inv, money):
    while True:
        choice = input(f"""
[1] Buy Premium dog food (5 for $50)
[2] Buy Mediocre dog food (5 for $25)
[3] Buy Trash dog food (5 for $10)
[4] Speed Amulet ({"$10" if "speed_amulet" not in pets[current_pet].inventory() else "BOUGHT"})
[5] Armor ({"$15" if "armor" not in pets[current_pet].inventory() else "BOUGHT"})
[6] Additional Training ({"$20" if "training" not in pets[current_pet].inventory() else "BOUGHT"})
[7] Back to Main Menu

Enter your choice: """)
        try:
            choice = int(choice)
            if 1 <= choice <= 7:
                break
        except:
            pass
    
    if choice == 1 and money >= 50:
        money -= 50
        user_inv[0] += 5
        print("You bought Premium dog food.")
    elif choice == 2 and money >= 25:
        money -= 25
        user_inv[1] += 5
        print("You bought Mediocre dog food.")
    elif choice == 3 and money >= 10:
        money -= 10
        user_inv[2] += 5
        print("You bought Trash dog food.")
    elif choice == 4 and money >= 10 and "speed_amulet" not in pets[current_pet].inventory():
        money -= 10
        pets[current_pet].stash(0)
        print("You bought the Speed Amulet.")
    elif choice == 5 and money >= 15 and "armor" not in pets[current_pet].inventory():
        money -= 15
        pets[current_pet].stash(1)
        print("You bought Armor.")
    elif choice == 5 and money >= 20 and "training" not in pets[current_pet].inventory():
        money -= 20
        pets[current_pet].stash(2)
        print("You bought additional training.")
    else:
        print("You either have insufficient funds or already have that item.")