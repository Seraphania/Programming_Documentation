## Loops

# Request input (and check it's an integer)
number = float(input("Please enter a number: "))
counter = 1
#product = number + counter
while counter <= 12:
    #I'm doing 12 times table!
    result = counter * number
    
     # Check if the result is a whole number
    if result.is_integer():
        # If it's a whole number, convert to int before printing
        print(int(counter), "x", int(number), "=", int(result))
    else:
        # If it's not a whole number, print with decimal places
        print(int(counter), "x", number, "=", result)

    counter += 1

#Key point of While Loop:

#    A while loop repeatedly executes a block of code as long as a given condition is true.
#    It does not have a fixed number of iterations but continues executing until the condition becomes false.
#    The condition is checked before each iteration, and if it's false initially, the code block is skipped entirely.
#    The condition is typically based on a variable or expression that can change during the execution of the loop.
#    It provides more flexibility in terms of controlling the loop's execution based on dynamic conditions.

#Key point of For Loop:

#    A for loop iterates over a sequence (such as a list, string, or range) or any object that supports iteration.
#    It has a predefined number of iterations based on the length of the sequence or the number of items to iterate over.
#    It automatically handles the iteration and does not require maintaining a separate variable for tracking the iteration count.
#    It simplifies the code by encapsulating the iteration logic within the loop itself.
#    It is commonly used when you know the exact number of iterations or need to iterate over each item in a collection.

