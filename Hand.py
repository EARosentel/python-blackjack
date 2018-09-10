
class Hand:

    def __init__(self):
        self.cards = 0
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
        self.cards += 1
        self.value += card.value
