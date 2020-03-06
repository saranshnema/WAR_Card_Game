from WAR.Deck import Deck
from WAR.Hand import Hand
from WAR.Player import Player
from random import shuffle

from WAR.Pot import Pot


class Game:
    def __init__(self):
        self.players = []
        deck = Deck()
        self.cards = deck.get_cards()
        shuffle(self.cards)
        self.rounds = 0

    def distribute_cards(self):
        hands = [player.hand for player in self.players]
        while len(self.cards) >= len(self.players):
            for hand in hands:
                hand.add_card(self.cards.pop())

    def create_game(self, player_names):
        for name in player_names:
            self.players.append(Player(name, Hand()))

        self.distribute_cards()

        for player in self.players:
            player.show_hand()

    def start_next_round(self, tied_players=None):
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
            print("Player {} won round {}.".format(winner.name,self.rounds))
        if winner is not None:
            current_playing_pot.reward(winner)
        else:
            print("!!! Tie Occurred !!!")
            winner = self.start_next_round(current_playing_pot.tied)
            current_playing_pot.reward(winner)
        return winner

    def increment_round(self):
        self.rounds += 1
        print('============================')

    def start_game(self):
        while not self.has_game_ended:
            self.start_next_round()
        self.end_game()

    def end_game(self):
        for player in self.players:
            if player.hand.has_cards:
                print()
                print("Player", player.name, 'wins the game by winning all the cards !!!')
                break

    @property
    def has_game_ended(self):
        return sum(bool(player.hand.cards) for player in self.players) == 1

