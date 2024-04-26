import random

from domain.Card import Card
from domain.Suit import SUITS

class Deck:
    cards = list[Card]

    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        self.cards = []
        for suit in SUITS:
            for number in range(2, 10):
                self.cards.append(Card(str(number), suit, number, number))

            self.cards.append(Card("J", suit, 10, 10))
            self.cards.append(Card("Q", suit, 10, 10))
            self.cards.append(Card("K", suit, 10, 10))
            self.cards.append(Card("A", suit, 11, 1))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()
