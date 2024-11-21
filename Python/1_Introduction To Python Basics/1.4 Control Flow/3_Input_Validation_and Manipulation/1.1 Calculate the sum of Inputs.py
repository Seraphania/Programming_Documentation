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