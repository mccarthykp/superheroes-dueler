from hero import Hero

class Team():
    def __init__(self, name):
        self.name = name
        self.heroes = list()

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