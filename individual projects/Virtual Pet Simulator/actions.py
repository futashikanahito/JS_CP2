# [1] Feed Pet, [2] Play with Pet, [3] Put Pet to Sleep

def feed(pet, user_inv):
    if pet.hunger >= 100:
        print(f"\n{pet.name} is already full and sniffs the food uninterestedly.")
        return

    if pet.energy <= 0:
        print(f"\n{pet.name} is too exhausted to even eat. Let them sleep first.")
        return

    print(f"""
--- FEED {pet.name.upper()} ---
[1] Premium Dog Food (+40 Hunger, +5 Health, +10 Happiness, -1 from inventory)
[2] Mediocre Dog Food (+25 Hunger, +0 Health, +5 Happiness, -1 from inventory)
[3] Trash Dog Food (+10 Hunger, -5 Health, -5 Happiness, -1 from inventory)
[4] Cancel
""")

    while True:
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if 1 <= choice <= 4:
                break
        except:
            pass

    if choice == 4:
        return

    food_map = {
        1: (0, 40, 10, 5,  "Premium Dog Food"),
        2: (1, 25, 5, 0,  "Mediocre Dog Food"),
        3: (2, 10, -5, -5,  "Trash Dog Food"),
    }

    inv_index, hunger_gain, happiness_change, health_change, food_name = food_map[choice]

    if user_inv[inv_index] <= 0:
        print(f"\nYou don't have any {food_name}! Visit the shop.")
        return None

    pet.hunger = min(100, pet.hunger + hunger_gain)
    pet.health = max(0, min(100, pet.health + health_change))
    pet.happiness = max(0, min(100, pet.happiness + happiness_change))
    pet.xp += 5

    print(f"\nYou fed {pet.name} some {food_name}.")
    print(f"  Hunger: +{hunger_gain}  |  Health: {'+' if health_change >= 0 else ''}{health_change} | Happiness: {'+' if health_change >= 0 else ''}{happiness_change}")

    return inv_index

def play(pet):
    if pet.energy <= 20:
        print(f"\n{pet.name} is too tired to play. Let them rest first!")
        return

    if pet.happiness >= 100:
        print(f"\n{pet.name} is already as happy as can be!")
        return

    print(f"""
--- PLAY WITH {pet.name.upper()} ---
[1] Go for a Walk (+20 Happiness, -15 Energy, +5 Hunger drain, +10 XP)
[2] Play Fetch (+30 Happiness, -25 Energy, +10 Hunger drain, +15 XP)
[3] Cuddle / Rest (+15 Happiness, -5 Energy,  +0 Hunger drain, +5 XP)
[4] Cancel
""")

    while True:
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if 1 <= choice <= 4:
                break
        except:
            pass

    if choice == 4:
        return

    play_map = {
        1: (20, -15, -5,  10, "You took {name} for a walk. They loved it!"),
        2: (30, -25, -10, 15, "You played fetch with {name}. What a workout!"),
        3: (15, -5,   0,  5,  "You cuddled with {name}. They purred... or whatever {name} does."),
    }

    happiness_gain, energy_cost, hunger_cost, xp_gain, message = play_map[choice]

    pet.happiness = min(100, pet.happiness + happiness_gain)
    pet.energy = max(0, pet.energy + energy_cost)
    pet.hunger = max(0, pet.hunger + hunger_cost)
    pet.xp = max(100, pet.xp + xp_gain)

    print(f"\n{message.format(name=pet.name)}")
    print(f"  Happiness: +{happiness_gain}  |  Energy: {energy_cost}  |  XP: +{xp_gain}")

def sleep(pet):
    if pet.energy >= 100:
        print(f"\n{pet.name} isn't tired at all and refuses to go to sleep.")
        return

    print(f"""
--- PUT {pet.name.upper()} TO SLEEP ---
[1] Quick Nap (30 min) — +20 Energy, -5 Happiness
[2] Normal Rest (8 hrs)  — +60 Energy, +0 Happiness, -10 Hunger
[3] Long Sleep (10 hrs) — +100 Energy, +10 Happiness, -20 Hunger
[4] Cancel
""")

    while True:
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if 1 <= choice <= 4:
                break
        except:
            pass

    if choice == 4:
        return

    sleep_map = {
        1: ( 20,  -5,   0, 5,  "Quick Nap"),
        2: ( 60,   0, -10, 10, "Normal Rest"),
        3: (100,  10, -20, 15, "Long Sleep"),
    }

    energy_gain, happiness_change, hunger_cost, xp_gain, sleep_name = sleep_map[choice]

    pet.energy = min(100, pet.energy + energy_gain)
    pet.happiness = max(0, min(100, pet.happiness + happiness_change))
    pet.hunger = max(0, pet.hunger + hunger_cost)
    pet.xp = max(100, pet.xp + xp_gain)

    print(f"\n{pet.name} had a {sleep_name}. They wake up feeling {'refreshed' if energy_gain >= 60 else 'a little better'}.")
    print(f"  Energy: +{energy_gain}  |  Happiness: {'+' if happiness_change >= 0 else ''}{happiness_change}  |  Hunger: {hunger_cost}")

def shop(pet, user_inv, money):
    while True:
        choice = input(f"""
[1] Buy Premium dog food (5 for $50)
[2] Buy Mediocre dog food (5 for $25)
[3] Buy Trash dog food (5 for $10)
[4] Speed Amulet ({"$10" if "speed_amulet" not in pet.inventory() else "BOUGHT"})
[5] Armor ({"$15" if "armor" not in pet.inventory() else "BOUGHT"})
[6] Additional Training ({"$20" if "training" not in pet.inventory() else "BOUGHT"})
[7] Back to Main Menu

Your Money: ${money}
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
    elif choice == 4 and money >= 10 and "speed_amulet" not in pet.inventory():
        money -= 10
        pet.stash(0)
        print("You bought the Speed Amulet.")
    elif choice == 5 and money >= 15 and "armor" not in pet.inventory():
        money -= 15
        pet.stash(1)
        print("You bought Armor.")
    elif choice == 5 and money >= 20 and "training" not in pet.inventory():
        money -= 20
        pet.stash(2)
        print("You bought additional training.")
    else:
        print("You either have insufficient funds or already have that item.")
    
    return user_inv, money