class Player():

    def __init__(self):
        self.name = ''
        self.amount_of_throwns = 0
        self.player_number = 0
        self.total_score = 0
        self.UPPER_SECTION = {
            'ones': None,
            'twos': None,
            'threes': None,
            'fours': None,
            'fives': None,
            'sixes': None,
        }
        self.LOWER_SECTION = {
            'three_of_a_kind' : None,
            'four_of_a_kind' : None,
            'full_house' : None,
            'small_street' : None,
            'large_street' : None,
            'yahtzee' : None,
            'chance' : None
        }

    def convertNoneScore(self):
        for key, value in self.UPPER_SECTION.items():
            if value == None:
                self.UPPER_SECTION[key] = 0
        for key, value in self.LOWER_SECTION.items():
            if value == None:
                self.LOWER_SECTION[key] = 0

    def determineScore(self):
        #self.convertNoneScore()
        score = sum(self.UPPER_SECTION.values())
        if score > 63:
            score = score + 50
        return score + sum(self.LOWER_SECTION.values())

    def fullCard(self):
        for value in self.UPPER_SECTION.values():
            if value == None:
                return False
        for value in self.LOWER_SECTION.values():
            if value == None:
                return False
        self.total_score = self.determineScore()
        return True
