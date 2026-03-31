#---------------------- CLASSES ----------------------
class GradeBook:
    def __init__(self):
        self.list = []

    def add_student(self, student):
        self.list.append(student)

    def remove_student(self, student):
        if student in self.list:
            self.list.remove(student)
        else:
            print("No student with that name found!")
    
    def find_student(self, search, method):
        results = []
        if method == "id":
            for student in self.list:
                if search in student.id:
                    results.append(student)
        else:
            for student in self.list:
                if search in student.name:
                    results.append(student)
        if not results:
            if method == "id":
                print("No one with that ID found.")
            else:
                print("No one with that name found.")
        else:
            print("┌─────────────────────────────────────┐")
            for result in results:
                print(f"│ {result.id} │ {result.name} │ {result.avg} │ {result.letter}")
            print("└─────────────────────────────────────┘")
            

class Student:
    def __init__(self, name, id, grades):
        self.name = name
        self.id = id
        self.grades = grades
        self.avg = None
        self.letter = None

    def __str__(self):
        return f"{self.name} (ID: {self.id})"
    
    def update(self):
        if len(self.grades) != 0:
            self.avg = float(sum(self.grades) / len(self.grades))
            if self.avg >= 90:
                self.letter = "A"
            elif self.avg >= 80:
                self.letter = "B"
            elif self.avg >= 70:
                self.letter = "C"
            elif self.avg >= 60:
                self.letter = "D"
            else:
                self.letter = "F"
    
    def save(self):
        return [self.id, self.name, self.grades]
    
    def add_grade(self, grade):
        self.grades.append(grade)