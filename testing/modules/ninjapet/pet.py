from testing.modules.ninjapet.ninja import Ninja


class Pet(Ninja):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 10
        self.energy = 25

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        if(self.type == "dog"):
            print("Bark")
        elif(self.type == "cat"):
            print("Meow")
        else:
            print("What does the ___ say")
