import random

def random_event(pets, current_pet, money, user_inv):
    events = [
        ("found_money", "You found $10 on the ground!"),
        ("treat_gift",  "A neighbor gifted you a bag of treats! (+1 Trash dog food)"),
        ("happy_walk",  "Your pet had a great walk and feels more energetic! (+10 Energy)"),
        ("tasty_meal",  "Your pet found something yummy and isn't as hungry! (+10 Hunger)"),
        ("good_mood",   "Your pet is in an especially good mood today! (+10 Happiness)"),
        ("health_boost","Fresh air and sunshine gave your pet a health boost! (+10 Health)"),
        ("vet_bill",    "Your pet needed a surprise vet visit. (-$15)"),
        ("stole_food",  "Your pet got into the trash and feels sick! (-10 Health)"),
        ("bad_dream",   "Your pet had nightmares and woke up tired. (-10 Energy)"),
        ("grumpy",      "Your pet woke up on the wrong side of the bed. (-10 Happiness)"),
        ("hungry_fast", "Your pet burned through food faster than usual. (-10 Hunger)"),
        ("nothing",     "Nothing unusual happened."),
        ("nothing",     "A quiet, uneventful stretch."),
        ("nothing",     "Your pet stares at the wall. Pets, right?"),
    ]

    event_id, message = random.choice(events)
    print(f"Random Event: {message}")

    if event_id == "found_money":
        money += 10
    elif event_id == "treat_gift":
        user_inv[2] += 1
    elif event_id == "happy_walk":
        pets[current_pet].energy = min(100, pets[current_pet].energy + 10)
    elif event_id == "tasty_meal":
        pets[current_pet].hunger = min(100, pets[current_pet].hunger + 10)
    elif event_id == "good_mood":
        pets[current_pet].happiness = min(100, pets[current_pet].happiness + 10)
    elif event_id == "health_boost":
        pets[current_pet].health = min(100, pets[current_pet].health + 10)
    elif event_id == "vet_bill":
        money = max(0, money - 15)
    elif event_id == "stole_food":
        pets[current_pet].health = max(0, pets[current_pet].health - 10)
    elif event_id == "bad_dream":
        pets[current_pet].energy = max(0, pets[current_pet].energy - 10)
    elif event_id == "grumpy":
        pets[current_pet].happiness = max(0, pets[current_pet].happiness - 10)
    elif event_id == "hungry_fast":
        pets[current_pet].hunger = max(0, pets[current_pet].hunger - 10)

    return money, user_inv