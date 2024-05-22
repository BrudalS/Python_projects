import random

options = ["rock", "paper", "sessior"]

player_win_count = 0
computer_win_count = 0

while True:
    #  rock -> 0, paper -> 1, sessior -> 2
    player_pick = input("Rock/Paper/Sessior or q to quit ").lower()

    random_value = random.randint(0, 2)
    computer_pick = options[random_value]

    if player_pick in options:
        if player_pick == "q":
            print("Exiting the game ")
            break

        elif player_pick == "paper" and computer_pick == "sessior":
            computer_win_count += 1

        elif player_pick == "sessior" and computer_pick == "rock":
            computer_win_count += 1

        elif player_pick == "rock" and computer_pick == "paper":
            computer_win_count += 1

        elif player_pick == computer_pick:
            computer_win_count = computer_win_count

        else:
            player_win_count += 1

        print(f"The computer pick is {computer_pick}")

    else:
        print("Invalid input")

if player_win_count > computer_win_count:
    print("U win")

elif player_win_count == computer_win_count:
    print("Its a draw")

else:
    print("Computer wins")

print(f"Player count is {player_win_count} computer count is {computer_win_count} ")
