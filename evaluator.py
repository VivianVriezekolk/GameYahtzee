import yahtzee

class Evaluator():
    def __init__(self):
        self.dices = yahtzee.Yatzee.numbers
        self.points = 0
        self.player

    def wrong_strategy(self):
        choice = input("Are you sure you want to do this? Your score would be zero, type 1 to choose another strategy and otherwise 0!")
        if int(choice) == 1:
            strategy = input("Type your new strategy")
            Evaluator.evaluate_strategy(self, strategy, self.player)
        else:
            self.points = 0

    def count_number(number, self):
        occurence = Evaluator.dices.count(number)
        print(str(occurence))
        if occurence == 0:
            Evaluator.wrong_strategy(self)
        else:
            self.points = occurence * number

    def count_kinds(number, self):
        for dice_eye in Evaluator.dices:
            if Evaluator.dices.count(dice_eye) <= number:
                self.points = sum(Evaluator.dices)
                return
        Evaluator.wrong_strategy(self)

    def check_full_house(self):
        twoValues = False
        threeValues = False
        for dice_eye in Evaluator.dices:
            if Evaluator.dices.count(dice_eye) == 2:
                twoValues = True
            if Evaluator.dices.count(dice_eye) == 3:
                threeValues = True
        if twoValues and threeValues:
            self.points = 25
        else:
            Evaluator.wrong_strategy(self)

    def check_street(number, self):
        if number <= len(set(Evaluator.dices)):
            if number == 4:
                print(set(sorted(Evaluator.dices)))
                if {1,2,3,4} == set(sorted(Evaluator.dices)) or {2,3,4,5} == set(sorted(Evaluator.dices)) or {3,4,5,6} == set(sorted(Evaluator.dices)):
                    self.points = 30
            else:
                print(set(sorted(Evaluator.dices)))
                if {1,2,3,4,5} == set(sorted(Evaluator.dices)) or {2,3,4,5,6} == set(sorted(Evaluator.dices)):
                    self.points = 40
        else:
            Evaluator.wrong_strategy(self)

    def check_yahtzee(self):
        if len(set(Evaluator.dices)) == 1:
            self.points = 50
        else:
            Evaluator.wrong_strategy(self)

    def evaluate_strategy(self, strategy, player):
        self.player = player
        for strategyA in self.player.UPPER_SECTION:
            print(strategyA)
        if strategy == "ones":
            Evaluator.count_number(1, self)
            player.UPPER_SECTION['ones'] = self.points
        elif strategy == "twos":
            Evaluator.count_number(2, self)
            player.UPPER_SECTION['twos'] = self.points
        elif strategy == "threes":
            Evaluator.count_number(3, self)
            player.UPPER_SECTION['threes'] = self.points
        elif strategy == "fours":
            Evaluator.count_number(4, self)
            player.UPPER_SECTION['fours'] = self.points
        elif strategy == "fives":
            Evaluator.count_number(5, self)
            player.UPPER_SECTION['fives'] = self.points
        elif strategy == "sixes":
            Evaluator.count_number(6, self)
            player.UPPER_SECTION['sixes'] = self.points
        elif strategy == "three_of_a_kind":
            Evaluator.count_kinds(3, self)
            player.LOWER_SECTION['three_of_a_kind'] = self.points
        elif strategy == "four_of_a_kind":
            Evaluator.count_kinds(4, self)
            player.LOWER_SECTION['four_of_a_kind'] = self.points
        elif strategy == "full_house":
            Evaluator.check_full_house(Evaluator)
            player.LOWER_SECTION['full_house'] = self.points
        elif strategy == "small_street":
            Evaluator.check_street(4, self)
            player.LOWER_SECTION['small_street'] = self.points
        elif strategy == "large_street":
            Evaluator.check_street(5, self)
            player.LOWER_SECTION['large_street'] = self.points
        elif strategy == "yahtzee":
            Evaluator.check_yahtzee(self)
            player.LOWER_SECTION['yahtzee'] = self.points
        elif strategy == "chance":
            player.LOWER_SECTION['chance'] = sum(Evaluator.dices)
        else:
            print("this is not a valid strategy choose from: \n")
            print(player.LOWER_SECTION.keys())
            print(player.UPPER_SECTION.keys())
            strategy = input("choose another strategy! \n")
            Evaluator.evaluate_strategy(self, strategy, player)








