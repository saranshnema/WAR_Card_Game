import unittest

from WAR.Deck import Deck
from WAR.Suit import SUIT


class DeckTestCases(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        self.cards = deck.get_cards()

    def test_len_of_cards(self):
        self.assertEqual(len(self.cards), 52)

    def test_spades_in_cards(self):
        spades = list(filter(lambda x: x.get_suit() == SUIT.SPADE, self.cards))
        self.assertEqual(len(spades), 13)
        self.assertEqual(spades[0].get_face_value(), 1)

    def test_hearts_in_cards(self):
        hearts = list(filter(lambda x: x.get_suit() == SUIT.HEART, self.cards))
        self.assertEqual(len(hearts), 13)
        self.assertEqual(hearts[1].get_face_value(), 2)

    def test_diamonds_in_cards(self):
        diamonds = list(filter(lambda x: x.get_suit() == SUIT.DIAMOND, self.cards))
        self.assertEqual(len(diamonds), 13)
        self.assertEqual(diamonds[2].get_face_value(), 3)

    def test_clubs_in_cards(self):
        clubs = list(filter(lambda x: x.get_suit() == SUIT.CLUB, self.cards))
        self.assertEqual(len(clubs), 13)
        self.assertEqual(clubs[3].get_face_value(), 4)


if __name__ == '__main__':
    unittest.main()