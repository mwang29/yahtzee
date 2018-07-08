import random as r


class dice():
    def __init__(self, num):
        self.values = []
        for i in range(num):
            self.values.append(r.randrange(1, 7))

    def roll(self, roll_id=[]):
        for i in roll_id:
            self.values[i - 1] = r.randrange(1, 7)
        return(self.values)


class score():
    def __init__(self):
        self.ones = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.fives = 0
        self.sixes = 0
        self.three_of_a_kind = 0
        self.four_of_a_kind = 0
        self.full_house = 0
        self.small_straight = 0
        self.large_straight = 0
        self.chance = 0
        self.yahtzee = 0
        self.yahtzee_bonus = 0
        self.bonus = 0

    def ones(self, player):
        self.ones = player.count(1)

    def twos(self, player):
        self.twos = 2 * player.count(2)

    def threes(self, player):
        self.threes = 3 * player.count(3)

    def fours(self, player):
        self.fours = 4 * player.count(4)

    def fives(self, player):
        self.fives = 5 * player.count(5)

    def sixes(self, player):
        self.sixes = 5 * player.count(6)
