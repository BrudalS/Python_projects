import random

MAX_BET = 100
MIN_BET = 10
ROWS = 3
COLUMS = 3
SYMBOLS = {
    "A":2,
    "B":3,
    "C":4,
    "D":5
}

def get_slot_machine_spin(rows, cols, symbol):
    all_symbol = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)

    coloums = []
    for _ in range(cols):
        coloum = []
        current_symbol = all_symbol[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            coloum.append(value)
        coloums.append(coloum)

    return coloums


def print_slot_machine(slots):
    for rows in range(len(slots[0])):
        for i, colum in enumerate(slots):
            if i != len(slots) - 1:
                print(colum[rows], end=" | ")
            else:
                print(colum[rows], end="")
        print()


def check_is_digit(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        if value.isdigit():
            value = int(value)
            if value > 0:
                return value
            else:
                print("The value is less than 0 ")
                return 0
        else:
            print("The entered value is not a number ")
            return 0

    return wrapper


@check_is_digit
def intake_value(value):
    return value


def main():
    balance = input("Enter the amount u wanna deposit $ ")
    balance = intake_value(balance)
    while True:
        while True:
            lines = input("Enter the number of lines u wanna select (1-3) ")
            lines = intake_value(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("Enter a number between 1-3 ")
        while True:
            get_bet = input(f"Enter the amount between ${MIN_BET} - ${MAX_BET} ")
            bet = intake_value(get_bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Enter a valid bet")
        total_bet = bet*lines
        if total_bet > balance:
            print("You dont have enough amount in ur balance")
            quit()
        print(f"You bet ${bet} on {lines} lines. Your total bet is {total_bet}")
        allow = input("Do u wanna print the slot machine (yes/no) ").lower()
        if allow == "yes":
            slots = get_slot_machine_spin(ROWS, COLUMS, SYMBOLS)
        else:
            break
        print_slot_machine(slots)

main()