import random as r
from collections import Counter


class player():
    def __init__(self, n=0):
        self.score = None
        self.hand = None
        self.name = n


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
    def __init__(self, name):
        self.one = None
        self.two = None
        self.three = None
        self.four = None
        self.five = None
        self.six = None
        self.toak = None
        self.foak = None
        self.fh = None
        self.ss = None
        self.ls = None
        self.c = None
        self.y = None
        self.yb = None
        self.b = None
        self.total = 0
        self.name = name

    def ones(self, hand):
        if self.one is None:
            self.one = hand.count(1)
            self.total += self.one
        else:
            return("Already scored!")

    def twos(self, hand):
        if self.two is None:
            self.two = 2 * hand.count(2)
            self.total += self.two
        else:
            return("Already scored!")

    def threes(self, hand):
        if self.three is None:
            self.three = 3 * hand.count(3)
            self.total += self.three
        else:
            return("Already scored!")

    def fours(self, hand):
        if self.four is None:
            self.four = 4 * hand.count(4)
            self.total += self.four
        else:
            return("Already scored!")

    def fives(self, hand):
        if self.five is None:
            self.five = 5 * hand.count(5)
            self.total += self.five
        else:
            return("Already scored!")

    def sixes(self, hand):
        if self.six is None:
            self.six = 5 * hand.count(6)
            self.total += self.six
        else:
            return("Already scored!")

    def three_of_a_kind(self, hand):
        if self.toak is None:
            if Counter(hand).values() >= 4:
                self.toak = sum(hand)
            else:
                self.toak = 0
            self.total += self.toak
        else:
            return("Already scored!")

    def four_of_a_kind(self, hand):
        if self.foak is None:
            if Counter(hand).values() >= 4:
                self.foak = sum(hand)
            else:
                self.foak = 0
            self.total += self.foak
        else:
            return("Already scored!")

    def yahtzee(self, hand):
        if self.y is None:
            if Counter(hand).values() == 5:
                self.y == 50
            else:
                self.y == 0
            self.total += self.y
        else:
            return("Already scored!")

    def yahtzee_bonus(self, hand):
        if Counter(hand).values() == 5 and self.y == 50:
            self.yb += 100
            self.total += 100
        else:
            return("Error! You cannot score Yahtzee Bonus!")

    def small_straight(self, hand):
        if self.ss is None:
            if len(Counter(hand).keys()) >= 4:
                self.ss = 30
            else:
                self.ss = 0
            self.total += self.ss
        else:
            return("Already scored!")

    def large_straight(self, hand):
        if self.ls is None:
            if len(Counter(hand).keys()) == 5:
                self.ls = 40
            else:
                self.ls = 0
            self.total += self.ls
        else:
            return("Already scored!")

    def full_house(self, hand):
        if self.fh is None:
            if all(x in Counter(hand).values() for x in [2, 3]):
                self.fh = 25
            else:
                self.fh = 0
        else:
            return("Already scored!")

    def chance(self, hand):
        if self.c is None:
            self.c = sum(hand)
        else:
            return("Already scored!")

    def total_score(self):
        print(f"Current score is {self.total}")
