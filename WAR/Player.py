class Player:

    def __init__(self, name, hand):
        self.name, self.hand = name, hand

    def drop_card(self, playing_pot):
        if self.hand.has_cards:
            playing_pot.add_card(self.hand.take_top(), self)

    def drop_bonus(self, playing_pot, count):
        playing_pot.add_bonus(self.hand.cards[:count])
        self.hand.cards = self.hand.cards[count:]

    def give_cards(self, cards):
        self.hand.add_all(cards)

    def show_hand(self):
        print("Player {} have following cards - ".format(self.name))
        print(self.hand)