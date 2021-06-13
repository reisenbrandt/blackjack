from hand import Hand
from deck import Deck
from card import Card

def score_hand(hand):
    value = 0

    for card in hand.cards:
        if card.value in ['J', 'Q', 'K']:
            value += 10
        elif card.value == 'A':
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        else:
            value += int(card.value)

    return value

# def player_round(hand):
#     print(score_hand(hand))
#     hit_stand = input('Do you want to hit or stand? ')
#     while hit_stand[0] != 's':
#         hand.add_card(new_deck.draw_one())

play = input('Do you want to play? ').lower()
while play[0] == 'y':
    # print('right')
    new_deck = Deck()
    new_deck.create_deck()
    new_deck.shuffle()
    hand_wip = True

    # def player_round(hand):
    # print(score_hand(hand))
    # hit_stand = input('Do you want to hit or stand? ')
    # while hit_stand[0] != 's':
    #     hand.add_card(new_deck.draw_one())

    while hand_wip == True:
        # print('here')
        player_hand = Hand()
        dealer_hand = Hand()

        print('\nYour first card is a ')
        player_hand.add_card(new_deck.draw_one())
        player_hand.print_status()

        print('\nThe dealers first card is a ')
        dealer_hand.add_card(new_deck.draw_one())
        dealer_hand.print_status()

        print('\nYour second card is a ')
        player_hand.add_card(new_deck.draw_one())
        player_hand.print_status()

        dealer_hand.add_card(new_deck.draw_one())

        print('\nYour total score is ')
        print(score_hand(player_hand))

        hit_stand = input('Do you want to hit or stand? ')
        while hit_stand[0] != 's':
            new_card = new_deck.draw_one()
            player_hand.add_card(new_card)
            new_card.print_status()
            # player_hand.print_status()

            print(score_hand(player_hand))
            if score_hand (player_hand) > 21:
                print('You bust. Better luck next time.')
                break
            else:
                hit_stand = input('Do you want to hit or stand? ')

        print(score_hand(player_hand))
        # else:
        #     hit_stand = input('Do you want to hit or stand? ')
            



        hand_wip = False
    play = 'end'