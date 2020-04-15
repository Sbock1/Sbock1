# TODO: create Blackjack
import random

import self as self

player = 0
player_hand_value = 0
player_hand_cards = []
dealer_hand_value = 0
dealer_hand_cards = []
bet = 0
budget = 200
game_over = 0


class Player(object):
    global budget

    def __init__(self, hand):
        pass

    def give_budget(self):
        self.budget += 100


class Cards(object):
    def __init__(self, cards_type=["Kreuz", "Herz", "Pike", "Karo"],
                 cards=["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "11"],
                 cards_value=[2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11], cards_stable=[]):
        self.cards_type = cards_type
        self.cards = cards
        self.cards_value = cards_value
        self.cards_stable = cards_stable
        self.game_over = game_over

        for elem in self.cards_type:
            for elem2 in self.cards:
                self.cards_stable.append(elem + " " + elem2)

        self.cards_value = int(len(self.cards_stable) / len(self.cards_value)) * self.cards_value
        self.cards_stable = dict(zip(self.cards_stable, self.cards_value))

    def give_card(self):
        global player, player_hand_value, player_hand_cards, dealer_hand_value, dealer_hand_cards, game_over
        if self.cards_stable is not {}:
            card = random.choice(list(self.cards_stable.items()))
            self.cards_stable.pop(card[0])
            if player == 0:
                player_hand_cards.append(card)
                return card
            else:
                dealer_hand_cards.append(card)
                return card
        else:
            print("The game is over, all cards were dealt!")
            game_over = 1


class Game(object):
    def __init__(self):
        pass

    def switch_players(self):
        global player
        if player == 0:
            player = 1
        else:
            player = 0

    def calc_hand_val(self):
        global player_hand_value, dealer_hand_value
        summe = 0
        if player == 0:
            for elem in player_hand_cards:
                summe += elem[1]
            print(summe)
        else:
            for elem in dealer_hand_cards:
                summe += elem[1]
            dealer_hand_value = 10

    def win_condition(self):
        global game_over
        if (player_hand_value or dealer_hand_value) <= 21:
            print(f"The game is still going on.")
        elif player_hand_value >= 22:
            print("You have lost!")
            game_over = 1
        elif dealer_hand_value >= 22:
            print("Dealer has lost!")
            game_over = 1


def test():
    global player_hand_value
    player_hand_value += 10
# while game_over == 0:
#   print("Hello, we are playing Blackjack!\nYou are going first."
#        f"Your budget is {budget}")
# bet = input("Please place your bet: ")
# game = Game()
