import random
import players

class Yatzee:
    def __init__(self):
        self.players = []
        self.dice_eyes = []

    def amount_of_players(self):
        print("Welcome to Yatzee")
        print("With how many players do you want to play?")
        amount_of_players = input()

        for player_number in range(int(amount_of_players)):
            print("What is the name of player " + str(player_number+1) + " ?")
            player = players.Player()
            player.player_number = player_number
            player.name = input()
            self.players.append(player)

    def roll_dice(self):
        numbers = []
        for i in range(5):
            numbers.append(random.randint(1,6))
        self.dice_eyes = numbers

    def check_knumbers(self, k_numbers):
        new_numbers = []
        for number in k_numbers:
            new_numbers.append(int(number))
        if all(x in self.dice_eyes for x in new_numbers):
            for numberb in new_numbers:
                amount = new_numbers.count(numberb)
                if amount > self.dice_eyes.count(numberb):
                    return False
            return True
        else:
            return False

    def remove_die_from_dice_eyes(self, k_number):
        new_dices = []
        for index, number in enumerate(self.dice_eyes):
            if str(number) not in k_number:
                new_dices.append(number)
        return new_dices

    def roll_again(self, k_numbers):
        if Yatzee.check_knumbers(self, k_numbers):
            maintained_eyes = Yatzee.remove_die_from_dice_eyes(self, k_numbers)
            n_numbers = []
            for i in range(len(k_numbers)):
                n_numbers.append(random.randint(1, 6))
            [n_numbers.append(int(n)) for n in maintained_eyes]
            self.dice_eyes = n_numbers
        else:
            print("You did not roll these dice eyes. \n")
            numbers = input("Type the eyes you want to roll again like this: 11. \n")
            Yatzee.roll_again(self, numbers)

    def game_ended(self):
        for player in self.players:
            if not(player.fullCard()):
                return False
        return True

    def determine_winner(self):
        highest_score = 0
        best_player = ''
        for player in self.players:
            if highest_score < player.total_score:
                highest_score = player.total_score
                best_player = player
        return best_player