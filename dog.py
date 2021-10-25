class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print(f'{self.name} initialized!')

    def bark(self):
        print(f'{self.name} woofs!')

    def sit(self):
        print(f'{self.name} sits.')

    def rollover(self):
        print(f'{self.name} rolls over!')
