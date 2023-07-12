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

"""game loop required for blackjack"""

import pickle
from os.path import exists
from blackjackgame import cards
from blackjackgame import player


def player_exists(name):
    """checks if player name exists in pickle file"""
    if exists("data.txt"):
        player_list = []
        with open("data.txt", "rb") as file:
            while True:
                try:
                    player_list.append(pickle.load(file))
                except EOFError:
                    break
            for player_x in player_list:
                if player_x.name == name:
                    return player_x
    return False


def create_player(name):
    """creates player if player does not already exist"""
    if player_exists(name):
        return player_exists(name)
    return player.Player(10000, name)


def get_players():
    """gets players"""
    player_list = []
    players = int(input("How many players?: "))
    while players > 4:
        players = int(input("Choose a number less than 5!: "))
    for i in range(players):
        player_name = input("Enter name " + str(i + 1) + ": ")
        player_list += [create_player(player_name)]
    player_list += [player.Dealer()]
    return player_list


def save_players(player_list):
    """saves players to pickle file"""
    with open("data.txt", "wb") as file:
        for player_x in player_list:
            pickle.dump(player_x, file)


def deal_cards(deck, players):
    """Deals one card to each player"""
    for player_x in players:
        player_x.add_card(deck.show_top_card())
        deck.remove_top_card()


def show_cards(players):
    """shows the cards of each player in list"""
    for player_x in players:
        player_x.display_hand()


def ask_action(deck, player_x):
    """ask players for actions"""
    if player_x.hand_val() == 21:
        return

    if player_x.does_double_down():
        player_x.add_card(deck.show_top_card())
        deck.remove_top_card()
        player_x.display_hand()
        return

    if isinstance(player_x, player.Dealer):
        player_x.reveal_cards()

    if player_x.does_hit():
        hit_decision = True
        while hit_decision:
            player_x.add_card(deck.show_top_card())
            deck.remove_top_card()
            if isinstance(player_x, player.Dealer):
                player_x.reveal_cards()
            else:
                player_x.display_hand()
            hit_decision = player_x.does_hit()


def reconcile(players):
    """losers lost, winners gain"""
    for playx in players:
        if isinstance(playx, player.Dealer):
            playx.clear_hand()
            return
        if (players[len(players) - 1].hand_val() < playx.hand_val() <= 21) or (
            playx.hand_val() <= 21 < players[len(players) - 1].hand_val()
        ):
            playx.receive_winnings()
        elif playx.hand_val() == players[len(players) - 1].hand_val() <= 21:
            playx.push()
        else:
            playx.remove_bet()
        playx.clear_hand()


def black_jack():
    """BlackJack game loop"""
    print("BlackJack!")
    player_list = get_players()
    game = True
    deck = cards.Deck(4)
    deck.shuffle()
    deck.set_cut()
    while game:
        if deck.pass_cut():
            deck = cards.Deck(4)
            deck.shuffle()
            deck.set_cut()
        for player_x in player_list:
            player_x.ask_for_bet()
        deal_cards(deck, player_list)
        deal_cards(deck, player_list)
        show_cards(player_list)
        for player_x in player_list:
            ask_action(deck, player_x)
        reconcile(player_list)
        game = bool(input("New Game?: ") in ("Yes", "yes"))

    save_players(player_list)
