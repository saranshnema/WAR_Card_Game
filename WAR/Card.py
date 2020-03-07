"""
This is Card class that helps create an object of each playing card in a given deck.
This object will have a Suit and a card value.
"""


class Card:
    def __init__(self, suit, face_value):
        """
        Constructor that initialize with following values
        :param suit: Enum from Suit Enum class
        :param face_value: Can range from 1-13 both included
        """
        self.__suit = suit
        self.__face_value = face_value

    def get_suit(self):
        """
        :return: Returns suit of a card
        """
        return self.__suit

    def get_face_value(self):
        """
        :return: Returns value of a given card
        """
        return self.__face_value

    def __str__(self):
        """
        Example - 6 of SPADE
        :return: String representation of a Object.
        """
        return '{} of {}'.format(self.__face_value, self.__suit.name)
