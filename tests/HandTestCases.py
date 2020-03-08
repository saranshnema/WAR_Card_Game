import unittest

from WAR.Deck import Deck
from WAR.Hand import Hand
from WAR.Suit import SUIT


class HandTestCases(unittest.TestCase):
    def setUp(self):
        print("\nSet up in process.")
        deck = Deck()
        self.cards = deck.get_cards()
        self.hand = Hand()
        print("Set up complete.")

    def test_add_card(self):
        print("******Running tests for adding a card in hand******")
        self.hand.add_card(self.cards[0])
        self.assertTrue(self.hand.has_cards)
        self.assertEqual(self.hand.__str__(), "1 of HEART")
        print("Completed tests for adding a card in hand")

    def test_take_top(self):
        print("******Running tests for taking the top card from hand******")
        self.assertFalse(self.hand.has_cards)
        self.hand.add_card(self.cards[0])
        self.assertTrue(self.hand.has_cards)
        hand_card = self.hand.take_top()
        self.assertEqual(hand_card.get_face_value(), 1)
        self.assertEqual(hand_card.get_suit(), SUIT.HEART)
        print("Completed tests for taking the top card from hand")

    def test_add_all(self):
        print("******Running tests for adding multiple cards to the hand******")
        self.assertFalse(self.hand.has_cards)
        self.hand.add_all(self.cards)
        self.assertTrue(self.hand.has_cards)
        self.assertEqual(len(self.hand.cards), 52)
        print("Completed tests for adding multiple cards to the hand")


if __name__ == '__main__':
    unittest.main()
