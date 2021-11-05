import random
from hero import Hero
class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        ''' Add hero object to self.heroes. '''
        # TODO: Add the hero object that is passed in to the list of heroes in self.heroes
        self.heroes.append(hero)

    def remove_hero(self, name):
        ''' Remove hero from heroes list, if hero isn't found return 0. '''
        found_hero = False

        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                found_hero = True
        
        if not found_hero:
            return 0

    def view_all_heroes(self):
        ''' Prints out all heroes to the console. '''
        # TODO: Loop over list of heroes and print their names.
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        ''' Print team statistics '''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f'{hero.name} Kill/Deaths: {kd}')

    def revive_heroes(self):
        ''' Reset all heroes health to starting health. '''
        # TODO: for each hero in self.heroes, set the hero's current_health to their starting_health.
        for hero in self.heroes:
            hero.current_hp = hero.starting_hp

    def attack(self, other_team):
        ''' Battle each team against each other. '''
        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # TODO: Complete the following:
            # 1. Randomly select living hero from each team (random.choice)
            # 2. Have the heroes fight each other (use fight method in Hero class)
            # 3. update the list of living_heroes and living_opponents to reflect the result of the fight

            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            hero.fight(opponent)

            if hero.is_alive() == False:
                living_heroes.remove(hero)
            else:
                living_opponents.remove(opponent)

        if len(living_heroes) > 0:
            print(f'{self.name} won the battle!')
        else:
            print(f'{opponent.name} won the battle!')
