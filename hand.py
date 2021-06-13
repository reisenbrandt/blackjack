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

    # def deal_card(self, deck):
    #     self.new_card = deck.pop()
    #     if self.new_card[0] == 'A':
    #         if self.value + 11 <= 21:
    #             self.value += 11
    #         else:
    #             self.value += 1

    #     else:
    #         self.value += deck.ranks[self.new_card[0]]
    #     self.hand.append(self.new_card)

    # def show_hand(self):
    #     print('Your hand consists of: ' + str(self.hand))
    #     print('Its value is: ' + str(self.value))

        