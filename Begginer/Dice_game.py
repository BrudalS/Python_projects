import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

def players_entery():
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            players = players
        else:
            print("The number of players must be between 2 and 4")
            return None

    else:
        print("Invalid syntax")
        return None

    return players

def players_list(players):
    players = [0 for _ in range(len(players))]
    return players


