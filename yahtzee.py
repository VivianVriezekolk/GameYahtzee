import random
import players

class Yatzee:
    def __init__(self):
        self.players = []
        self.dice_eyes = []

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

    def roll_dices(self, k_number):
        new_dices = []
        length = len(k_number)
        for index, number in enumerate(self.dice_eyes):
            if str(number) in k_number and length != 0:
                self.dice_eyes[index] = random.randint(1, 6)
                length -= 1
        return self.dice_eyes

    def roll_again(self, k_numbers):
        if Yatzee.check_knumbers(self, k_numbers):
            new_eyes = Yatzee.roll_dices(self, k_numbers)
            self.dice_eyes = new_eyes
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