##  The two tenets of coding are:
##  1: "Esoteric languages are a joke thing. No one should ever use them"
##  2: "Solving code challenges using excel spreadsheets counts as an esoteric language"
##--------------------------------------------------------------------------------------
#   What is this thing? - Task 1: Define and Call a Function
#   1:  Define a function named greet_user that prints "Hello, user!" when called. 
#   2:  Call the function to see the output.
def greet_user(user):
    print(f"Hello {user}! ")

greet_user(input("Please enter your name: "))

#   What is this thing? - Task 2: Function Parameters and Return Values
#   1:  Modify your greet_user function to take a parameter user_name.
#   2:  Instead of getting the user's name using input() within the function, pass the name as an argument when calling the function.
#   3:  Have the function return a greeting message rather than printing it directly.
#   4:  Call the function, passing a name as an argument and store the returned message in a variable.
#   5:  Print the variable containing the greeting message.
def greet_user(user_name):
    greeting = (f"hello {user_name}!")
    return greeting

# name = "John"
# greet = greet_user(name)
# print(greet)

#   What is this thing? - Task 3: Functions with Multiple Parameters
#   1:  Modify your greet_user function to take two parameters: user_name and age.
#   2:  Update the greeting message to include the user's age.
#   3:  Call the function with different values for both parameters.
#   4:  Print the returned greeting message.
def greet_user(user_name, age):
    greeting = (f"hello {user_name}! You are {age} years old.")
    return greeting

name = "John"
age = 25
greet = greet_user(name, age)
print(greet)

#   What is this thing? - Task 4: Default Parameters and Keyword Arguments
#   1:  Modify the greet_user function to have a default value for the age parameter (e.g., set it to 18 by default).
#   2:  Call the function without providing an age (let it use the default), and then call it again with a specific age.
#   3:  Print both returned greeting messages.
def greet_user(user_name, age= 18):
    greeting = (f"hello {user_name}! You are {age} years old.")
    return greeting

name = "John"
age = 25
greet = greet_user(name)
print(greet)
greet = greet_user(name, age)
print(greet)

#   What is this thing? - Task 5: Creating Your Own Function
#   1:  Define a new function named calculate_area_of_rectangle that takes two parameters: length and width.
#   2:  Inside the function, calculate and return the area of the rectangle using the formula area = length * width.
#   3:  Call the function with different values for length and width.
#   4:  Print the returned area.
def area_of_rectangle(length, width):
    area = int(length) * int(width)
    return area

print("This will calculate the area of a rectangle.")
length = input("What is the length of the rectangle in metres? ")
width = input("What is the width of the rectangle in metres? ")
print(f"the area of the rectangle is {area_of_rectangle(length, width)} meters squared.")