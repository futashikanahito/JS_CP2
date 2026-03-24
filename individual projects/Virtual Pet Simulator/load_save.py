# [6] Save Game, [7] Load Game
import csv
from pet import Pet

def save(pets, day, time, money, user_inv):
    pet_save = []
    user_save = []

    for pet in pets:
        pet_save.append(pet.save())
    with open("individual projects/Virtual Pet Simulator/save_pets.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["name", "species", "age", "level", "health", "hunger", "happiness", "energy", "xp", "pet_inv", "attributes"])
        csv_writer.writerows(pet_save)
    user_save.append(day); user_save.append(time); user_save.append(money); user_save.append(user_inv)

    with open("individual projects/Virtual Pet Simulator/save_user.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["day", "time", "money", "user_inv"])
        csv_writer.writerow(user_save)

def load():
    with open("individual projects/Virtual Pet Simulator/save_pets.csv", "r", newline="") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = []
        for line in csv_reader:
            rows.append(line)
        
        pets = []
        for line in rows:
            pets.append(Pet(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], list[line[9]], list[line[10]]))
    
    with open("individual projects/Virtual Pet Simulator/save_user.csv", "r", newline="") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        row = next(csv_reader)
        
    day = int(row[0])
    time = int(row[1])
    money = int(row[2])
    user_inv = eval[row[3]]
    
    return pets, day, time, money, user_inv

def clear():
    with open("individual projects/Virtual Pet Simulator/save_pets.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["name", "species", "age", "level", "health", "hunger", "happiness", "energy", "xp", "pet_inv", "attributes"])

    with open("individual projects/Virtual Pet Simulator/save_user.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows([["day", "time", "money", "user_inv"], [1, 8, 100, [0, 0, 2]]])