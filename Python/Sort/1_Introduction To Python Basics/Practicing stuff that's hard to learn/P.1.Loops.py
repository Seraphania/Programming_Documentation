#  the two tenets of coding are:
#  1: "esoteric languages are a joke thing. no one should ever use them"
#  2: "solving code challenges using excel spreadsheets counts as an esoteric language"
#--------------------------------------------------------------------------------------
# level 1: basics
# print numbers:
# use a for loop to print numbers from 1 to 10.
print("task 1.1: # print numbers: \nuse a for loop to print numbers from 1 to 10.")
for numbers in range (1, 11):
    print(numbers)

input("Press the anykey to continue...")
# print even numbers:
# modify the previous program to print only the even numbers from 1 to 10.
print("\ntask 1.2: modify the previous program to print only the even numbers from 1 to 10")
for numbers in range (1, 11):
    if numbers %2 == 0:
        print(numbers)

input("Press the anykey to continue...")
# sum of numbers:
# write a program to calculate and print the sum of numbers from 1 to 10.
print("\ntask 1.3: write a program to calculate and print the sum of numbers from 1 to 10")
Total = 0
for num in range (1, 11):

    if num % 2 == 0:
        Total += num
print("the sum of the even numbers from 1-10 is: ", Total)

        
input("Press the anykey to continue...")
# level 2: intermediate
# factorial calculation:
# write a program to calculate the factorial of a given number using a for loop.
def getpositiveinteger(prompt):
    while True:
        try:
           num = int(input(prompt))
           if num > 0:
                return num
        except ValueError:
            print("please enter a positive number")
print("\ntask 2.1: write a program to calculate the factorial of a given number using a for loop.")
import math
inputnum = getpositiveinteger("please enter a number greater than 0: ")
numbers = [num for num in range(1, inputnum + 1)]
factorial = math.prod(numbers)
print(f"the factorial of {inputnum} is {factorial}")

input("Press the anykey to continue...")
# multiplication table:
# print the multiplication table (up to 12) for a given number using a nested for loop.
def getpositiveinteger(prompt):
    while True:
        try:
           num = int(input(prompt))
           if num > 0:
                return num
           break
        except ValueError:
            print("please enter a positive number")

print("\ntask 2.2: print the multiplication table (up to 12) for a given number using a nested for loop.")
inputnum = getpositiveinteger("please enter a number greater than 0: ")
rows = [f"{x} x {y} = {x*y}" for x in range(1, inputnum + 1) for y in range(1, 13)]
print("here is the ", inputnum, " times table: ")
for line in rows[-12:]:
    print(line)

input("Press the anykey to continue...")
# count characters:
# take a user input string and use a for loop to count the number of characters in it.
print("\ntask 2.3: take a user input string and use a for loop to count the number of characters in it.")
string = input("please enter some text: ")
length = 0
for i in string:
    length += 1
print("the length of the string you entered is: ", (length))
print("but also... just len(string)) = ", len(string))


input("Press the anykey to continue...")
# level 3: advanced
# prime numbers:
# write a program to check if a given number is prime or not. use a for loop to iterate through potential divisors.
def getpositiveinteger(prompt):
    while True:
        try:
           num = int(input(prompt))
           if num > 0:
                return num
           break # not needed why?
        except ValueError:
            print("please enter a positive number")
            
print("\ntask 3.1: write a program to check if a given number is prime or not.")
inputnum = getpositiveinteger("please enter a number greater than 0: ")
# 1 is never prime
if inputnum == 1:
    print((inputnum), " is not a prime number")
# check the rest
counter = 0
for i in range(1, inputnum): 
     if (inputnum % i == 0):
        counter += 1      
if counter >= 2:
     print((inputnum), " is not a prime number")
else:
    print((inputnum), " is a prime number")    

input("Press the anykey to continue...")
# fibonacci sequence:
# print the first 10 numbers in the fibonacci sequence using a for loop.
def getpositiveinteger(prompt):
    while True:
        try:
           num = int(input(prompt))
           if num > 0:
                return num
           break
        except ValueError:
            print("please enter a positive number")
            
print("\ntask 3.2: Print the numbers in the fibonacci sequence using a for loop.")
count = getpositiveinteger("How much of the sequence woudl you like to see? (please enter a number greater than 0): ")
fibseq = [0, 1]
for i in range(1, count-1):
    add = (fibseq[-1]+fibseq[-2])
    fibseq.append(add)
for row in fibseq:
    print(row)

input("Press the anykey to continue...")
# Palindrome Check:
# Write a program to check if a given string is a palindrome (reads the same backward as forward) using a loop.
print("\ntask 3.3: Write a program to check if a given string is a palindrome.")
String = input("Please enter a string, and i'll check if it's a palindrome: ")
if String[::-1] == String:
    print(f"your String '{String}' is a palindrome.")
else:
    print(f"'{String}' Is not a palindrome")

input("Press the anykey to continue...")
# Level 4: Expert
# FizzBuzz:
# Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, 
# and for the multiples of five, print "Buzz." For numbers that are multiples of both three and five, print "FizzBuzz."
print("\ntask 4.1: FizzBuzz.")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
input("Press the anykey to continue...")     
# pascal's triangle:
# generate and print the first x rows of pascal's triangle using nested loops.
def get_positive_integer(prompt):
    while True:
        try:
           num = int(input(prompt))
           if num > 0:
                return num
        except ValueError:
            print("please enter a positive number")
print("\ntask 4.2: Generate and print the first x rows of pascal's triangle using nested loops")            
rows = get_positive_integer("How many rows do you want?: ")    
triangle = ["1"]
counter = 0
while counter < rows:
    current_row = triangle[-1]
    new_row = [1]
    for i in range(len(current_row) -1):
        ele = current_row[i] + current_row[i+1]
        new_row.append(ele)
        
    new_row.append(1)
    triangle.append(new_row)
    counter += 1 
# Stole this a bit really.    
last_row = triangle[-1]
number_width = len(str(max(last_row))) + 1
triangle_width = number_width * len(last_row)

for row in triangle:
    string = ""

    for number in row:
        number_string = str(number)
        string += number_string + ' ' * (number_width - len(number_string))

    print(string.center(triangle_width))

input("Press the anykey to continue...")
# Guess the Number Game:
# Create a simple number guessing game. Generate a random number between 1 and 100, and let the user guess the number. 
# Provide hints like "Too high" or "Too low" until the correct number is guessed.
print("\ntask 4.3: Create a simple number guessing game (Guess Numbers Between 1-100).")
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

input("Press the anykey to continue...")
# Bonus: Miss Nix's Multiplication Game:
# This Game will present a player with a selected times table and then test them on it.
print("\ntask Bonus! Miss Nix's Multiplication Game")
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