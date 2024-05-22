import random

while True:
    number_of_players = input("Enter the number of players (2-4) ")
    if number_of_players.isdigit():
        number_of_players = int(number_of_players)
        if number_of_players < 1 or number_of_players > 5:
            print("Enter the player range between (2-4) ")
        else:
            break
    else:
        print("Invalid input, Enter a numerical value")

player_list = [0 for _ in range(number_of_players)]

for i in range(len(player_list)):
    score = 0
    print(f"Player {i + 1} turn has been started!!!")
    while True:
        choice = input(f"do u wanna roll the dice (y) or press q to stop").lower()
        if choice == "q":
            player_list[i] = score
            break
        elif choice == "y":
            random_roll = random.randint(1, 6)
            print(f"You rolled: {random_roll}")
            if random_roll != 1:
                score += random_roll
                print("Current score: ", score)
                if score >= 50:
                    print(f"U won player {i+1}")
                    break
            else:
                score = 0
                break
        else:
            print("Invalid Input")

for i in range(len(player_list)):
    print(f"Total Score of player {i+1} is {player_list[i]} ")

max_score = max(player_list)
player_won_index = player_list.index(max_score)
print(f"The winner of the game is player {player_won_index+1}")
