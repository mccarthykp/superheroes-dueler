from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self, team_one = None, team_two = None):
        self.team_one = Team('team_one')
        self.team_two = Team('team_two')

    def create_ability(self):
        ''' Prompt for Ability information, return Ability with values from user input '''
        name = input('What is the Ability name? ')
        max_damage = int(input('What is the Max Damage of the Ability? '))

        return Ability(name, max_damage)

    def create_weapon(self):
        ''' Prompt user for Weapon information, return Weapon with values from user input '''
        name = input('What is the Weapon name? ')
        max_damage = int(input('What is the Max Damage of the Weapon? '))

        return Weapon(name, max_damage)

    def create_armor(self):
        ''' Prompt user for Armor information, return Armor with values from user input '''
        name = input('What is the Armor name? ')
        max_block = int(input('What is the Max Block of the Armor? '))

        return Armor(name, max_block)

    def create_hero(self):
        ''' Prompt user for Hero information, return Hero with values from user input  '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != '4':
            add_item = input('[1] Add Ability\n[2] Add Weapon\n[3] Add Armor\n[4] Done\n\nYour choice: ')
            if add_item == '1':
                hero.add_ability(self.create_ability())
            elif add_item == '2':
                hero.add_weapon(self.create_weapon())
            elif add_item == '3':
                hero.add_armor(self.create_armor())
        return hero

    def build_team_one(self):
        ''' Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        # Add the created hero to team one.

        numOfTeamMembers = int(input('How many members would you like on Team One?\n'))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        ''' Prompt the user to build team_two '''
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        # Add the created hero to team two.

        numOfTeamMembers = int(input('How many members would you like on Team Two?\n'))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
    
    def team_battle(self):
        ''' Battle team_one and team_two together '''
        # TODO: This method should battle the teams together
        # Call the attack method that exists in your team objects for the battle functionality

        self.team_one.attack(self.team_two)

    def show_stats(self):
        # TODO: This method should print out battle statistics including each team's average kill/death ratio.
            # Required Stats:
                # Show surviving heroes.
                # Declare winning team
                # Show both teams average kill/death ratio.

        # TODO: for each team, loop through all of their heroes,
        # and use the is_alive() method to check for alive heroes,
        # printing their names and increasing the count if they're alive.
        #
        # TODO: based off of your count of alive heroes,
        # you can see which team has more alive heroes, and therefore,
        # declare which team is the winning team
        #
        # TODO for each team, calculate the total kills and deaths for each hero,
        # find the average kills and deaths by dividing the totals by the number of heroes.
        # finally, divide the average number of kills by the average number of deaths for each team

        print('\n')
        print(self.team_one.name + ' statistics: ')
        self.team_one.stats()
        print('\n')
        print(self.team_two.name + ' statistics: ')
        self.team_two.stats()
        print('\n')

        team_kills = 0
        team_deaths = 1
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        print(self.team_one.name + ' average K/D was: ' + str(team_kills/team_deaths))    

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print('survived from ' + self.team_one.name + ': ' + hero.name)

        team_two_kills = 0
        team_two_deaths = 1
        for hero in self.team_two.heroes:
            team_two_kills += hero.kills
            team_two_deaths += hero.deaths
        print(self.team_two.name + ' average K/D was: ' + str(team_two_kills/team_two_deaths))

        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print('survived from ' + self.team_two.name + ': ' + hero.name)

# if __name__ == "__main__":
#     arena = Arena()
#     arena.build_team_one()
#     arena.build_team_two()
#     arena.team_battle()
#     arena.show_stats()

# if __name__ == "__main__":
#     game_is_running = True

#     arena = Arena()

#     arena.build_team_one()
#     arena.build_team_two()

#     while game_is_running:
#         arena.team_battle()
#         arena.show_stats()
#         play_again = input("Play Again? Y or N: ")

#         if play_again.lower() == "n":
#             game_is_running = False
#         else:
#             arena.team_one.revive_heroes()
#             arena.team_two.revive_heroes()
