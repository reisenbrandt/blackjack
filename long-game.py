# # from collections import namedtuple

# # Card = namedtuple('Card',['suit', 'rank'])

# class Deck:
#     card_ranks = []
#     card_suits = []

#     def __init__(self):
#         self.cards = []



# class Frenchsuited(Deck):

# print(Frenchsuited.card_suits)

from random import randint

card_ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

def card_deck():
    deck = []
    for i in card_suits:
        for j in card_ranks:
            deck.append(j + ' of ' + i)
    return deck


# print(card_deck())

def card_value(card):
    if card[:1] in ('J', 'Q', 'K', '1'):
        return int(10)
    elif card[:1] in ('2', '3', '4', '5', '6', '7', '8', '9'):
        return card[:1]
    elif card[:1] == 'A':
        print(str(card))
        ace = input('Do you want this ace to be a 1 or an 11?\n')
        if ace == '1':
            return int(1)
        elif ace == '11':
            return int(11)
        else:
            ace = input('Do you want this ace to be a 1 or an 11?\n')

# print(card_value('A'))

def draw_card(deck):
    return deck[randint (0, len(card_deck) -1)]

def remove_card(deck, card):
    return deck.remove(card)

# gameplay


