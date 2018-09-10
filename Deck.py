import random
import Cards


class Deck:

    faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

    def __init__(self):
        """
        Initializes a deck in order
        """

        self.cards = []
        for face in Deck.faces:
            for suit in Deck.suits:
                self.cards.append(self, Cards.Cards(suit, face))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        """
        Adds each card to the result string in parentheses with a comma after
        :return: The result string minus the last character, which would be an extra comma
        """
        result = ""
        for card in self.cards:
            result.append(f"({card.__str__()}),")
        return result[0:-1]

    def deal(self):
        """
        Removes one card from the deck
        :return: removed card
        """
        return self.cards.pop(self)

