from domain.Card import Card
from domain.Dealer import Dealer
from domain.Player import Player

from utility.Utilities import clear_console

import shutil
from colorama import Fore

class Table:
    player: Player
    dealer: Dealer

    def __init__(self, player: Player, dealer: Dealer):
        self.player = player
        self.dealer = dealer

    def draw_cards(self, cards: list[Card]):
        if len(cards) == 0:
            print("")
        else:
            card_out = ''
            for card in cards:
                card_out += card.draw_card()
            print(card_out.center(shutil.get_terminal_size().columns))

    def draw_points(self, player: Player):
        if len(player.cards) != 0:
            if player.get_high_card_value() == player.get_low_card_value() or player.get_high_card_value() > 21:
                print(f"({str(player.get_low_card_value())})".center(shutil.get_terminal_size().columns))
            else:
                print(f"({str(player.get_low_card_value())} / {str(player.get_high_card_value())})"
                      .center(shutil.get_terminal_size().columns))

    def draw_table(self):
        clear_console()

        print("Dealer".center(shutil.get_terminal_size().columns))
        # Display dealer cards
        self.draw_cards(self.dealer.cards)
        print("")
        self.draw_points(self.dealer)
        # Display table
        print("\n\n\n")
        if self.player.current_bet != 0:
            print(f"Current bet: [{Fore.YELLOW}{self.player.current_bet}{Fore.RESET}]".center(shutil.get_terminal_size().columns))
        print("\n")
        # Display player cards
        self.draw_points(self.player)
        print("")
        self.draw_cards(self.player.cards)

        print(self.player.name.center(shutil.get_terminal_size().columns))
        print(f"[{self.player.money}]".center(shutil.get_terminal_size().columns))
