import Player


def get_player_info(player):
    pname = input('What is your name? ')
    pbank = input('How much money do you want to play with? ')
    player.set_name(pname)
    player.set_bank(pbank)








if __name__ == '__main__':

    # set up computer player/house/dealer
    dealer = Player()
    dealer.set_name('Dealer')
    dealer.set_bank(1000000)

    player1 = Player()
    get_player_info(player1)

    while True:
        
        pass


