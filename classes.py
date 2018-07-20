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
    def __init__(self):
        self.ones = None
        self.twos = None
        self.threes = None
        self.fours = None
        self.fives = None
        self.sixes = None
        self.three_of_a_kind = None
        self.four_of_a_kind = None
        self.full_house = None
        self.small_straight = None
        self.large_straight = None
        self.chance = None
        self.yahtzee = None
        self.yahtzee_bonus = None
        self.bonus = None
        self.total = None

    def ones(self, hand):
        if self.ones == None:
            self.ones = hand.count(1)
            self.total += self.ones
        else:
            return("Already scored!")

    def twos(self, hand):
        if self.twos == None:
            self.twos = 2 * hand.count(2)
            self.total += self.twos
        else:
            return("Already scored!")

    def threes(self, hand):
        if self.threes == None:
            self.threes = 3 * hand.count(3)
            self.total += self.threes
        else:
            return("Already scored!")

    def fours(self, hand):
        if self.fours == None:
            self.fours = 4 * hand.count(4)
            self.total += self.fours
        else:
            return("Already scored!")

    def fives(self, hand):
        if self.fives == None:
            self.fives = 5 * hand.count(5)
            self.total += self.fives
        else:
            return("Already scored!")

    def sixes(self, hand):
        if self.sixes == None:
            self.sixes = 5 * hand.count(6)
            self.total += self.sixes
        else:
            return("Already scored!")

    def three_of_a_kind(self, hand):
        if self.three_of_a_kind == None:
            if counter(hand).values() >= 4:
                self.three_of_a_kind = sum(hand)
            else:
                self.three_of_a_kind = 0
            self.total += self.three_of_a_kind
        else:
            return("Already scored!")

    def four_of_a_kind(self, hand):
        if self.four_of_a_kind == None:
            if counter(hand).values() >= 4:
                self.four_of_a_kind = sum(hand)
            else:
                self.four_of_a_kind = 0
            self.total += self.four_of_a_kind
        else:
            return("Already scored!")

    def yahtzee(self, hand):
        if self.yahtzee == None:
            if counter(hand).values() == 5:
                self.yahtzee == 50
            else:
                self.yahtzee == 0
            self.total += self.yahtzee
        else:
            return("Already scored!")

    def yahtzee_bonus(self, hand):
        if counter(hand).values() == 5 and self.yahtzee == 50:
            self.yahtzee_bonus += 100
            self.total += 100
        else:
            return("Error! You cannot score Yahtzee Bonus!")

    def small_straight(self, hand):
        if self.small_straight == None:
            if counter(hand).keys() >= 4:
                self.small_straight = 30
            else:
                self.small_straight = 0
            self.total += self.small_straight
        else:
            return("Already scored!")

    def large_straight(self, hand):
        if self.large_straight == None:
            if counter(hand).keys() == 5:
                self.large_straight = 40
            else:
                self.large_straight = 0
            self.total += self.large_straight
        else:
            return("Already scored!")
