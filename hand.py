from deck import Deck
from card import Card

class Hand:
    def __init__(self):
        self.cards = []
        # self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def print_status(self):
        for card in self.cards:
            card.print_status()

