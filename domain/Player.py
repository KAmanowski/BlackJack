from domain.Card import Card
from utility.Utilities import ask_for_positive_int, ask_for_bool


class Player:
    name: str
    cards: list[Card]
    money: int
    current_bet: int

    def __init__(self, name: str, money: int):
        self.name = name
        self.cards = []
        self.money = money
        self.current_bet = 0

    def get_high_card_value(self) -> int:
        total: int = 0
        for card in self.cards:
            if not card.hidden:
                if (total + card.upper_value) > 21:
                    total += card.lower_value
                else:
                    total += card.upper_value

        return total

    def get_low_card_value(self) -> int:
        total: int = 0

        for card in self.cards:
            if not card.hidden:
                total += card.lower_value

        return total

    def get_true_value(self):
        if self.get_high_card_value() <= 21:
            return self.get_high_card_value()
        else:
            return self.get_low_card_value()

    def ask_for_bet(self):
        self.current_bet = ask_for_positive_int("Place your bet: ", self.money)
        self.money -= self.current_bet

    def ask_for_hit(self) -> bool:
        return ask_for_bool("Hit? (Y/N) ")

    def has_blackjack(self):
        if self.get_true_value() == 21:
            return True
        else:
            return False

    def has_bust(self):
        if self.get_true_value() > 21:
            return True
        else:
            return False
