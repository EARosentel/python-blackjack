from Hand import Hand


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

    def get_bank(self):
        return self.bank

    def draw_card(self, card):
        self.hand.draw(card)

    def reset_hand(self):
        self.hand = Hand()

    def get_hand_total(self):
        return self.hand.value

    def hit_21(self, betamount):
        print(f'BLACKJACK!!! {self.name} wins!!')
        self.update_bank(betamount)
        return False

    def bust(self, betamount):
        print(f'{self.name} busts! Game Over')
        self.update_bank(betamount*-1)
        return False

    def win(self, betamount):
        print(f'{self.name} wins!!!')
        self.update_bank(betamount)
        return False

    def lose(self, betamount):
        self.update_bank(betamount*-1)
        return False



