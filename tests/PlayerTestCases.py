import unittest

from WAR.Deck import Deck
from WAR.Hand import Hand
from WAR.Player import Player
from WAR.Pot import Pot


class PlayerTestCases(unittest.TestCase):
    def setUp(self):
        deck = Deck()
        self.cards = deck.get_cards()
        self.hand1 = Hand()
        self.hand2 = Hand()
        self.player1 = Player("A", self.hand1)
        self.player2 = Player("B", self.hand2)
        self.pot = Pot()

    def test_name(self):
        self.assertEqual(self.player1.name, "A")
        self.assertEqual(self.player2.name, "B")

    def test_drop_card(self):
        self.hand1.add_card(self.cards.pop())

        self.assertTrue(self.player1.hand.has_cards)
        self.assertEqual(len(self.pot.cards), 0)

        self.player1.drop_card(self.pot)

        self.assertFalse(self.player1.hand.has_cards)
        self.assertEqual(len(self.pot.cards), 1)

    def test_drop_bonus(self):
        self.hand1.add_card(self.cards.pop())
        self.hand1.add_card(self.cards.pop())
        self.hand1.add_card(self.cards.pop())

        self.assertTrue(self.player1.hand.has_cards)
        self.assertEqual(len(self.pot.bonus), 0)

        self.player1.drop_bonus(self.pot, 3)

        self.assertFalse(self.player1.hand.has_cards)
        self.assertEqual(len(self.pot.bonus), 3)

    def test_give_cards(self):
        self.assertFalse(self.player1.hand.has_cards)
        cards = []
        for _ in range(3):
            cards.append(self.cards.pop())
        self.player1.give_cards(cards)
        self.assertTrue(self.player1.hand.has_cards)
        self.assertEqual(len(self.player1.hand.cards), 3)

if __name__ == '__main__':
    unittest.main()
