## Loops

# Request input
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