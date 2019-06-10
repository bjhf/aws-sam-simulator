
class HouseRules:

    decks_per_shoe = None
    shuffle_mode = None
    shuffle_mode_map = {
        'NO-SHUFFLE': 0,
        'FISHER-YATES': 1,
        0: 'NO-SHUFFLE',
        1: 'FISHER-YATES'
    }
    dealer_hit_mode = None
    dealer_hit_mode_map = {
        'ON-SIXTEEN': 0,
        'ON-SOFT-SEVENTEEN': 1,
        0: 'ON-SIXTEEN',
        1: 'ON-SOFT-SEVENTEEN'
    }
    split_aces_limit = None
    minimum_bet = None
    maximum_bet = None
    blackjack_pays = None

    def load(self, house_rules):
        self.decks_per_shoe = house_rules['decks_per_shoe']
        self.shuffle_mode = self.shuffle_mode_map.get(house_rules['shuffle_mode'].upper())
        self.dealer_hit_mode = self.dealer_hit_mode_map.get(house_rules['dealer_hit_mode'].upper())
        self.split_aces_limit = house_rules['split_aces_limit']
        self.minimum_bet = house_rules['minimum_bet']
        self.maximum_bet = house_rules['maximum_bet']
        self.blackjack_pays = house_rules['blackjack_pays']
