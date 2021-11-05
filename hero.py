import random
from armor import Armor
from weapon import Weapon
from ability import Ability
class Hero:
    def __init__(self, name, starting_health_points = 100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_hp = starting_health_points
        self.current_hp = starting_health_points
        self.deaths = 0
        self.kills = 0

    def add_armor(self, armor):
        ''' Add armor to armors list '''
        self.armors.append(armor)

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        ''' Add weapon to abilities list '''
        # TODO: this method will append the weapon object passed in as an argument to self.abilities
        # self.abilities will be a list of abilites and weapons
        self.abilities.append(weapon)
    
    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount '''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths '''
        self.deaths += num_deaths

    def attack(self):
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        # take in incoming_damage
        ''' Calculate the total block amount from all armor blocks. Return total_block: int'''
        total_block = 0

        if self.armors == None or self.current_hp <= 0:
            return total_block
        else:
            for armor in self.armors:
                total_block += armor.block()
            return total_block
            
            # if total_block < 0:
            #     total_block = incoming_damage
            #     return total_block
            # else:
            #     total_block = 0
            #     return total_block


    def take_damage(self, damage):
        ''' Updates self.current_hp to reflect (incoming damage value - defend total_block value) '''
        # TODO: Create a method that updates self.current_hp to (self.current_hp - self.defend(damage))

        if damage - self.defend() < 0:
            return
        else:
            self.current_hp -= damage - self.defend()
    
    def is_alive(self):
        ''' Return True or False depending on whether the hero is alive or not '''
        # TODO: Check the current_hp of hero, if it is <= 0, return False, else return True
        if self.current_hp == 0:
            return False
        else:
            return True


    def fight(self, opponent):
        ''' Current hero will fight opponent hero that is passed in '''
        # TODO: fight each hero until a victor emerges
        # Phases to implement
        # 1. Randomly choose winner (random library choice method)
    
        # rand_num = random.randint(0, 1)

        # if rand_num == 1:
        #     print(f'{self.name} defeats {opponent.name}!')
        # elif rand_num == 0:
        #     print(f'{opponent.name} defeats {self.name}!')

        # ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
        # TODO: current_hp decides winner
        # Phases to implement
        # 1. Choose winner based on percent chance of current_hp

        # cumulative_hp = (self.current_hp + opponent.current_hp)
        # attacker_chance = (self.current_hp / cumulative_hp)
        # defender_chance = (opponent.current_hp / cumulative_hp)
        
        # if attacker_chance > defender_chance:
        #     print(f'{self.name} defeats {opponent.name}!')
        # elif defender_chance > attacker_chance:
        #     print(f'{opponent.name} defeats {self.name}!')

        # ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
        # TODO: current hero will take turns fighting the opponent hero passed in, decide winner based on abilities and hp
        # Phases to implement
        # 1. check if at least one hero has abilities, if no hero has abilities, print "DRAW"
        # 2. else, start fighting loop until a hero has won
        # 3. the hero (self) and their opponent must attack each other and each must take damage from the other's attack
        # 4. after each attack, check if either hero (self) or the opponent is alive. if one has died print "heroname won!" and end the fight loop

        # if len(self.abilities) == 0 and len(opponent.abilities) == 0:
        #     print("DRAW")
        #     return
        # else:
        #     while self.is_alive() and opponent.is_alive():
        #         opponent.take_damage(self.attack())
        #         self.take_damage(opponent.attack())
        #     if self.is_alive:
        #         print(f'{self.name} won!')
        #     else:
        #         print(f'{opponent.name} won!')

        # TODO: Refacter to update the following:
        # 1. the number of kills the hero (self) has when the opponent dies.
        # 2. the number of kills the opponent has when the hero (self) dies.
        # 3. the number of deaths of the opponent if they die in the fight.
        # 4. the number of deaths of the hero (self) if they die in the fight.

        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("DRAW")
            return
        else:
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
            if self.is_alive():
                self.add_kill(1)
                opponent.add_death(1)
                print(f'{self.name} won!')
            else:
                opponent.add_kill(1)
                self.add_death(1)
                print(f'{opponent.name} won!')




# If you run this file from the terminal
if __name__ == '__main__':
    # this block is executed.
    hero_kevin = Hero('Kevin', 333)
    hero_juggernaut = Hero('Juggernaut', 300)

    ability_1 = Ability('Good Debugging', 25)
    ability_2 = Ability('Great Debugging', 50)
    print(len(hero_kevin.abilities))
    hero_kevin.add_ability(ability_1)
    hero_kevin.add_ability(ability_2)
    print(len(hero_kevin.abilities))
    print(hero_kevin.abilities[0].name)

    lasso = Weapon('Lasso of Truth', 90)
    hero_kevin.add_weapon(lasso)
    print(hero_kevin.attack())

    armor_1 = Armor('Good Debugging Shield', 20)
    armor_2 = Armor('Great Debugging Shield', 45)
    hero_kevin.add_armor(armor_1)
    hero_kevin.add_armor(armor_2)


    hero_kevin.fight(hero_juggernaut)