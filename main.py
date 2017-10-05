import yahtzee
import evaluator

class Main():

    def __init__(self):
        self.yahtzee = yahtzee.Yatzee()

    def startGame(self):
        self.yahtzee.amount_of_players()
        while not(self.yahtzee.game_ended()):
            for player in self.yahtzee.players:
                print('\n' + player.name + " is going to roll the dices. \n")
                self.yahtzee.roll_dice()
                while player.amount_of_throwns < 3:
                    print(self.yahtzee.dice_eyes)
                    roll = input('Do you want to stop or try to get a higher score? Typ 0 for stop and 1 otherwise \n')
                    self.loop(player, roll)
                player.amount_of_throwns = 0
        player = self.yahtzee.determine_winner()
        print(str(player.name) + ' heeft gewonnen met ' + str(player.total_score))

    def loop(self, player, roll):
        if int(roll) == 0 or player.amount_of_throwns == 2:
            strategy = input('\nWhat do you want to do? \n')
            evaluator.Evaluator.dices = self.yahtzee.dice_eyes
            evaluator.Evaluator.evaluate_strategy(self, strategy, player)
            print("")
            print(player.name, player.UPPER_SECTION)
            print(player.LOWER_SECTION)
            player.amount_of_throwns = 3
        else:
            numbers = input("Typ the numbers you want to keep like this: 11 \n")
            self.yahtzee.roll_again(numbers)
            player.amount_of_throwns +=1

main = Main()
main.startGame()






