class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def print_status(self):
        print(f"""_______
|{self.value}{" "if self.value == 10 else "  "}  |
|  {self.suit}  |
|__{"_"if self.value == 10 else "__"}{self.value}|""")
