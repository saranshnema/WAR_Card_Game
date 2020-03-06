import datetime

from WAR.Card import Card
from WAR.Suit import SUIT


class Deck:

    def __init__(self):
        self.__cards = []
        self.__creation_date = datetime.date.today()
        for suit in SUIT:
            for value in range(1, 14):
                self.__cards.append(Card(suit, value))

    def get_cards(self):
        return self.__cards