##  The two tenets of coding are:
##  1: "Esoteric languages are a joke thing. No one should ever use them"
##  2: "Solving code challenges using excel spreadsheets counts as an esoteric language"
##--------------------------------------------------------------------------------------
#   What is this thing? - Task 1: Understanding Modules
#   1:  Learn about what modules are in Python and how they help organize code.
#   2:  Familiarize yourself with some built-in modules like math and random.
#   2:  Write a simple script that imports the math module and uses its functions (e.g., sqrt, pow) to perform basic mathematical operations.
import math
import random as rd

modifier = rd.randrange(1, 101) 
number = int(input("Please enter a number: "))
print(f"The sqare of the number is {number ** modifier:.2f}.")
print(f"The sqare root of the number is {math.sqrt(number):.2f}.")
print(f"{number} x {modifier} = {number * modifier:.2f}")