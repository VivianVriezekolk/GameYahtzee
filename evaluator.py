import yahtzee

class Evaluator():
    def __init__(self):
        self.dices = yahtzee.Yatzee.numbers
        self.points = 0
        self.player

    def wrong_strategy(self):
        choice = input("Are you sure you want to do this? Your score would be zero, type 1 to choose another strategy and otherwise 0!")
        if int(choice) == 1:
            newStrategy = input("Type your new strategy \n")
            Evaluator.evaluate_strategy(self, newStrategy, self.player)
            return True
        else:
            self.points = 0
            return False

    def count_number(number, self):
        occurence = Evaluator.dices.count(number)
        if occurence == 0:
            return not Evaluator.wrong_strategy(self)
        else:
            self.points = occurence * number
            return True

    def count_kinds(number, self):
        for dice_eye in Evaluator.dices:
            if Evaluator.dices.count(dice_eye) <= number:
                self.points = sum(Evaluator.dices)
                return True
        return not Evaluator.wrong_strategy(self)

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
            return True
        else:
            return not Evaluator.wrong_strategy(self)

    def check_street(number, self):
        if number <= len(set(Evaluator.dices)):
            if number == 4:
                if {1,2,3,4} == set(sorted(Evaluator.dices)) or {2,3,4,5} == set(sorted(Evaluator.dices)) or {3,4,5,6} == set(sorted(Evaluator.dices)):
                    self.points = 30
                    return True
                else:
                    return not Evaluator.wrong_strategy(self)
            else:
                if {1,2,3,4,5} == set(sorted(Evaluator.dices)) or {2,3,4,5,6} == set(sorted(Evaluator.dices)):
                    self.points = 40
                    return True
        else:
            return not Evaluator.wrong_strategy(self)

    def check_yahtzee(self):
        if len(set(Evaluator.dices)) == 1:
            self.points = 50
            return True
        else:
            return not Evaluator.wrong_strategy(self)

    def is_strategy_filled(self, strategy):
        for strategyA in self.player.UPPER_SECTION:
            if strategyA == strategy:
                if self.player.UPPER_SECTION[str(strategy)] == None:
                    return False
        for strategyB in self.player.LOWER_SECTION:
            if strategyB == strategy:
                if self.player.LOWER_SECTION[str(strategy)] == None:
                    return False
        return True

    def valid_strategy(self, strategy):
        for strategyA in self.player.LOWER_SECTION:
            if strategyA == strategy:
              return True
        for strategyB in self.player.UPPER_SECTION:
            if strategyB == strategy:
                return True
        return False

    def evaluate_strategy(self, strategy, player):
        self.player = player
        if Evaluator.valid_strategy(self, strategy) == False:
            print("this is not a valid strategy, choose from: \n")
            print(player.LOWER_SECTION.keys())
            print(player.UPPER_SECTION.keys())
            strategy = input("choose another strategy! \n")
            Evaluator.evaluate_strategy(self, strategy, player)
        elif Evaluator.is_strategy_filled(self, strategy) == True:
            print("You already used this strategy, choose a new strategy: \n")
            print(player.LOWER_SECTION.keys())
            print(player.UPPER_SECTION.keys())
            strategy = input("choose another strategy! \n")
            Evaluator.evaluate_strategy(self, strategy, player)
        else:
            if (strategy == "ones") and Evaluator.count_number(1, self):
                player.UPPER_SECTION['ones'] = self.points
            elif (strategy == "twos") and Evaluator.count_number(2, self):
                player.UPPER_SECTION['twos'] = self.points
            elif (strategy == "threes") and Evaluator.count_number(3, self):
                player.UPPER_SECTION['threes'] = self.points
            elif (strategy == "fours") and Evaluator.count_number(4, self):
                player.UPPER_SECTION['fours'] = self.points
            elif (strategy == "fives") and Evaluator.count_number(5, self):
                player.UPPER_SECTION['fives'] = self.points
            elif (strategy == "sixes") and Evaluator.count_number(6, self):
                player.UPPER_SECTION['sixes'] = self.points
            elif (strategy == "three_of_a_kind") and Evaluator.count_kinds(3, self):
                player.LOWER_SECTION['three_of_a_kind'] = self.points
            elif strategy == "four_of_a_kind" and Evaluator.count_kinds(4, self):
                player.LOWER_SECTION['four_of_a_kind'] = self.points
            elif strategy == "full_house" and Evaluator.check_full_house(Evaluator):
                player.LOWER_SECTION['full_house'] = self.points
            elif strategy == "small_street" and Evaluator.check_street(4, self):
                player.LOWER_SECTION['small_street'] = self.points
            elif strategy == "large_street" and Evaluator.check_street(5, self):
                player.LOWER_SECTION['large_street'] = self.points
            elif strategy == "yahtzee" and Evaluator.check_yahtzee(self):
                player.LOWER_SECTION['yahtzee'] = self.points
            elif strategy == "chance":
                player.LOWER_SECTION['chance'] = sum(Evaluator.dices)




