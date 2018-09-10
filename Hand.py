
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0

    def check(self):
        """
        Checks if hand is still valid
        :return: bool if hand valid
        """
        return self.value <= 21

    def draw(self, card):
        """
        Adds a card to the hand
        :param card: expects a Cards Object
        :return: n/a
        """
        self.cards.append(self, card)
        self.value += card.value

    def __str__(self):
        pass
