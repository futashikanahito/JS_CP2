# [11] RACE
import random
import os

def race(pet, money):
    if pet.energy < 20:
        print(f"\n{pet.name} is too tired to race! Let them rest first.")
        input("Press Enter to continue... ")
        return money

    print(f"""
========== RACE MENU ==========
Current Racer: {pet.name} ({pet.species})
  Speed: {pet.attributes[0]}
  Stamina: {pet.attributes[1]}
  Form: {pet.attributes[2]}
  Energy: {pet.energy}%

Race tiers:
  [1] Amateur Race (easy) — Entry: $10 | Prize: $25 
  [2] Pro Race (medium) — Entry: $25 | Prize: $75
  [3] Elite Race (hard) — Entry: $50 | Prize: $150
  [4] Back

Your money: ${money}
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
        return money

    tier_map = {
        1: (10, 25, "Amateur Race", 1, 4),
        2: (25, 75, "Pro Race", 3, 6),
        3: (50, 150, "Elite Race", 5, 8),
    }

    entry_fee, prize, tier_name, npc_min, npc_max = tier_map[choice]

    if money < entry_fee:
        print(f"\nYou can't afford the ${entry_fee} entry fee!")
        input("Press Enter to continue... ")
        return money

    money -= entry_fee
    print(f"\nYou paid the ${entry_fee} entry fee. Good luck!\n")
    input("Press Enter to start the race... ")

    # --- Race ---
    npc_names = random.sample(["Rex", "Bubbles", "Shadow", "Pebbles", "Fang", "Mochi", "Zippy", "Blaze", "Nugget", "Turbo"], 5)

    speed_bonus = 2 if "speed_amulet" in pet.pet_inv else 0
    stamina_bonus = 2 if "armor" in pet.pet_inv else 0
    form_bonus = 2 if "training" in pet.pet_inv else 0

    player_score = ((pet.attributes[0] + speed_bonus) * 3) + ((pet.attributes[1] + stamina_bonus) * 2) + ((pet.attributes[2] + form_bonus) * 1) + random.randint(0, 10)

    racers = [(pet.name + " (YOU)", player_score)]
    for name in npc_names:
        npc_score = ((random.randint(npc_min, npc_max)) * 3) + ((random.randint(npc_min, npc_max)) * 2) + ((random.randint(npc_min, npc_max)) * 1) + random.randint(0, 10)
        racers.append((name, npc_score))

    racers.sort(key=lambda x: x[1], reverse=True)
    player_place = next(place for place, (name, score) in enumerate(racers, 1) if "(YOU)" in name)

    # --- Results ---
    os.system("cls")
    print("""
===========================================================
                    --- RESULTS ---
===========================================================""")
    for place, (name, score) in enumerate(racers, 1):
        print(f"#{place} — {name}")

    print()
    if player_place == 1:
        money += prize
        pet.xp += 30
        pet.happiness = min(100, pet.happiness + 20)
        print(f"{pet.name} won the {tier_name}! You earned ${prize}!")
        print(f"+30 XP | +20 Happiness")
    elif player_place == 2:
        money += prize // 4
        pet.xp += 15
        pet.happiness = min(100, pet.happiness + 10)
        print(f"Good effort! {pet.name} came 2nd. You earned ${prize // 4}.")
        print(f"+15 XP | +10 Happiness")
    else:
        pet.xp += 5
        pet.happiness = max(0, pet.happiness - 10)
        print(f"Better luck next time. {pet.name} came in {player_place}.")
        print(f"+5 XP | -10 Happiness")

    pet.energy = max(0, pet.energy - 30)
    print(f"\n-30 Energy (from racing)")

    input("\nPress Enter to continue... ")
    return money 