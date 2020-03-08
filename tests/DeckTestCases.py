import unittest

from WAR.Deck import Deck
from WAR.Suit import SUIT


class DeckTestCases(unittest.TestCase):
    def setUp(self):
        print("\nSet up in process.")
        deck = Deck()
        self.cards = deck.get_cards()
        print("Set up complete.")

    def test_len_of_cards(self):
        print("******Running tests for length of cards in a deck******")
        self.assertEqual(len(self.cards), 52)
        print("Completed tests for length of cards in a deck")

    def test_spades_in_cards(self):
        print("******Running tests for cards of spade in a deck******")
        spades = list(filter(lambda x: x.get_suit() == SUIT.SPADE, self.cards))
        self.assertEqual(len(spades), 13)
        self.assertEqual(spades[0].get_face_value(), 1)
        print("Completed tests for cards of spade in a deck")

    def test_hearts_in_cards(self):
        print("******Running tests for cards of heart in a deck******")
        hearts = list(filter(lambda x: x.get_suit() == SUIT.HEART, self.cards))
        self.assertEqual(len(hearts), 13)
        self.assertEqual(hearts[1].get_face_value(), 2)
        print("Completed tests for cards of heart in a deck")

    def test_diamonds_in_cards(self):
        print("******Running tests for cards of diamond in a deck******")
        diamonds = list(filter(lambda x: x.get_suit() == SUIT.DIAMOND, self.cards))
        self.assertEqual(len(diamonds), 13)
        self.assertEqual(diamonds[2].get_face_value(), 3)
        print("Completed tests for cards of diamond in a deck")

    def test_clubs_in_cards(self):
        print("******Running tests for cards of club in a deck******")
        clubs = list(filter(lambda x: x.get_suit() == SUIT.CLUB, self.cards))
        self.assertEqual(len(clubs), 13)
        self.assertEqual(clubs[3].get_face_value(), 4)
        print("Completed tests for cards of club in a deck")


if __name__ == '__main__':
    unittest.main()