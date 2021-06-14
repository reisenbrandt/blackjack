import time
from hand import Hand
from deck import Deck
from card import Card

# sleep delay intervals
delay = 1
delay2 = 2

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
            print('The dealer busts. You win!')
        elif score_hand(player_hand) > score_hand(dealer_hand):
            print('Congratulations! You win!')
        elif score_hand(player_hand) < score_hand(dealer_hand):
            print('Unlucky... you lose. Better luck next time.')
        elif score_hand(player_hand) == score_hand(dealer_hand):
            print('It\'s a tie!')
    return ""

print("""
Welcome to The Casino.
Where the bets don't matter, and the money isn't real.
*Gambling not encouraged*
""")

play = input('Would you like to play? ').lower()
while play[0] == 'y':
    new_deck = Deck()
    new_deck.create_deck()
    new_deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    print('\nYour first card is a ')
    player_hand.add_card(new_deck.draw_one())
    time.sleep(delay)
    player_hand.print_status()

    time.sleep(delay2)
    print('\nThe dealer\'s first card is a ')
    dealer_hand.add_card(new_deck.draw_one())
    time.sleep(delay)
    dealer_hand.print_status()

    time.sleep(delay2)
    print('\nYour second card is a ')
    player_hand.add_card(new_deck.draw_one())
    time.sleep(delay)
    player_hand.print_status()

    time.sleep(delay2)
    print('\nThe dealer is dealt a card face down.')
    dealer_hand.add_card(new_deck.draw_one())

    time.sleep(delay)
    print(f'\nYour total score is: {score_hand(player_hand)}')
    time.sleep(delay)
    player_bust = False
# player turn hit or stand phase
    if score_hand(player_hand) < 21:
        hit_stand = input('Do you want to hit or stand? ')
        while hit_stand[0] != 's':
            new_card = new_deck.draw_one()
            player_hand.add_card(new_card)
            time.sleep(delay)
            print('\nYour new card is a ')
            new_card.print_status()

            time.sleep(delay)
            print(f'For a total of: {score_hand(player_hand)}')
            if score_hand(player_hand) > 21:
                time.sleep(delay)
                print('You bust. Better luck next time.')
                hit_stand = 's'
                player_bust = True
            elif score_hand(player_hand) == 21:
                print('Blackjack!')
                hit_stand = 's'
            else:
                time.sleep(delay)
                hit_stand = input('Do you want to hit or stand? ')

# dealer turn hit or stand phase
    if player_bust == False:
        time.sleep(delay)
        print('\nThe dealer flips over his face down card. Showing a ')
        time.sleep(delay)
        dealer_hand.print_status()
        print(f'\nFor a total of: {score_hand(dealer_hand)}')

        while score_hand(dealer_hand) < 17:
            dealer_card = new_deck.draw_one()
            print('\nThe dealer hits and receives a ')
            dealer_hand.add_card(dealer_card)
            time.sleep(delay)
            dealer_card.print_status()
            print(f'\nFor a total of: {score_hand(dealer_hand)}')

# comparison of scores to determine a winner
    print(results(player_hand, dealer_hand))

    time.sleep(delay2)
    play = input('Would you like to play again? ')




