## Even or odd

while True:
    try:
        number = int(input("Please enter a number: "))
        break  # Break out of the loop if input is successfully converted to an integer
    except ValueError:
        print("Please enter an integer.")

# Check if Zero
if number == 0:
    print("0 is neither odd nor even")
# Check if odd
elif number % 2 != 0:
    print(number, "is an odd number")
# Check if even
else:
    print(number, "is an even number")