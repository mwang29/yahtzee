import random as r


class dice():
    def __init__(self, num):
        self.values = []
        for i in range(num):
            self.values.append(r.randrange(1, 7))

    def roll(self, roll_id):
        for i in roll_id:
            self.values[i] = r.randrange(1, 7)
        return(self.values)
