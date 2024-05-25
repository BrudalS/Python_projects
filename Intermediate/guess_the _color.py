import random

COLORS = ["R", "G", "B", "Y", "M", "C"]
COLOR_COUNT = 4
number_of_turns = 10


def choose_colors(colors, count):
    colors = random.sample(colors, count)
    colors_selected = random.sample(colors, count)
    print("The Colors list is as follows ")
    for index in range(count):
        print(colors_selected[index])
    return colors


def get_input(colors):
    user_coulors = input("Enter the color formate ").upper().split(" ")
    print(user_coulors)
    if len(user_coulors) == COLOR_COUNT:
        for index in range(COLOR_COUNT):
            if user_coulors[index] in colors:
                pass
            else:
                print("Enter the vaild colors refering to the above data ")
    else:
        print(f"Enter the vaild number of colors i.e is {COLOR_COUNT}")
    return user_coulors


def test_input(generated_colors, user_color):
    correct_cont = 0
    incorrect_count = 0
    for index in range(COLOR_COUNT):
        if generated_colors[index] == user_color[index]:
            correct_cont += 1
        else:
            incorrect_count += 1
    return correct_cont, incorrect_count


generated_colors = choose_colors(COLORS, COLOR_COUNT)

for turns in range(number_of_turns):
    user_input = get_input(generated_colors)
    correct, incorrect = test_input(generated_colors, user_input)
    if correct != COLOR_COUNT:
        print(f"Your guess has {correct} correct colors in place and {incorrect} incorrect colors in place ")
    else:
        print("U chose the accurate placing of colors thats make u a winner")
        break
    print(f"The number of turns left {9 - turns}")

print(f"The computer generated color were {generated_colors}")