# [7] Save, [8] Load, [9] Clear
import csv, ast
from classes import Student, GradeBook

#---------------------- [7] Save ----------------------
def save(book):
    book_save = []

    for student in book.list:
        book_save.append(student.save())
    with open("individual projects/Simple Grade Book/catalog.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["id", "name", "grades"])
        csv_writer.writerows(book_save)
    
#---------------------- [8] Load ----------------------
def load():
    with open("individual projects/Simple Grade Book/catalog.csv", "r", newline="") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        rows = []
        for line in csv_reader:
            rows.append(line)
        
        book = GradeBook()
        for line in rows:
            grades = ast.literal_eval(line[2]) if line[2] else []
            book.add_student(Student(str(line[1]), str(line[0]), grades))
        
    return book

#---------------------- [9] Clear ----------------------
def clear(book):
    with open("individual projects/Simple Grade Book/catalog.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["id", "name", "grades"])
    
    book.list = []
    return book