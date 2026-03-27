# [6] Save, [7] Load, [8] Clear
import csv
from classes import Student

def save(students):
    students_save = []

    for student in students:
        students_save.append(student.save())
    with open("individual projects/Simple Grade Book/catalog.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["id", "name", "grades"])
        csv_writer.writerows(students_save)
    

def load():
    with open("individual projects/Simple Grade Book/catalog.csv", "r", newline="") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = []
        for line in csv_reader:
            rows.append(line)
        
        students = []
        for line in rows:
            students.append(Student(int(line[0]), str(line[1]), list(line[2])))
    
    return students

def clear():
    with open("individual projects/Simple Grade Book/catalog.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["id", "name", "grades"])