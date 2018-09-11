import Player
import Deck


def get_player_info(player):
    pname = input('What is your name? ')
    pbank = input('How much money do you want to play with? ')
    player.set_name(pname)
    player.set_bank(pbank)


def display_table(player, computer, show_all):
    if show_all:
        print(computer.hand)
    else:
        print(computer.hand.show_first_card())

    print()
    print(player.hand)

def play_again():
    return input('Would you like to keep playing? (Y/N) ')
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

        # show board - pass in false for show all attribute
        display_table(player1, dealer, show_all=False)

        # set game variable
        game_on = True

        # player1 - hit or stay
        hit = True
        while hit:
            response = input('Would you like to hit or stay? (Y/N)')
            if response.upper() == 'Y':
                player1.draw_card(deck.deal())
                if player1.get_hand_total() < 21:
                    pass
                elif player1.get_hand_total() == 21:
                    game_on = player1.hit_21()
                    break
                else:
                    player1.bust()
                    game_on = dealer.win()
                    break
            else:
                hit = False

        # dealer - hit until win or bust
        while game_on:
            dealer.draw_card(deck.deal())

            if dealer.get_hand_total() > 21:
                dealer.bust()
                game_on = player1.win()
                break
            elif dealer.get_hand_total() == 21:
                game_on = dealer.hit_21()
                break
            elif dealer.get_hand_total() > player1.get_hand_total():
                game_on = dealer.win()
                break

        # if game is over
        if not game_on:
            if play_again().upper() != 'Y':
                break
            else:
                continue

        # game really should be over by now
        else:
            print('Something is very wrong here. No end of game declared.')

    # exited while loop by saying no to play again prompt
    print(f"Thank you for playing, {player1.name}. Have a nice day.")
