import random
import Cards


class Deck:

    cards = 52
    faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

    def __init__(self):
        self.cards = []
        for face in Deck.faces:
            for suit in Deck.suits:
                self.cards.append(self, Cards.Cards(suit, face))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        for card in self.cards:
            print(card)

    def deal(self):
        return self.cards.pop(self)

