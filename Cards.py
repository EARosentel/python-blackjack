class Cards:
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
              'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        self.value = Cards.values(face)

    def __str__(self):
        print(f'{self.face} of {self.suit}')
