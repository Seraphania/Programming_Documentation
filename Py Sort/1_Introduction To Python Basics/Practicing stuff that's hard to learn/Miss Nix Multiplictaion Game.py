# Miss Nix's Multiplication Game:
# This Game will present a player with a selected times table and then test them on it.
import random
# Generate the times table for memorisation
def Matrix(Table):
    rows = [f"{x} x {y} = {x*y}" for x in range(1, Table + 1) for y in range(1, 13)]
    print("here is the", Table, "times table: ")
    for line in rows[-12:]:
        print(line)
    input("Press the enter When you're ready to be tested...")
    for i in range(1, 1000):
        print("\n")
        
# Validate user guess input
def GetPositiveInteger(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print("Please enter a positive number for your answer.")
        except ValueError:
            print("Please enter a valid number: ")

# Validate user continue input
def Continue(ask):
    while ask not in ("y", "n"):
        ask = input("Invalid input. To continue please enter 'y' to exit please enter 'n' ")
    if ask == "y":
        return ask
    else:
        print("kthnxbye :)")
        exit()

# Test whether the guess is correct
def CheckCorrect(Guess, CorrectNum):        
    if Guess == CorrectNum:
        print("Correct!")
        return True
    else:
        print("Sorry, That's not right, would you like to try again? ")
        return False
        
# Main Game loop
Start = input("Welcome to Miss Nix's Multiplication Game! \nYou choose a times table to memorise, then you will be tested on it. \nAre you ready to play? (y/n) ")
Continue(Start)
while True:
    if Start == "y":
        Table = GetPositiveInteger("Which times table would you like to look at? (please enter a number): ")
        Matrix(Table)
        Random = random.randint(1, 12)
        CorrectNum = Random * Table
        Count = 0
        while Count < 5:
            Random = random.randint(1, 12)
            CorrectNum = Random * Table
            Guess = GetPositiveInteger(f"What is {Table} X {Random}?: ")
            if CheckCorrect(Guess, CorrectNum):
                Count += 1
        Restart = input("Nice, 5 correct answers! Would you like to play again? ")
        Start = Continue(Restart)
    else:
        print("kthnxbye :)")
        exit()