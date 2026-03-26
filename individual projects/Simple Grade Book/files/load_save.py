# [6] Save Game, [7] Load Game
import csv
from classes import Student

def save(students):
    students_save = []

    for student in students:
        students_save.append(student.save())
    with open("individual projects/Simple Grade Book/catalog.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["name", "species", "age", "level", "health", "hunger", "happiness", "energy", "xp", "pet_inv", "attributes"])
        csv_writer.writerows(students_save)
    

def load():
    with open("individual projects/Simple Grade Book/catalog.csv", "r", newline="") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = []
        for line in csv_reader:
            rows.append(line)
        
        pets = []
        for line in rows:
            pets.append(Pet(line[0], line[1], float(line[2]), int(line[3]), int(line[4]), int(line[5]), int(line[6]), int(line[7]), int(line[8]), eval(line[9]), eval(line[10])))
    
    return students

def clear():
    with open("individual projects/Simple Grade Book/catalog.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["id", "name", "grades"])