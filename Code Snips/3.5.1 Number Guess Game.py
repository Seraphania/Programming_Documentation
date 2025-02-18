# Guess the Number Game:
# Create a simple number guessing game. Generate a random number between 1 and 100, and let the user guess the number. 
# Provide hints like "Too high" or "Too low" until the correct number is guessed.
import random

# Random number generator
def get_random():
   return random.randint(1, 100)

# Validate user guess input
def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0 and num <= 100:
                return num
            else:
                print("Please enter a positive number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number: ")

# Validate user continue input
def continue_game(ask):
    while ask not in ("y", "n"):
        ask = input("Invalid inpuut. To contiinue please enter 'y' to exit please enter 'n' ")
    return ask

# Evaluate guess 
def check_correct(guess, correct_num):        
    if guess == correct_num:
        print("Woo! Gratz you guessed it!!")
        return True
    elif guess < correct_num:
        print("Nope, too low, guess again: ")
        return False
    else:
        print("Nope, too high, guess again: ")
        return False
        
# Main Game loop
start = input("This is a game where I think of a number between 1 and 100 and you have to guess what it is. \nDo you want to have a guess? (y/n) ")
continue_game(start)
while True:
    if start == "y":
        correct_num = get_random()
        while True:
            guess = get_positive_integer("Please take a guess: ")
            if check_correct(guess, correct_num):
                start = continue_game("Would you like to play again? (y/n)")
                break
    else:
        print("kthnxbye :)")
        exit()