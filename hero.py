import random

class Hero:
    def __init__(self, name, starting_health_points = 100):
        self.name = name
        self.starting_hp = starting_health_points
        self.current_hp = starting_health_points

    def fight(self, opponent):
        '''Current hero will fight opponent hero that is passed in'''
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

        cumulative_hp = (self.current_hp + opponent.current_hp)
        attacker_chance = (self.current_hp / cumulative_hp)
        defender_chance = (opponent.current_hp / cumulative_hp)
        
        if attacker_chance > defender_chance:
            print(f'{self.name} defeats {opponent.name}!')
        elif defender_chance > attacker_chance:
            print(f'{opponent.name} defeats {self.name}!')


# If you run this file from the terminal
if __name__ == '__main__':
    # this block is executed.
    hero_kevin = Hero('Kevin', 333)
    hero_juggernaut = Hero('Juggernaut', 1000)

    hero_kevin.fight(hero_juggernaut)
    