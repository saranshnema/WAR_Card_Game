"""
This class is used to a player. It maintains players name and player hand.
This class helps perform action on behalf of a player like playing a card
from hand and take back cards into the hand.
"""


class Player:

    def __init__(self, name, hand):
        """
        Constructor that maintains name of the player and hand of a player
        :param name: Name of the player
        :param hand: Hand object of the player
        """
        self.name, self.hand = name, hand

    def drop_card(self, playing_pot):
        """
        This method is used to drop a card in playing pot if a player has
        any card in his/her hand.
        :param playing_pot: Pot object of a given round
        :return: None
        """
        if self.hand.has_cards:
            playing_pot.add_card(self.hand.take_top(), self)

    def drop_bonus(self, playing_pot, count):
        """
        This method is used to drop n number of cards in the playing pot's
        bonus bucket of the given round.
        :param playing_pot: Object of the playing pot
        :param count: Number of cards to drop
        :return: None
        """
        playing_pot.add_bonus(self.hand.cards[:count])
        self.hand.cards = self.hand.cards[count:]

    def give_cards(self, cards):
        """
        This method is used to add cards to a players hand
        :param cards: list of cards
        :return: None
        """
        self.hand.add_all(cards)

    def show_hand(self):
        """
        This method is used to print all the cards in players hand
        :return: None
        """
        print("Player {} have following cards - ".format(self.name))
        print(self.hand)