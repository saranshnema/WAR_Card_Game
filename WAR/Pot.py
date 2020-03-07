"""
This method simulates the center part of table where game is being played.
Players throw in the cards on the table. In case of a tie extra cards which
are known as bonus cards are also played here.
"""


class Pot:

    def __init__(self):
        """
        Constructor that maintains list of cards played in a round,
        players involved in the round, in case of a tie extra cards(bonus)
        being played in the round
        """
        self.cards = []
        self.players = []
        self.bonus = []

    def add_card(self, card, player):
        """
        This method is used to add card and player to respective
        buckets when they play a card in any given round.
        :param card: Card played
        :param player: Player who played the card
        :return: None
        """
        self.cards.append(card)
        self.players.append(player)

    def add_bonus(self, cards):
        """
        This method is adds all the bonus cards to bonus bucket
        :param cards: list of cards
        :return: None
        """
        self.bonus.extend(cards)

    @property
    def winner(self):
        """
        This method is used to identify the max valued card played in the round,
        and the player who played that card. This method also helps identify the
        tie in any given round.
        :return: Winner player or None in case of tie
        """
        self.show_pot()
        values = [card.get_face_value() for card in self.cards]
        self.best = max(values)
        if values.count(self.best) == 1:
            return self.players[values.index(self.best)]

    def show_pot(self):
        """
        This method prints cards played by each player in the given round
        :return: None
        """
        for player, card in zip(self.players, self.cards):
            print('Player {} played {}.'.format(player.name, card))

    def reward(self, player):
        """
        This method gives all the cards i.e cards bucket and bonus bucket
        to the winner player
        :param player: Winner of the round
        :return: None
        """
        player.give_cards(self.cards)
        player.give_cards(self.bonus)

    @property
    def tied(self):
        """
        In case of a tie this method provides player only those players
        that are involved in the tie and have the highest ranking card.
        :return: Player involved in the tie
        """
        for card, player in zip(self.cards, self.players):
            if card.get_face_value() == self.best:
                yield player
