#! /usr/bin/env python3
# Arturo Silva
# CPSC 386-00
# 2022-07-24
# arturitosilva20@csu.fullerton.edu
# @ArturoSilva20
#
# Lab 07-01
#
# Simple BlackJack game
#

"""Player Module covers the dealer and bots"""

from blackjackgame import cards


class Player:
    """Blackjack Player Class"""

    def __init__(self, bankroll, name):
        """Initialize a player"""
        # the player's hand is a list, there is no separate class
        self._hand = []
        self._bankroll = bankroll
        self._name = name
        self._bet = 0

    def ask_for_bet(self):
        """Prompt and gather a bet from a player, returns integer"""
        # deducts from self._bankroll
        print("Bank: " + str(self._bankroll))
        self._bet = int(input(self._name + "'s Bet: "))
        while self._bet > self._bankroll:
            self._bet = int(input("Choose a lower Bet: "))
        self._bankroll -= self._bet
        print("")

    def does_double_down(self):
        """Asks player if they want to double down, returns boolean"""
        player_input = input(self._name + " Double down?(Yes/No): ")
        if self._bet < self._bankroll:
            if bool(player_input in ("Yes", "yes")):
                self._bankroll -= self._bet
                self._bet += self._bet
                return True
            return False
        return False

    def does_hit(self):
        """Asks player if they want to hit, returns boolean"""
        if self.hand_val() < 21:
            return bool(input(self._name + "Hit?: ") in ("Yes", "yes"))
        print("Busted!")
        return False

    def hand_val(self):
        """Returns the value of the current hand"""
        # Uses function from cards module to sum the cards and return the sum
        return cards.sum_hand(self._hand)

    def add_card(self, card):
        """adds card to hand"""
        self._hand += [card]

    def display_hand(self):
        """displays current hand"""
        print(self._name + "'s Hand:")
        for card in self._hand:
            print(card)
        print("")

    def clear_hand(self):
        """clears hand"""
        self._hand = []

    @property
    def bankroll(self):
        """Return the current bankroll"""
        return self._bankroll

    @property
    def name(self):
        """returns name"""
        return self._name

    def push(self):
        """bet returns to bank"""
        self._bankroll += self._bet
        self._bet = 0
        print(self._name + " Push")
        print("")

    def remove_bet(self):
        """clears bet"""
        self._bet = 0
        print(self._name + " Lost")
        print("")

    def receive_winnings(self):
        """Receive the money won, recieve 0.00 if we lost"""
        self._bankroll += self._bet * 2
        self._bet = 0
        print(self._name + " Won!")
        print("")


class Dealer(Player):
    """Blackjack Dealer Class"""

    def __init__(self, bankroll=-1, name="Dealer"):
        """initialize default values"""
        super().__init__(bankroll, name)

    def ask_for_bet(self):
        """Dealer doesn't bet"""
        return

    def does_double_down(self):
        """Dealer doesn't double down"""
        return False

    def does_hit(self):
        """dealer only hits when hand_value is less than 17"""
        if self.hand_val() < 17:
            return True
        return False

    def display_hand(self):
        """Only displays first card in hand"""
        print(self._name + "'s Hand:")
        print(self._hand[0])
        print("[Hidden]")
        print("")

    def reveal_cards(self):
        """reveals dealer's cards"""
        print(self._name + "'s Hand:")
        for card in self._hand:
            print(card)
        print("")
