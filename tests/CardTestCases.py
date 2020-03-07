import unittest

from WAR.Card import Card
from WAR.Suit import SUIT


class CardTestCases(unittest.TestCase):
    def setUp(self):
        self.card1 = Card(SUIT.SPADE, 1)
        self.card2 = Card(SUIT.CLUB, 2)
        self.card3 = Card(SUIT.DIAMOND, 3)
        self.card4 = Card(SUIT.HEART, 4)

    def test_get_suit(self):
        self.assertEqual(self.card1.get_suit(), SUIT.SPADE)
        self.assertEqual(self.card2.get_suit(), SUIT.CLUB)
        self.assertEqual(self.card3.get_suit(), SUIT.DIAMOND)
        self.assertEqual(self.card4.get_suit(), SUIT.HEART)

    def test_get_face_value(self):
        self.assertEqual(self.card1.get_face_value(), 1)
        self.assertEqual(self.card2.get_face_value(), 2)
        self.assertEqual(self.card3.get_face_value(), 3)
        self.assertEqual(self.card4.get_face_value(), 4)

    def test_get_string_repr(self):
        self.assertEqual(self.card1.__str__(), "1 of SPADE")
        self.assertEqual(self.card2.__str__(), "2 of CLUB")
        self.assertEqual(self.card3.__str__(), "3 of DIAMOND")
        self.assertEqual(self.card4.__str__(), "4 of HEART")


if __name__ == '__main__':
    unittest.main()
