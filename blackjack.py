import time
from hand import Hand
from deck import Deck
from card import Card

# sleep delay intervals
delay1 = 1
delay2 = 2


# determines the values of the card and adds to a total
def score_hand(hand):
    value = 0
    # for each card in the hand
    for card in hand.cards:
        # face cards are always 10
        if card.value in ['J', 'Q', 'K']:
            value += 10
        # aces can be 1 or 11 based on the total - automatically determines the best use of ace for the user
        elif card.value == 'A':
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        # otherwise, cards have face value
        else:
            value += int(card.value)

    return value

# determines the winner of the game
def results(player_hand, dealer_hand):
    # as long as the dealer has a hand of 17 or more
    if score_hand(dealer_hand) >= 17:
        # if dealer over 21 - dealer bust
        if score_hand(dealer_hand) > 21:
            print('The dealer busts. You win!')
        # player beats dealer
        elif score_hand(player_hand) > score_hand(dealer_hand):
            print('Congratulations! You win!')
        # dealer beats player
        elif score_hand(player_hand) < score_hand(dealer_hand):
            print('Unlucky... you lose. Better luck next time.')
        # totals are the same - automatic tie
        elif score_hand(player_hand) == score_hand(dealer_hand):
            print('It\'s a tie!')
    return ""


print("""
Welcome to The Casino.
*Gambling not encouraged*
""")
# Where the bets aren't real, and the money doesn't matter.
# ask if user wants to play to start the loop
play = input('Would you like to play? ').lower()

# bet = int(input('How much would you like to bet? '))
# as long as the player wants to play, loop runs
while play[0] == 'y':
    # instantiate a deck, creates cards, and shuffles
    new_deck = Deck()
    new_deck.create_deck()
    new_deck.shuffle()

    # instantiate player and dealer hands
    player_hand = Hand()
    dealer_hand = Hand()

    # reveal player first two cards and dealers first card
    print('\nYour first card is a ')
    player_hand.add_card(new_deck.draw_one())
    time.sleep(delay1)
    player_hand.print_status()

    time.sleep(delay2)
    print('\nThe dealer\'s first card is a ')
    dealer_hand.add_card(new_deck.draw_one())
    time.sleep(delay1)
    dealer_hand.print_status()

    time.sleep(delay2)
    print('\nYour second card is a ')
    player_hand.add_card(new_deck.draw_one())
    time.sleep(delay1)
    player_hand.print_status()

    time.sleep(delay2)
    print('\nThe dealer is dealt a card face down.')
    dealer_hand.add_card(new_deck.draw_one())

    time.sleep(delay1)
    print(f'\nYour total score is: {score_hand(player_hand)}')
    time.sleep(delay1)
    player_bust = False
    # player turn hit or stand phase - if player has not bust
    if score_hand(player_hand) < 21:
        # ask the user what to do, as long as not stand, loop runs
        hit_stand = input('Do you want to hit or stand? ')
        while hit_stand[0] != 's':
            # draw a new card and add to player hand
            new_card = new_deck.draw_one()
            player_hand.add_card(new_card)
            time.sleep(delay1)
            print('\nYour new card is a ')
            new_card.print_status()

            time.sleep(delay1)
            print(f'For a total of: {score_hand(player_hand)}')
            # if user next card does busts
            if score_hand(player_hand) > 21:
                time.sleep(delay1)
                print('You bust. Better luck next time.')
                hit_stand = 's'
                player_bust = True
            # if player gets 21, its a natural blackjack but still need to see if dealer gets 21
            elif score_hand(player_hand) == 21:
                print('Blackjack!')
                hit_stand = 's'
            # ask the user what they want to do again to continue loop if not over 21
            else:
                time.sleep(delay1)
                hit_stand = input('Do you want to hit or stand? ')

    # dealer turn hit or stand phase
    # if player did not bust on their hit/stand phase
    # dealer flips over face down card and then determines whether to hit or stand
    if player_bust == False:
        time.sleep(delay1)
        print('\nThe dealer flips over his face down card. Showing a ')
        time.sleep(delay1)
        dealer_hand.print_status()
        time.sleep(delay2)
        print(f'\nFor a total of: {score_hand(dealer_hand)}')

        # dealers have to hit on anything less than 17 and stand on anything higher than 17
        while score_hand(dealer_hand) <= 17:
            dealer_card = new_deck.draw_one()
            print('\nThe dealer hits and receives a ')
            dealer_hand.add_card(dealer_card)
            time.sleep(delay1)
            dealer_card.print_status()
            print(f'\nFor a total of: {score_hand(dealer_hand)}')
            time.sleep(delay1)

        # comparison of scores to determine a winner
        print(results(player_hand, dealer_hand))

    time.sleep(delay2)
    play = input('Would you like to play again? ')




