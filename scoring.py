from collections import Counter


def recommend(hand):
    n2w = {1: 'Ones', 2: 'Twos', 3: 'Threes', 4: 'Fours', 5: 'Fives', 6: 'Sixes'}
    # Individual numbers
    numbers = Counter(hand).keys()
    freq = Counter(hand).values()
    rec = []

    if max(freq) >= 3:
        rec.append("Three of a kind")
    if max(freq) >= 4:
        rec.append("Four of a kind")
    if max(freq) == 5:
        rec.append("Yahtzee")
    if len(numbers) >= 4:
        rec.append("Small straight")
    if len(numbers) == 5:
        rec.append("Large straight")
    if all(x in freq for x in [2, 3]):
        rec.append("Full house")
    for n in numbers:
        rec.append(n2w[n])
    rec.append("Chance")
    return(rec)
