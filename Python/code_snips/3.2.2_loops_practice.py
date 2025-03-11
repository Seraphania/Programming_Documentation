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

number =1
while number <= 10:
    print(number)
    number += 1
###########################################
# print even numbers:
# modify the previous program to print only the even numbers from 1 to 10.
print("\ntask 1.2: modify the previous program to print only the even numbers from 1 to 10")
for numbers in range (1, 11):
    if numbers %2 == 0:
        print(numbers)

input("Press the anykey to continue...")

###########################################
# sum of numbers:
# write a program to calculate and print the sum of numbers from 1 to 10.
print("\ntask 1.3: write a program to calculate and print the sum of numbers from 1 to 10")
Total = 0
for num in range (1, 11):

    if num % 2 == 0:
        Total += num
print("the sum of the even numbers from 1-10 is: ", Total)

input("Press the anykey to continue...")

###########################################
##  Generate a list of 10 random integers between 1 and 100. 
##   Print the list, and then print the sum of all the even numbers in the list.

# Generate a list of 10 random integers from 1-100
counter = 0
numbers_list = []
import random

while counter < 10:
    number = random.randint(1,100)
    numbers_list.append(number)
    counter += 1

# Print the list nicely
print("Generated some random numbers: ", *numbers_list, sep = "\n")

# Sum all the even numbers in the list
#evens = []
#for num in numbers_list:
#    if num %2 == 0:
#        evens.append(num)
## better version:
even_sum = sum(num for num in numbers_list if num %2 ==0)

# Print the sum of those numbers
print ("The sum of the even numbers in this list is: ", even_sum)

input("Press the anykey to continue...")

###########################################
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

###########################################
## Calculate the sum of a list of numbers entered by the user

# Request input (and check it's an integer)
while True:
    try:
        numbers = input("Please enter some numbers seperated by spaces: ")
        break
    except ValueError:
        print("Please enter an integer: ")
        
numbers_list = [int(num) for num in numbers.split()]

sum_numbers = sum(numbers_list)
print("The sum of the numbers is: ", sum_numbers)

input("Press the anykey to continue...")

###########################################
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

###########################################
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

###########################################
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

###########################################
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

###########################################
# Palindrome Check:
# Write a program to check if a given string is a palindrome (reads the same backward as forward) using a loop.
print("\ntask 3.3: Write a program to check if a given string is a palindrome.")
String = input("Please enter a string, and i'll check if it's a palindrome: ")
if String[::-1] == String:
    print(f"your String '{String}' is a palindrome.")
else:
    print(f"'{String}' Is not a palindrome")

input("Press the anykey to continue...")

###########################################
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

###########################################
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

###########################################
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