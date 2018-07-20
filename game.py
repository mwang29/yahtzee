from classes import player, dice, score
import time
import sys
from scoring import recommend

print("\n\nWelcome to Yahtzee!\n\n")
player_num = int(input('How many players?\n'))
players = []
scores = []
hands = []
wait = "................................."
# empty list of players

for n in range(player_num):
    if n == 0:
        new_name = input("Please enter a name: ")
    else:
        new_name = input("Please enter another name: ")
    players.append(player(new_name))
    scores.append(score(new_name))

for n in range(player_num):
    print(f"\nPlayer {n+1} start!\n")
    hands.append(dice(5))
    start = input('Press Enter to roll your first hand!')

    print(f"Your roll is.. \n\n")
    print(hands[n].values)

    for i in range(2):
        s = input(
            "\n\nEnter positions of dice you would like to re-roll. (Ex: 1,2,3) If none, type 'none'\n\n").lower()
        if s != "none":
            roll_id = list(map(int, s.split(",")))
            hands[n].roll(roll_id)
            print(f"\nYour current hand: {hands[n].values}")
        else:
            print(f"\nYour current hand: {hands[n].values}")

    rec = recommend(hands[n].values)
    print(f"Recommended categories: {rec}")

    cat = input("Please enter which category you would like to score:")
    getattr(scores[n], cat)(hands[n].values)
    # Converts input category to method
    # players[n].score.func(players[n].hand.values)
    scores[n].total_score()
