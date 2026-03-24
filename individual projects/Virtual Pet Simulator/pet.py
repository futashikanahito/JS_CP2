#---------------------- CLASSES ----------------------
class Pet:
    def __init__(self, name, species, age, level, health, hunger, happiness, energy, xp, pet_inv, attributes):
        self.name = name
        self.species = species
        self.age = age
        self.level = level
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.xp = xp
        self.pet_inv = pet_inv
        self.attributes = attributes

        print("\nPet created successfully!")
        input("Press Enter to continue... ")
    
    def __str__(self):
        return f"{self.name} ({self.species}, {self.age}yrs)"
    
    def status(self):
        return f"""┌─────── ─ ─ ─
│ Name: {self.name}
│ Species: {self.species}
│ Age: {self.age} years
│ Level: {self.level}
│ Health: {self.health}%
│ Hunger: {self.hunger}%
│ Happiness: {self.happiness}%
│ Energy: {self.energy}%
│ EXP: {self.xp} / 100 
│ Pet Inventory: {f"{self.pet_inv[0].title()}" + ", " if self.pet_inv[0] != None else ""} {f"{self.pet_inv[1].title()}" + ", " if self.pet_inv[1] != None else ""} {f"{self.pet_inv[2].title()}" + ", " if self.pet_inv[2] != None else ""} {None if self.pet_inv == None else ""}
│ Attributes: {self.attributes[0]} Speed, {self.attributes[1]} Endurance, {self.attributes[2]} Form
└─────── ─ ─ ─"""
    
    def save(self):
        return [self.name, self.species, self.age, self.level, self.health, self.hunger, self.happiness, self.energy, self.xp, self.pet_inv, self.attributes]

    def inventory(self):
        return self.pet_inv
    
    def exp(self):
        return self.xp
    
    def stash(self, index):
        if index == 0:
            self.pet_inv[index] == "speed_amulet"
        elif index == 1:
            self.pet_inv[index] == "armor"
        elif index == 2:
            self.pet_inv[index] == "training"
    
    def level_up(self):
        if self.attributes[0] < 10:
            self.attributes[0] += 1
        if self.attributes[1] < 10:
            self.attributes[1] += 1
        if self.attributes[2] < 10:
            self.attributes[2] += 1