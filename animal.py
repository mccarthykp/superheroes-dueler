class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating.')
        return 

    def drink(self):
        print(f'{self.name} is drinking.')
        return 


class Frog(Animal):
    def jump(self):
        print(f'{self.name} is jumping.')
        return 


animal = Animal('corinne')
animal.eat()
animal.drink()

frog = Frog('jeb')
frog.eat()
frog.drink()
frog.jump()