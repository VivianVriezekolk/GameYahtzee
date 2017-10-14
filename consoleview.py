class ConsoleView():

    def __init__(self, model):
        self.yahtzee = model

    def welcome_message(self):
        print("Welcome to yahtzee!")

    def ask_amount_players(self):
        print("With how many players do you want to play?")
        amount_of_players = input()
        return amount_of_players

    def ask_name_of_players(self):
        names = []
        for player in self.yahtzee.players:
            names.append(input("What is the name of the player " + str(player.player_number + 1) + "? \n"))
        return names

    def printScores(self):
        print(self.yahtzee.dice_eyes)

    def print_winner_of_game(self):
        print(self.yahtzee.winner + " heeft gewonnen met " + self.yahtzee.winner.total_score + " punten!")
