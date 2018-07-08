from classes import dice

print("\n\nWelcome to Yahtzee!\n\n")
start = input('Press Enter to roll your first hand!')

player_1 = dice(5)  # initialize 5 dice
print(f"\n\nYour current hand: {player_1.values}")

# Roll 2
s = input("\n\nEnter poisitions of dice you would like to re-roll. Ex: 1,2,3\nIf none, type 'none'\n").lower()
if s != "none":
    roll_id = list(map(int, s.split(",")))
    player_1.roll(roll_id)
    print(f"\nYour current hand: {player_1.values}")
else:
    print(f"\nYour current hand: {player_1.values}")

# Roll 3
s = input("\n\nEnter poisitions of dice you would like to re-roll. Ex: 1,2,3\nIf none, type 'none'\n").lower()
if s != "none":
    roll_id = list(map(int, s.split(",")))
    player_1.roll(roll_id)
    print(f"\nYour current hand: {player_1.values}")
else:
    print(f"\nYour current hand: {player_1.values}")
