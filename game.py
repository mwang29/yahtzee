from classes import player, dice, score
import time
import sys
from scoring import recommend

print("\n\nWelcome to Yahtzee!\n\n")
player_num = int(input('How many players?\n'))
players = []
wait = "................................."
# empty list of players

for n in range(player_num):
    if n == 0:
        new_name = input("Please enter a name: ")
    else:
        new_name = input("Please enter another name: ")
    players.append(player(new_name))
    players[n].score = score()

for n in range(player_num):
    print(f"\nPlayer {n+1} start!\n")
    players[n].hand = dice(5)
    start = input('Press Enter to roll your first hand!')

    print(f"Your roll is.. \n\n")
    print(players[n].hand.values)

    for i in range(2):
        s = input(
            "\n\nEnter positions of dice you would like to re-roll. (Ex: 1,2,3) If none, type 'none'\n\n").lower()
        if s != "none":
            roll_id = list(map(int, s.split(",")))
            players[n].hand.roll(roll_id)
            print(f"\nYour current hand: {players[n].hand.values}")
        else:
            print(f"\nYour current hand: {players[n].hand.values}")

    rec = recommend(players[n].hand.values)
    print(f"Recommended plays: {rec}")
