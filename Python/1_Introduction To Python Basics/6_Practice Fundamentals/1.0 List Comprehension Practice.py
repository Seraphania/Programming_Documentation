##  The two tenets of coding are:
##  1: "Esoteric languages are a joke thing. No one should ever use them"
##  2: "Solving code challenges using excel spreadsheets counts as an esoteric language"
##--------------------------------------------------------------------------------------
#   What is this thing? - Practice fundamentals to make sure I know them
# Part 1: list comprehension practice
# Problem 1.1:
# Create a list comprehension to generate a list of square numbers from 1 to 10.
squares = [i**2 for i in range(1, 11)]
print(squares)

# Problem 1.2:
# Generate a list of even numbers from 1 to 20 using a list comprehension.
evens = [i for i in range(1, 21) if i % 2 == 0]
print(evens)

# Problem 1.3:
# Create a nested list comprehension to generate a multiplication table for numbers 1 to 5. 
# The result should be a list of lists representing the multiplication table.
table = [f"{j} x {i} = {j*i}" for j in range (1, 2) for i in range(1, 6)] # Not the desired output apparently, but nice all the same.
for row in table:
    print(row)

other_table = [[j * i for i in range(1, 6)] for j in range(1, 6)]
for row in other_table:
    print(row)
    
# Part 2: Explore Other Iteration Methods:
# Problem 2.1:
# Use the map() function to square each element in a list of numbers (e.g., [1, 2, 3, 4]). 
# Compare this approach with a list comprehension for the same task.
def square(n):
    return n**2

numbers = (1, 2, 3, 4)
result = map(square, numbers)
print(list(result))
#Can map without the seperate function:
result = map(lambda x: x**2, numbers)
print(list(result))
# List comprehension version
squares = [i**2 for i in range(1, 5)]
print(squares)

# Problem 2.2:
# Filter a list of words to include only those with more than 3 characters using the filter() function. 
# Try achieving the same result with a list comprehension.
def long(n):
    if len(n) > 3:
        return n
    return ""
# Could also do:
# def long(n):
#     return n if len(n) > 3 else ""

words = ["apple", "ban", "ape", "strawberry", "kiwi", "pineapple", "mango", "at"]
word = "apple"
long_words = list(filter(long, words))
# Or could do:
# long_words = list(filter(lambda x: len(x) > 3, words))
print(long_words)

# List comprehension version:
l_words = [i for i in words if len(i) > 3]
print(l_words)

# Problem 2.3:
# Explore the enumerate() function by iterating over a list and printing both the index and the corresponding element. 
# Understand how it simplifies iteration.
# Syntax: enumerate(iterable, start=0)
print(list(enumerate(words)))
print(list(enumerate(word)))

    
# printing the tuples in object directly
for ele in enumerate(word):
    print (ele)
 
# changing index and printing separately
for count, ele in enumerate(word, 100):
    print (count, ele)
 
# getting desired output from tuple
for count, ele in enumerate(word):
    print(count)
    print(ele)
    
# Can do this:
for index, value in enumerate(words):
    print(index, value)

# Problem 2.3:
# Use the zip() function to combine two lists into pairs. 
# For example, given [1, 2, 3] and ['a', 'b', 'c'], 
# the result should be [(1, 'a'), (2, 'b'), (3, 'c')].
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = list(zip(numbers, letters))
other_zipped = list(zip(letters, numbers))
print(numbers)
print(letters)
print(zipped)
print(other_zipped)