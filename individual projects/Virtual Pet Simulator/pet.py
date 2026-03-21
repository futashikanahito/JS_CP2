#---------------------- CLASSES ----------------------
class Pet:
    def __init__(self):
        self.name = input("Pet Name: ")
        print()

        choice = input("[1] Cat\n[2] Dog\n[3] Lizard\n[4] Snake\n[5] Fish\n[6] Rabbit\n[7] Bird\n[8] Turtle\n\nEnter your choice: ")
        while True:
            try:
                choice = int(choice)
                break
            except:
                choice = input("That was not a valid choice! Enter your choice: ")
        species = ("Cat" if choice == 1 else "Dog" if choice == 2 else "Lizard" if choice == 3 else "Snake" if choice == 4 else "Fish" if choice == 5 else "Rabbit" if choice == 6 else "Bird" if choice == 7 else "Turtle")
        self.species = species

        age = input("\nAge (in yrs): ")
        while True:
            try:
                age = float(age)
                break
            except:
                age = input("That was not a valid age! \nAge (in yrs): ")
        self.age = age

        self.level = 1
        self.health = 100
        self.hunger = 100
        self.happiness = 100
        self.energy = 100
        self.xp = 0

        print("\nPet created successfully!")
    
    def __str__(self):
        return f"{self.name} ({self.species}, {self.age}yrs)"
    
    def status(self):
        return f"{self.name} ({self.species}, {self.age}yrs)"
    
    def save(self):
        return [self.name, self.species, self.age, self.level, self.hunger, self.happiness, self.energy, self.xp]