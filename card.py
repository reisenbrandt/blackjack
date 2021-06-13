class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def print_status(self):
        print(self.value + ' of ' + self.suit)