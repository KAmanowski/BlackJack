from domain.Suit import Suit
from domain.Colour import Colour
from colorama import Fore

class Card:
    symbol: str
    suit: Suit
    upper_value: int
    lower_value: int
    hidden: bool

    def __init__(self, symbol: str, suit: Suit, upper_value: int, lower_value: int):
        self.symbol = symbol
        self.suit = suit
        self.upper_value = upper_value
        self.lower_value = lower_value
        self.hidden = False

    def draw_card(self):
        card_out = '['
        if self.suit.colour == Colour.RED:
            card_out += Fore.RED + f'{self.suit.symbol} '
        else:
            card_out += f'{self.suit.symbol} '

        if self.hidden:
            card_out += f'{Fore.RESET}?]'
        else:
            card_out += f'{Fore.RESET}{self.symbol}]'
        return card_out
