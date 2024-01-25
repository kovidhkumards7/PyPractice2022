import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count-1):
            all_symbols.append(symbol)

        columns = []
        for _ in range(cols):
            column = []
            current_symbols = all_symbols[:]
            for _ in range(rows):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)
            column.append(column)
        return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        print()

def deposit():
    while True:
        amount = input("How much amount would you like to input?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The entered amount must be > 0")
        else:
            print("enter a number")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines >= 1:
                break
            else:
                print("The entered no of lines must be within range")
        else:
            print("enter a number")
    return lines


def get_bet():
    while True:
        amount = input("How much amount would you like to bet on each line?")
        if amount.isdigit():
            amount = int(amount)
            if MAX_BET >= amount >= MIN_BET:
                break
            else:
                print("The entered amount must be btw " + str(MIN_BET) + " and " + str(MAX_BET))
        else:
            print("enter a number")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"u don't have enough to bet that amt, ur present balance is {balance}")
        else:
            break
    print(f"u r betting ${bet} on {lines} lines.Total bet is equal to: ${total_bet}")
    print(balance, lines)

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()
