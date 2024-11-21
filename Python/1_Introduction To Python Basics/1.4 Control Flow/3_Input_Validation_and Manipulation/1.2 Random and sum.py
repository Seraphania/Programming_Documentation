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
