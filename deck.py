import random
from card import Card


class Deck:


    def __init__(self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = ['\u2660', '\u2665', '\u2663', '\u2666']
        self.deck = []

    def create_deck(self):
        for rank in self.ranks:
            for suit in self.suits:
                new_card = Card(suit, rank)
                self.deck.append(new_card)

    def print_status(self):
        for c in self.deck:
            print(c.value + ' of ' + c.suit)

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_one(self):
        return self.deck.pop(0)

