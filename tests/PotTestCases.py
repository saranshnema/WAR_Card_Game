import unittest

from WAR.Deck import Deck
from WAR.Hand import Hand
from WAR.Player import Player
from WAR.Pot import Pot


class PotTestCases(unittest.TestCase):
    def setUp(self):
        print("\nSet up in process.")
        deck = Deck()
        self.cards = deck.get_cards()
        self.hand1 = Hand()
        self.hand2 = Hand()
        self.player1 = Player("A", self.hand1)
        self.player2 = Player("B", self.hand2)
        self.pot = Pot()
        print("Set up complete.")

    def test_add_card(self):
        print("******Running tests to add a card into the pot******")
        card_1 = self.cards.pop()
        card_2 = self.cards.pop()

        self.pot.add_card(card_1, self.player1)
        self.assertIn(card_1, self.pot.cards)
        self.assertIn(self.player1, self.pot.players)

        self.pot.add_card(card_2, self.player2)
        self.assertIn(card_2, self.pot.cards)
        self.assertIn(self.player2, self.pot.players)

        self.assertEqual(card_1, self.pot.cards[0])
        self.assertEqual(card_2, self.pot.cards[1])

        self.assertEqual(self.player1, self.pot.players[0])
        self.assertEqual(self.player2, self.pot.players[1])

        self.assertEqual(len(self.pot.bonus), 0)
        print("Completed tests to add a card into the pot")

    def test_add_bonus(self):
        print("******Running tests to add cards into the bonus bucket******")
        self.pot.add_bonus([self.cards.pop(), self.cards.pop()])
        self.assertEqual(len(self.pot.bonus), 2)
        print("Completed Running tests to add cards into the bonus bucket")

    def test_winner(self):
        print("******Running tests to get a winner from a round******")
        self.test_add_card()
        self.assertEqual(self.pot.winner.name, "A")
        self.assertEqual(self.pot.best, 13)
        print("Completed tests to get a winner from a round")

    def test_reward(self):
        print("******Running tests to give reward to a winner******")
        self.test_add_card()
        self.pot.reward(self.player1)
        self.assertEqual(len(self.hand1.cards), 2)
        print("Completed tests to give reward to a winner")

    def test_tied(self):
        print("******Running tests to identify players involved in a tie******")
        card = self.cards.pop()
        self.pot.add_card(card, self.player1)
        self.pot.add_card(card, self.player2)

        self.assertFalse(self.pot.winner)

        tied_players = []

        for player in self.pot.tied:
            tied_players.append(player)

        self.assertIn(self.player1, tied_players)
        self.assertIn(self.player2, tied_players)
        print("Completed tests to identify players involved in a tie")


if __name__ == '__main__':
    unittest.main()
