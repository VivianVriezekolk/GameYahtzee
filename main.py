import yahtzee
import evaluator
import players
import consoleview

class Main():

    def __init__(self):
        self.yahtzee = yahtzee.Yatzee()
        self.view = consoleview.ConsoleView(self.yahtzee)

    def startGame(self):
        self.amount_of_players()
        while not(self.yahtzee.game_ended()):
            for player in self.yahtzee.players:
                print('\n' + player.name + " is going to roll the dice. \n")
                self.yahtzee.roll_dice()
                while player.amount_of_throwns < 3:
                    self.view.printScores()
                    if(player.amount_of_throwns == 2):
                        print('End of turn.')
                    else:
                        roll = input('Do you want to stop or try to get a higher score? Type "stop" to stop or type the numbers you want to roll again. \n')
                    self.loop(player, roll)
                player.amount_of_throwns = 0
        self.yahtzee.determine_winner()
        self.view.print_winner_of_game()

    def amount_of_players(self):
        self.view.welcome_message()
        amount_of_players = self.view.ask_amount_players()

        for player_number in range(int(amount_of_players)):
            player = players.Player()
            player.player_number = player_number
            self.yahtzee.players.append(player)

        names = self.view.ask_name_of_players()
        for player in self.yahtzee.players:
                player.name = names[player.player_number]

    def loop(self, player, roll):
        if roll == 'stop' or player.amount_of_throwns == 2:
            strategy = input('\nWhat do you want to do? \n')
            evaluator.Evaluator.dices = self.yahtzee.dice_eyes
            evaluator.Evaluator.evaluate_strategy(self, strategy, player)
            print("")
            print(player.name, player.UPPER_SECTION)
            print(player.LOWER_SECTION)
            player.amount_of_throwns = 3
        elif roll.isdigit():
            self.yahtzee.roll_again(roll)
            player.amount_of_throwns +=1
        else:
            roll = input('Your input is not "stop" or numbers that you want to roll again, type stop or the dice you want to roll again to continue your turn. \n')
            self.loop(player, roll)

main = Main()
main.startGame()






