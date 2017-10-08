class ConsoleView():

    def __init__(self, model):
        self.yahtzee = model


    def welcome_message(self):
        print("Welcome to yahtzee!")

    def ask_amount_players(self):
        print("With how many players do you want to play?")
        amount_of_players = input()
        return amount_of_players