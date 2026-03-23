# [6] Save Game, [7] Load Game
import csv

def save(pets, day, time, money, user_inv):
    pet_save = []
    user_save = []

    for pet in pets:
        pet_save.append(pet.save())
    with open("individual projects/Virtual Pet Simulator/save_pets.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["name", "species", "age", "level", "hunger", "happiness", "energy", "xp"])
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
            row = []
            for item in line:
                row.append(item)
            rows.append(row)
        
        pets = []
        for line in rows:
            pets.append(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])
    
    with open("individual projects/Virtual Pet Simulator/save_user.csv", "r", newline="") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        row = []
        for line in csv_reader:
            row.append(line)
        
        day = row[0]
        time = row[1]
        money = row[2]
        user_inv = row[3]
    
    return pets, day, time, money, user_inv

def clear():
    with open("individual projects/Virtual Pet Simulator/save_pets.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["name", "species", "age", "level", "hunger", "happiness", "energy", "xp"])

    with open("individual projects/Virtual Pet Simulator/save_user.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows([["day", "time", "money", "user_inv"], [1, 8, 100, [0, 0, 2]]])