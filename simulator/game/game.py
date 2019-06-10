from typing import Type
from simulator.game.houserules import HouseRules
import random

class Game:

    house_rules: HouseRules = None
    shoe = []
    need_to_shuffle = False

    def __init__(self, house_rules: HouseRules):
        self.house_rules = house_rules
        self.reset()

    def reset(self):
        self.reset_shoe()
        self.print_shoe()
        return

    def reset_shoe(self):
        # Special way we represent cards.
        # See: https://stackoverflow.com/questions/56471384/how-to-do-high-performance-comparisons-within-a-fixed-set-of-options-in-python-3/
        self.shoe = list(range(8, 60)) * self.house_rules.decks_per_shoe
        if self.house_rules.shuffle_mode == 1:
            # Fisher-Yates
            random.shuffle(self.shoe)
        self.shoe.insert(int(len(self.shoe) * 0.75), 0)
        return

    def print_shoe(self):
        rank_names = ['Cut Card', '?', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                      'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        suit_names = ['Club', 'Diamond', 'Heart', 'Spade']
        for card in self.shoe:
            print(rank_names[card >> 2] + ' of ' + suit_names[card & 3] + 's')


    def play(self):
        return