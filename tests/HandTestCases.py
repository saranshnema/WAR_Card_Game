import unittest

from WAR.Deck import Deck
from WAR.Hand import Hand
from WAR.Suit import SUIT


class HandTestCases(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        self.cards = deck.get_cards()
        self.hand = Hand()

    def test_add_card(self):
        self.hand.add_card(self.cards[0])
        self.assertTrue(self.hand.has_cards)
        self.assertEqual(self.hand.__str__(), "1 of HEART")

    def test_take_top(self):
        self.assertFalse(self.hand.has_cards)
        self.hand.add_card(self.cards[0])
        self.assertTrue(self.hand.has_cards)
        hand_card = self.hand.take_top()
        self.assertEqual(hand_card.get_face_value(), 1)
        self.assertEqual(hand_card.get_suit(), SUIT.HEART)

    def test_add_all(self):
        self.assertFalse(self.hand.has_cards)
        self.hand.add_all(self.cards)
        self.assertTrue(self.hand.has_cards)
        self.assertEqual(len(self.hand.cards), 52)


if __name__ == '__main__':
    unittest.main()
