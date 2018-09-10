import Player, Deck


def get_player_info(player):
    pname = input('What is your name? ')
    pbank = input('How much money do you want to play with? ')
    player.set_name(pname)
    player.set_bank(pbank)


def display_table(player, computer):
    print(computer)
    print()
    print(player)


if __name__ == '__main__':

    # set up computer player/house/dealer
    dealer = Player()
    dealer.set_name('Dealer')
    dealer.set_bank(1000000)

    player1 = Player()
    get_player_info(player1)

    deck = Deck()

    while True:
        # game set up
        deck.shuffle()
        player1.reset_hand()
        dealer.reset_hand()

        # deal initial cards
        player1.draw_card(deck.deal())
        player1.draw_card(deck.deal())
        dealer.draw_card(deck.deal())
        dealer.draw_card(deck.deal())


        


