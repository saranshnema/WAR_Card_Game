import math

from WAR.Deck import Deck
from WAR.Hand import Hand
from WAR.Player import Player
from random import shuffle

from WAR.Pot import Pot

"""
This is the driver class of WAR game. This keeps track of each player in a given round.
This class starts and ends the game upon the appropriate given end condition.
2-52 Players can play this game. Game is ended when a player wins all the cards.
Players are evicted from the game when they loose all their cards in hand to other
player. 
"""


class Game:
    def __init__(self, player_names):
        """
        Constructor that contains Player, playing cards and maintain round count.
        This also takes care of shuffling the cards before distribution amongst the players.
        """
        self.player_names = player_names
        self.players = []
        self.get_cards()
        shuffle(self.cards)
        self.rounds = 0

    def get_cards(self):
        player_count = len(self.player_names)
        deck = Deck()
        self.cards = []
        min_cards = player_count * 15
        if min_cards <= 52:
            self.cards = deck.get_cards()
        else:
            min_deck = math.ceil(min_cards / 52)
            while min_deck:
                self.cards.extend(deck.get_cards())
                min_deck -= 1
        print(len(self.cards))

    def distribute_cards(self):
        """
        This method helps distribute equal number of cards amongst players
        playing in the game.
        :return: None
        """
        hands = [player.hand for player in self.players]
        while len(self.cards) >= len(self.players):
            for hand in hands:
                hand.add_card(self.cards.pop())

    def create_game(self):
        """
        This method creates the game instance by creating players, distributing
        equal cards to each player and finally showing which player got which card.
        :param player_names: Names of each player involved in the game.
        :return: None
        """
        for name in self.player_names:
            self.players.append(Player(name, Hand()))

        self.distribute_cards()

        for player in self.players:
            player.show_hand()

    def start_next_round(self, tied_players=None):
        """
        This method starts any given round. In a round all players play a card
        from their hand. A winner is decided based on cards added to the playing
        pot. If there is a tie amongst two or more player then this round is called
        again to play a round amongst the tied player to resolve the tie and
        identify a winner.
        :param tied_players: Tied player
        :return: Winner of the round
        """
        if tied_players is None:
            self.increment_round()
        if tied_players:
            print("*** Tie Resolution ***")
        current_playing_pot = Pot()
        for player in (self.players if tied_players is None else tied_players):
            player.drop_card(current_playing_pot)
            if tied_players:
                player.drop_bonus(current_playing_pot, 3)
        winner = current_playing_pot.winner
        if winner:
            print("Player {} won round {}.".format(winner.name, self.rounds))
        if winner is not None:
            current_playing_pot.reward(winner)
        else:
            print("!!! Tie Occurred !!!")
            winner = self.start_next_round(current_playing_pot.tied)
            current_playing_pot.reward(winner)
        return winner

    def increment_round(self):
        """
        This method is used to increment round count
        and print a separator on console.
        :return: None
        """
        self.rounds += 1
        print('============================')

    def start_game(self):
        """
        This is the driver method that plays round until game has ended.
        Once the game end, it calls the end_game method to declare a winner.
        :return: None
        """
        while not self.has_game_ended:
            self.start_next_round()
        self.end_game()

    def end_game(self):
        """
        This method is used to declare the winner
        :return: None
        """
        for player in self.players:
            if player.hand.has_cards:
                print()
                print("Player", player.name, 'wins the game by winning all the cards !!!')
                break

    @property
    def has_game_ended(self):
        """
        This is used to identify if there is only one player in the game that has cards in his/her hand.
        :return:  True or False based on condition mentioned above.
        """
        return sum(bool(player.hand.cards) for player in self.players) == 1
