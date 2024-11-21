# Guess the Number Game:
# Create a simple number guessing game. Generate a random number between 1 and 100, and let the user guess the number. 
# Provide hints like "Too high" or "Too low" until the correct number is guessed.
import random

# Random number generator
def GetRandom():
   return random.randint(1, 100)

# Validate user guess input
def GetPositiveInteger(prompt):
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
def Continue(ask):
    while ask not in ("y", "n"):
        ask = input("Invalid inpuut. To contiinue please enter 'y' to exit please enter 'n' ")
    return ask

# Evaluate guess 
def CheckCorrect(Guess, CorrectNum):        
    if Guess == CorrectNum:
        print("Woo! Gratz you guessed it!!")
        return True
    elif Guess < CorrectNum:
        print("Nope, too low, guess again: ")
        return False
    else:
        print("Nope, too high, guess again: ")
        return False
        
# Main Game loop
Start = input("This is a game where I think of a number between 1 and 100 and you have to guess what it is. \nDo you want to have a guess? (y/n) ")
Continue(Start)
while True:
    if Start == "y":
        CorrectNum = GetRandom()
        while True:
            Guess = GetPositiveInteger("Please take a guess: ")
            if CheckCorrect(Guess, CorrectNum):
                Start = Continue("Would you like to play again? (y/n)")
                break
    else:
        print("kthnxbye :)")
        exit()
