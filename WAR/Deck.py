import datetime

from WAR.Card import Card
from WAR.Suit import SUIT

"""
This is Deck class that works as a collection of Card objects.
This is used to simulate real life deck of 52 playing cards. 
"""


class Deck:

    def __init__(self):
        """
        Constructor that creates collection of cards and stores
        the timestamp of creation.
        """
        self.__cards = []
        self.__creation_date = datetime.date.today()
        for suit in SUIT:
            for value in range(1, 14):
                self.__cards.append(Card(suit, value))

    def get_cards(self):
        """
        :return: Returns collection of 52 playing cards
        """
        return self.__cards
