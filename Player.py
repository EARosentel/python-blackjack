import Hand


class Player:

    def __init__(self):
        self.hand = Hand()
        self.name = ""
        self.bank = 0

    def __str__(self):
        return f"{self.name} has {self.hand.__str__()} in his hand and ${self.bank} in their bank."

    def update_bank(self, bet_amount):
        self.bank += bet_amount

    def set_name(self, pname):
        self.name = pname

    def set_bank(self, pbank):
        self.bank = pbank




