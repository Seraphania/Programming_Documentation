##  Ye Olde FizzBuzz

# Ask a user how many numbers to input
counter = 1

while True:
    try:
        total = int(input("How high do you want to get? (enter a number to count to) "))
        break  # Break out of the loop if input is successfully converted to an integer
    except ValueError:
        print("Please enter an integer.")

while counter <= total:
    if counter %3 == 0 and counter %5 == 0:
        print("FizzBuzz!")
        
    elif counter %3 ==0:
        print("Fizz")
        
    elif counter %5 ==0:
        print("Buzz")     

    else: 
        print(counter)    
    counter += 1

