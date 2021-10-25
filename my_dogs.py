from dog import Dog

my_dog = Dog('Rex', 'SuperDog')
my_other_dog = Dog('Annie', 'SuperDog')

dog_1 = Dog('Rhino', 'DinoDog')
dog_2 = Dog('Garbo', 'TrashDog')
dog_3 = Dog('Neo', 'MatrixDog')

print(my_other_dog.name)
my_dog.bark()

dog_1.bark()
dog_2.sit()
dog_3.rollover()