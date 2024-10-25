import random

class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A"] + [i for i in range(2, 11)] + ["J", "Q", "K"]

        self.cards = [Card(suit, value) for suit in suits for value in values]
    
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if self.cards:
            card = self.cards.pop()
            print(card)
        else:
            print("No more cards in the deck")
