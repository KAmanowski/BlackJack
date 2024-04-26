import time

from domain.Dealer import Dealer
from domain.Deck import Deck
from domain.Player import Player
from domain.Table import Table
from utility.Utilities import ask_for_int, ask_for_positive_int, ask_for_bool, clear_console, pause_for_dramatic_effect
from colorama import Fore

clear_console()

DEALER: Dealer = Dealer()
PLAYER: Player = Player(input(Fore.RESET + "Enter name: "), ask_for_positive_int("Enter starting money: "))
TABLE: Table = Table(PLAYER, DEALER)
DECK: Deck = Deck()

WINNER: Player = None

first_time_loop = True

# Game loop
while True:
    TABLE.draw_table()
    if PLAYER.money < 1:
        break

    if not first_time_loop:
        if not ask_for_bool("Would you like to continue? (Y/N) "):
            break

    # Betting Phase
    PLAYER.ask_for_bet()

    # Initial Draw Phase
    for x in range(2):
        dealer_drawn_card = DECK.draw()
        if x == 1:
            # Hide second card
            dealer_drawn_card.hidden = True

        DEALER.cards.append(dealer_drawn_card)
        TABLE.draw_table()
        time.sleep(1)

        PLAYER.cards.append(DECK.draw())
        TABLE.draw_table()
        time.sleep(1)

    # Player Hit Phase
    while True:
        TABLE.draw_table()
        if PLAYER.has_blackjack():
            print("You got BlackJack!")
            pause_for_dramatic_effect()
            break
        if PLAYER.has_bust():
            WINNER = DEALER
            print("Ah fuck - you bust!")
            pause_for_dramatic_effect()
            break

        if PLAYER.ask_for_hit():
            PLAYER.cards.append(DECK.draw())
        else:
            break

    # Un-hide the card
    DEALER.cards[1].hidden = False

    # If the player has bust then no need for the dealer to play
    if WINNER != DEALER:
        time.sleep(1)
        # Dealer Hit Phase (if player hasn't bust)
        while True:
            TABLE.draw_table()
            if DEALER.get_true_value() < 17:
                DEALER.cards.append(DECK.draw())
                time.sleep(1)
            else:
                break

        if PLAYER.get_true_value() > DEALER.get_true_value():
            WINNER = PLAYER
        elif PLAYER.has_blackjack() and DEALER.has_blackjack():
            WINNER = None
        elif PLAYER.get_true_value() == DEALER.get_true_value():
            WINNER = None
        elif DEALER.has_bust():
            WINNER = PLAYER
        else:
            WINNER = DEALER

    # Money Adjustment Phase
    if WINNER == DEALER:
        print(f"The dealer has won. Say bye-bye to {PLAYER.current_bet} CP coins!")
        pause_for_dramatic_effect()
    elif WINNER == PLAYER:
        print(f"The dealer has lost. Say hello to {PLAYER.current_bet} CP coins!")
        PLAYER.money += PLAYER.current_bet * 2
        pause_for_dramatic_effect()
    else:
        print(f"The dealer has drawn with you. Your bet was returned to you.")
        pause_for_dramatic_effect()
        PLAYER.money += PLAYER.current_bet

    # Reset Phase
    PLAYER.current_bet = 0
    PLAYER.cards = []
    DEALER.cards = []

    DECK.reset()
    first_time_loop = False
    WINNER = None

clear_console()

if PLAYER.money < 1:
    print("Unfortunately you have no more money left - fuck off.")
else:
    print(f"You ended up with {PLAYER.money} CP coins.")