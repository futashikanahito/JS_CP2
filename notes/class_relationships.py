# JS, 1st, Class Relationship Notes

# Inheritance "is a"
# ex. a "Car" "is a" "Vehical"

# Parent Class
class Vehicle:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def move(self):
        print("Move!")

# Child Class
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Touring 2020")
plane = Plane("Boeing", "747")

#car.move()
#boat.move()
#plane.move()

# ------------------------------------------

# Aggregation "has a"
# ex. "Library" "has a" "Book"

class Library:
    def __init__(self, name, catalog = []):
        self.name = name
        self.catalog = catalog

    def add_book(self, book):
        self.catalog.append(book)

    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.pop(book)
        else:
            print("No book with that name found!")
    
    def view_catalog(self):
        for book in self.catalog:
            print(book)
    
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

lib = Library("Provo City Library")

lib.add_book(Book("Way of Kings", "Brandon Sanderson"))
lib.add_book(Book("Fellowship of the Ring", "J.R.R. Tolkien"))
lib.add_book(Book("The Last Battle", "C.S. Lewis"))

#lib.view_catalog()