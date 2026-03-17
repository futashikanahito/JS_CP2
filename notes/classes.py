# JS, 1st, Classes Notes

# Ex 1
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def __str__(self):
        return f"Name = {self.name}, \nSpecies = {self.species}, \nAge = {self.age}\n"

    def birthday(self):
        self.age += 1

dog = Animal("Doug", "Dog", 4)
bunny = Animal("Judy", "Rabbit", 20)
#print(dog)
#print(bunny)
#dog.birthday()
#print(dog)

# Ex 2
class ClassPeriod:
    def __init__(self, subject = None, teacher = None, room = None):
        self.subject = subject.capitalize()
        self.teacher = teacher
        self.room = room
    
    def __str__(self):
        return f"Subject: {self.subject}, \nTeacher: {self.teacher}, \nRoom: {self.room}"

first = ClassPeriod(subject = "Computer Programming 2", teacher = "Ms. LaRose", room = "200")
print(first)