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

""" Contains the Deck class required to play blackjack """
from collections import namedtuple
from random import shuffle, randint

Card = namedtuple("Card", ["rank", "suit"])

"""this code turns the suits and values into the card names"""


def stringify_card(input_card):
    """returns easy to read string of card"""
    return f"[{input_card.rank} {input_card.suit}]"


def int_card_value(input_card):
    """returns card rank"""
    return RANKTOVALUE[input_card.rank]


def is_ace(input_card):
    """is the card an ace"""
    return input_card.rank == "Ace"


RANKS = "Ace 2 3 4 5 6 7 8 9 10 Jack Queen King".split()
SUITS = "♦ ♠ ♥ ♣".split()
VALUES = list(range(1, 11)) + [10, 10, 10]
RANKTOVALUE = dict(zip(RANKS, VALUES))

Card.__str__ = stringify_card

Card.__int__ = int_card_value


def card_value(card):
    """returns value of a card"""
    return RANKTOVALUE[card.rank]


# hand = [Card("Ace", "Diamond"), Card("Queen", "Diamond")]
# print(", ".join(map(str, hand)))

# print(f"The sum of the hand is {sum(map(int, hand))}")


def sum_hand(hand):
    """Gets list of cards and returns its value"""
    num_aces = sum(map(is_ace, hand))
    hand_value = sum(map(int, hand))

    if hand_value <= 21:
        for _ in range(num_aces):
            if hand_value + 10 <= 21:
                hand_value += 10
    return hand_value


# print(f"The real sum of te hand is {sum_hand(hand)}")

# card is named tuple Card = namedtuple('Card', ['rank', 'suit'])
# deck is list of tuples
# deck class contains the list of tuples for easy


def make_new_deck(deck_number=1):
    """Creates a new deck"""
    card_list = [Card(rank, suit) for suit in SUITS for rank in RANKS]
    while deck_number > 1:
        card_list += [Card(rank, suit) for suit in SUITS for rank in RANKS]
        deck_number -= 1
    return card_list


class Deck:
    """Deck class that can contain multiple decks"""

    def __init__(self, number_of_decks=1):
        """contains the list of cards and number of decks"""
        self._cards = make_new_deck(number_of_decks)
        self._number_of_decks = number_of_decks
        self._cut_card_position = (len(self._cards) / 2) + randint(-15, 15)

    def shuffle(self):
        """shuffles cards"""
        shuffle(self._cards)

    def cut_cards(self):
        """cuts list with a random error"""
        cut_point = (len(self._cards) / 2) + randint(-15, 15)
        upperhalf = self._cards[:cut_point]
        lowerhalf = self._cards[cut_point:]
        self._cards = upperhalf + lowerhalf

    def print_cards(self):
        """prints all cards in the deck"""
        print(", ".join(map(str, self._cards)))

    def remove_top_card(self):
        """removes top card of deck"""
        # The last card in the list is the "top"
        self._cards.pop()

    def show_top_card(self):
        """returns top card"""
        top_card = self._cards[len(self._cards) - 1]
        return top_card

    def set_cut(self):
        """resets cut card postion"""
        self._cut_card_position = (len(self._cards) / 2) + randint(-15, 15)

    def pass_cut(self):
        """returns bool of passed cut card"""
        return bool(len(self._cards) < self._cut_card_position)
