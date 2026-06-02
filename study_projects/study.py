import random

# ---------------------------------------------------------------
def questions_answers():
    questions = ("Is long hair gay?: ",
                "Is quadrober are retarded?:")
    options = (
        ("A. Yes", "B. Not"),
        ("A. Yes", "B. Not"),
    )

    answers = ("B", "A")

    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("--------------------------")
        print(question)
        for every_option in options[question_num]:
            print(every_option, end = " ")
        guess = input(str("\nEnter your answer (A or B): ")).upper()
        guesses.append(guess)

        if guess == answers[question_num]:
            score += 1
            print("Correct")
        else:
            print("Incorrect")
            print(f"{answers[question_num]} is the correct answer")

        question_num += 1
#---------------------------------------------------------------
# questions_answers()
# ---------------------------------------------------------------
def restorant_dictionary():
    menu = {
        "pasta": 12.99,
        "pizza": 10.49,
        "salad": 8.99,
        "salmon": 15.99,
        "chicken": 13.49
    }
    total = 0.0
    ordered_dishes = []
    print("Welcome to the restaurant!")
    print("Menu: ----------")
    for dish, price in menu.items():
        print(f"{dish}: ${price:.2f}")
    print("Menu: ----------")
    
    while True:
        order = input("Enter the dish you want to order (or 'exit' to finish): ").lower()
        if order == 'exit':
            break
        elif order in menu:
            print(f"You ordered {order} for ${menu[order]:.2f}")
            total += menu[order]
        else:
            print("Sorry, we don't have that dish on the menu.")
        ordered_dishes.append(order)
    print("--------------------------")
    print("You ordered: ", ", ".join(ordered_dishes))
    print(f"Your total is: ${total:.2f}")
    print("--------------------------")
#---------------------------------------------------------------
# restorant_dictionary()
#---------------------------------------------------------------


# dice game

def roll_dice_game():
    dice_art = {
        1: ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
        3: ("┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"),
        5: ("┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"), 
        6: ("┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘")
    }
    dice = []
    total = 0
    num_dice = int(input("How many dice do you want to roll?: "))
    for die in range(num_dice):
        dice.append(random.randint(1, 6))
        total += dice[die]

    # print the dice art in a multiple rows
    # for die in range(num_dice):
    #     for line in dice_art.get(dice[die]):
    #         print(line)
    
    # print the dice art in a single row
    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()
            
    print(f"You rolled a total of: {total}")   
#---------------------------------------------------------------
roll_dice_game()
#---------------------------------------------------------------

