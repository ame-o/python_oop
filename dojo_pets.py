class Ninja:
    def __init__(self, pet, first_name="America", last_name="O", treats = "Pupperoni", pet_food="kibble"):
        self.pet = pet
        self.first_name = first_name 
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
    # Methods
    def walk(self):
        print(f"{self.first_name}{self.last_name} took {self.pet} on a walk.")
        self.pet.play()
        return self

    def feed(self):
        print(f"{self.first_name}{self.last_name} is feeding the furbaby ...again.")
        self.pet_food
        self.pet.eat()
        return self

    def bathe(self):
        print(f"It's that monthly bath time for furbaby!")
        self.pet.noise()
        self.pet.sleep()
        return self

america= Ninja("Luci")

class Pet:
    def __init__(self, name, type, tricks = "sit"):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 50
        self.health = 50

    def sleep(self):
        self.energy+=25
        print(f"{self.name} went to sleep and increased her energy by 25.")
        return self

    def eat(self):
        self.energy += 5 
        self.health += 10
        print(f"{self.name} was fed; gained energy by +5 and health by +10.")
        return self

    def play(self):
        self.health+=5
        print(f"{self.name} has the zoomies! 5 points to health! ")
        return self

    def noise(self):
        print("Squeak! I mean Woof! Woof!")


america.walk()
america.feed()
america.bathe()