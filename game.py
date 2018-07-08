from classes import dice

print("Welcome to Yahtzee!")
start = input('Press Enter to roll your first hand!')

player_1 = dice(5)  # initialize 5 dice
print(f"Your current hand: {player_1.values}")

s = input("Enter poisitions of dice you would like to re-roll. Ex: 1,2,3,\n")
roll_id = list(map(int, s.split(",")))

player_1.roll(roll_id)
print(f"Your current hand: {player_1.values}")
