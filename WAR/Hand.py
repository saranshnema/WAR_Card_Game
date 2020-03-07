"""
This class is used to simulate a bunch of card in any players hand.
Just like a real life person, this class will help add cards to hand,
take first card from the hand, or add cards to the hand.
"""


class Hand:

    def __init__(self):
        """
        Initializes card list to populate the cards
        """
        self.cards = []

    def __str__(self):
        """
        String representation of all the cards in hand
        :return:
        """
        return ', '.join(map(str, self.cards))

    def add_card(self, card):
        """
        Method used to add cards to hand
        :param card: Object of a card
        :return: None
        """
        self.cards.append(card)

    def take_top(self):
        """
        :return: First card in hand
        """
        return self.cards.pop(0)

    def add_all(self, cards):
        """
        Add a bunch of cards to hand
        :param cards: List of card objects
        :return: None
        """
        self.cards.extend(cards)

    @property
    def has_cards(self):
        """
        Returns if there are cards in players hand or not
        :return: True or False
        """
        return bool(self.cards)
