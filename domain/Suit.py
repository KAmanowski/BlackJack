from domain.Colour import Colour

class Suit:
    name: str
    colour: Colour
    symbol: str

    def __init__(self, name, colour, symbol):
        self.name = name
        self.colour = colour
        self.symbol = symbol


SUITS: list[Suit] = [Suit('heart', Colour.RED, '♥'),
                     Suit('diamond', Colour.RED, '♦'),
                     Suit('club', Colour.BLACK, '♧'),
                     Suit('spade', Colour.BLACK, '♤')]
