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

    def ones(self, hand):
        self.ones = hand.count(1)

    def twos(self, hand):
        self.twos = 2 * hand.count(2)

    def threes(self, hand):
        self.threes = 3 * hand.count(3)

    def fours(self, hand):
        self.fours = 4 * hand.count(4)

    def fives(self, hand):
        self.fives = 5 * hand.count(5)

    def sixes(self, hand):
        self.sixes = 5 * hand.count(6)

    def three_of_a_kind(self, hand):
        for i in range(1, 7):
            if hand.count(i) >= 3:
                self.three_of_a_kind = sum(hand)

    def four_of_a_kind(self, hand):
        for i in range(1, 7):
            if hand.count(i) >= 4:
                self.four_of_a_kind = sum(hand)

    def yahtzee(self, hand):
        for i in range(1, 7):
            if hand.count(i) == 5:
                self.yahtzee == 50

    def yahtzee_bonus(self, hand):
        for i in range(1, 7):
            if hand.count(i) == 5 and self.yahtzee == 50:
                self.yahtzee_bonus = 100

    def small_straight(self, hand):
        if counter(hand).keys() >= 4:
            self.small_straight = 30

    def large_straight(self, hand):
        if counter(hand).keys() == 5:
            self.large_straight = 40
