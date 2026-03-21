# [6] Save Game, [7] Load Game
import csv

def save(pets):
    pass

def load():
    pass

def clear():
    with open("individual projects/Virtual Pet Simulator/save.csv", "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["name", "species", "age", "level", "hunger", "happiness", "energy", "xp"])