from hashlib import new
from typing import Coroutine
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

def results(player_hand, dealer_hand):
    if score_hand(dealer_hand) > 17:
        if score_hand(dealer_hand) > 21:
            print('The dealer busts. You win.')
        elif score_hand(player_hand) > score_hand(dealer_hand):
            print('Congratulations! You win!')
        elif score_hand(player_hand) < score_hand(dealer_hand):
            print('Unlucky... you lose. Better luck next time.')
        elif score_hand(player_hand) == score_hand(dealer_hand):
            print('It\'s a tie!')
    return ""

play = input('Do you want to play? ').lower()
while play[0] == 'y':
    # print('right')
    new_deck = Deck()
    new_deck.create_deck()
    new_deck.shuffle()

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

    print(f'\nYour total score is: {score_hand(player_hand)}')

    player_bust = False
# player turn hit or stand phase
    if score_hand(player_hand) < 21:
        hit_stand = input('Do you want to hit or stand? ')
        while hit_stand[0] != 's':
            new_card = new_deck.draw_one()
            player_hand.add_card(new_card)
            new_card.print_status()
            # player_hand.print_status()

            print(score_hand(player_hand))
            if score_hand(player_hand) > 21:
                print('You bust. Better luck next time.')
                hit_stand = 's'
                player_bust = True
            elif score_hand(player_hand) == 21:
                print('Blackjack!')
                hit_stand = 's'
            else:
                hit_stand = input('Do you want to hit or stand? ')

            # print(score_hand(player_hand))

# dealer turn hit or stand phase
    if player_bust == False:
        print('\nThe dealer flips over his face down card. Showing a ')
        dealer_hand.print_status()

        print('\nFor a total of: ')
        print(score_hand(dealer_hand))

        while score_hand(dealer_hand) < 17:
            dealer_card = new_deck.draw_one()
            print('The dealer hits and receives a ')
            dealer_hand.add_card(dealer_card)
            dealer_card.print_status()
            print('\nFor a total of ')
            print(score_hand(dealer_hand))

# comparison of scores to determine a winner
    print(results(player_hand, dealer_hand))

    play = input('Would you like to play again? ')




        # while score_hand(dealer_hand) > 17:
        #     if score_hand(player_hand) > score_hand(dealer_hand):
        #         print('Congratulations! You win!')
        #     elif score_hand(player_hand) < score_hand(dealer_hand):
        #         print('Unlucky... you lose. Better luck next time.')
        #     elif score_hand(player_hand) == score_hand(dealer_hand):
        #         print('It\'s a tie!')

        # if hand_compare == 'done':
        #     if score_hand(player_hand) > score_hand(dealer_hand):
        #         print('Congratulations! You win!')
        #     elif score_hand(player_hand) < score_hand(dealer_hand):
        #         print('Unlucky... the dealer wins!')
        #     elif score_hand(player_hand) == score_hand(dealer_hand):
        #         print('It\'s a tie!')

            


        # else:
        #     hit_stand = input('Do you want to hit or stand? ')
            


