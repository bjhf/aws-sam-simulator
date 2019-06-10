import json
from simulator.utility import logger
from simulator.game.houserules import HouseRules
from simulator.game.game import Game

LOG = logger.get_logger(__name__)
house_rules = HouseRules()


def start_sim(event, context):
    house_rules.load(event['house_rules'])
    for i in range(0, event['iterations']):
        LOG.debug(f"Execution {i}")
        game = Game(house_rules)
        game.play()






if __name__== '__main__':
    start_sim(
        event={
            'simulation_id': '2cbce278-fc91-4a32-860c-edc17a4879a9',
            'iterations': 10,
            # This stuff can probably eventually come from DynamoDB in the form of pre-sets
            'house_rules': {
                'decks_per_shoe': 7,
                'shuffle_mode': 'fisher-yates',
                'dealer_hit_mode': 'on-sixteen',
                'split_aces_limit': 1,
                'minimum_bet': 50,
                'maximum_bet': 500,
                'blackjack_pays': 1.5
            }
        },
        context={}
    )

