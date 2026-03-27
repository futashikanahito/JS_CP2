#---------------------- CLASSES ----------------------
class Student:
    def __init__(self, name, id, grades):
        self.name = name
        self.id = id
        self.grades = grades

    def __str__(self):
        return f"{self.name} (ID: {self.id})"

    def save(self):
        return [self.id, self.name, self.grades]
    
    def add_grade(self, grade):
        self.grades.append(grade)