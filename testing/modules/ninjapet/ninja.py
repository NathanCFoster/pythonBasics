from pet import Pet

class Ninja:
    def __init__(self, firstName, lastName, treats, petFood, petName, petType, petTricks):
        self.firstName = firstName
        self.lastName = lastName
        self.treats = treats
        self.petFood = petFood
        self.pets = {}
        self.pets[petName] = Pet(petName, petType, petTricks)
    def walk(self, petname):
        self.pets[petname].play()
        return self
    def feed(self, petname):
        self.pets[petname].eat()
        return self
    def bathe(self, petname):
        self.pets[petname].noise()
        return self
    def checkStats(self, petname):
        print("Pet: %s\nHealth: %s\nEnergy: %s" %(petname, self.pets[petname].health, self.pets[petname].energy))

nin = Ninja("NIN", "Ja", "treats", "food", "Reeces", "dog", "Stand!")
nin.feed("Reeces").walk("Reeces").bathe("Reeces").checkStats("Reeces")