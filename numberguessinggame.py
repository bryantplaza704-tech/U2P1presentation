from random import randint

def roll_dice():
    print("Welcome to the Dice Roller!")
    try:
        rolls = int(input("How many rolls? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # step 1: make the list to track counts
    roll_list = [0, 0, 0, 0, 0, 0]

    # step 2: roll and update the list
    for _ in range(rolls):
        result = randint(1, 6)
        print("You rolled a", result)
        roll_list[result - 1] += 1   # subtract 1 so number 1 goes to index 0

    # step 3: show stats
    display_stats(roll_list, rolls)


def display_stats(roll_list, total_rolls):
    print("\nResults:")
    for i in range(6):  # loop over numbers 1–6
        count = roll_list[i]
        percent = (count / total_rolls) * 100
        print(f"{i+1}: {count} times ({percent:.2f}%)")


roll_dice()
