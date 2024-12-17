# Practice Excercises

## List Comprehensions Practice  
### Problem 1
Create a list comprehension to generate a list of square numbers from 1 to 10.  
**Desired Output:**  
```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
<details>
<summary>Solution Attempt:</summary>  

```py
squares = [i**2 for i in range(1, 11)]
print(squares)
```
</details>

### Problem 2
Generate a list of even numbers from 1 to 20 using a list comprehension.

<details>
<summary>Solution Attempt:</summary>  

```py
evens = [i for i in range(1, 21) if i % 2 == 0]
print(evens)
```
</details>  

### Problem 3
Create a nested list comprehension to generate a multiplication table for numbers 1 to 5. The result should be a list of lists representing the multiplication table.  
Desired output:  
```
[1, 2, 3, 4, 5]
[2, 4, 6, 8, 10]
[3, 6, 9, 12, 15]
[4, 8, 12, 16, 20]
[5, 10, 15, 20, 25]
```

<details>
<summary>Solution Attempt:</summary>  

*Me:*  
 I am having a small issues with Problem3; It is printing all the times tables, from 1-5, not just the single one; can you offer some guidance on where I am going wrong?
```py
table = [f"{j} x {i} = {j*i}" for j in range (1, 6) for i in range(1, 6)]
for row in table:
    print(row)
```

*ChatGPT:*  
Your code for Problem 3 is almost correct, but it seems like you are using an f-string to format each entry in the multiplication table. This results in a flat list of strings when you should be creating a list of lists. Here's a modification to fix this:
```python
table = [[j * i for i in range(1, 6)] for j in range(1, 6)]
for row in table:
    print(row)
```

Now, table is a list of lists, and each row represents a multiplication table for a specific number (1 to 5). The inner list comprehends the product of each number in the range (1 to 5) with the corresponding outer loop value (1 to 5).

*Me:*  
Answer for problem 3 and output:
```py
table = [f"{j} x {i} = {j*i}" for j in range (1, 2) for i in range(1, 6)]
for row in table:
    print(row)
```

```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
```

*ChatGPT:*  
There's a small mistake; You have `range(1, 2)` in the outer loop, which will only execute once. It should be `range(1, 6)` to cover numbers 1 to 5. Here's the corrected version:  
```python
table = [[j * i for i in range(1, 6)] for j in range(1, 6)]
for row in table:
    print(row)
```

With this correction, you should get the full multiplication table from 1 to 5.  
</details>  

___
## Explore Other Iteration Methods
### Problem 4  
Use the `map()` function to square each element in a list of numbers (e.g., `[1, 2, 3, 4]`). Compare this approach with a list comprehension for the same task.

<details>
<summary>Solution Attempt:</summary>  

```py
# Map Version:
def square(n):
    return n**2

numbers = (1, 2, 3, 4)
result = map(square, numbers)
print(list(result))

# List comprehension version:
squares = [i**2 for i in range(1, 5)]
print(squares)
```

*GPT:*  
You can directly use `map()` without defining a separate function. For example:
```python
numbers = [1, 2, 3, 4]
result = map(lambda x: x**2, numbers)
print(list(result))
```

</details>

### Problem 5  
Filter a list of words to include only those with more than 3 characters using the `filter()` function. Try achieving the same result with a list comprehension.  
Here's a list of words to use:
```python
words = ["apple", "banana", "orange", "grape", "strawberry", "kiwi", "blueberry", "watermelon", "pineapple", "mango"]
```

<details>
<summary>Solution Attempt:</summary>  

```py
# Filter version:
def long(n):
    if len(n) > 3:
        return n
    return ""

words = ["apple", "ban", "ape", "strawberry", "kiwi", "pineapple", "mango", "at"]
word = "apple"
long_words = list(filter(long, words))
print(long_words)

# List comprehension version:
l_words = [i for i in words if len(i) > 3]
print(l_words)
```

*GPT:*  
Instead of using an if-else in your long function, you can simplify it by returning the condition directly:
```python
def long(n):
    return n if len(n) > 3 else ""
```

Similarly, you can use a lambda function in `filter()`:
```python
    long_words = list(filter(lambda x: len(x) > 3, words))
```

</details>

### Problem 6 
Explore the `enumerate()` function by iterating over a list and printing both the index and the corresponding element. Understand how it simplifies iteration.
<details>
<summary>Solution Attempt:</summary>  

```py
words = ["apple", "ban", "ape", "strawberry", "kiwi", "pineapple", "mango", "at"]
word = "apple"

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
```

*GPT:*  
When using `enumerate()`, you get tuples of index and value. You can use tuple unpacking in the for loop directly:  
```python
for index, value in enumerate(words):
    print(index, value)
```

</details>

### Problem 7
Use the `zip()` function to combine two lists into pairs. For example, given `[1, 2, 3]` and `['a', 'b', 'c']`, the result should be `[(1, 'a'), (2, 'b'), (3, 'c')]`.
<details>
<summary>Solution Attempt:</summary>  

```py
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = list(zip(numbers, letters))
other_zipped = list(zip(letters, numbers))
print(numbers)
print(letters)
print(zipped)
print(other_zipped)
```
</details>

___



### Pascal's Triangle
*Me:*  
Below is a list of tasks that you have given me, that I have completed, but struggled with. Can you analyze these nd identify what areas I should practice is so that these become easier to me?
```py
Flattening a 2D Matrix
#   Given a 2D matrix (list of lists), 
#   flatten it into a single list using a nested list comprehension.
#   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   Desired output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#   What is this thing? - Transposing a Matrix
#   Given a 2D matrix, transpose it using a nested list comprehension. 
#   The transpose of a matrix is obtained by swapping its rows and columns.
#   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   Desired output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

Generate a matrix
#   Generate a matrix, identifying where the rows and columns are
#   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   Desired output: r1c1 r1c2 r1c3
#                   r2c1 r2c2 r2c3
#                   r3c1 r3c2 r3c3

Given a 2D matrix (list of lists), 
#   Generate a matrix, identifying where the rows and columns are
#   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   Desired output: r1c1 r1c2 r1c3
#                   r2c1 r2c2 r2c3
#                   r3c1 r3c2 r3c3

and this example is currently too difficult for me:
Generating a Pascal's Triangle
#   Generate the first five rows of Pascal's Triangle using a nested list comprehension. 
#   Desired output: 
#        1
#       1 1
#      1 2 1
#     1 3 3 1
#    1 4 6 4 1


```

Could you design a series of tasks for each of the areas below, gradually increasing difficulty in each until I am proficient, and after I am good with each, create challenges that gradually combine them? For each new task please include a brief introduction to the topic, and suggested areas of study?
I may ask for more information, but please give me just enough to point me in the right direction - not solve the problem.

Nested Loops   
String Formatting   
Mathematical Patterns  
Nested Lists and Comprehensions   


## 1 Nested Loops:  
*Introduction:*  
Nested loops involve using one or more loops inside another loop. They are useful for iterating through combinations of elements in nested data structures.

### Task 1: Simple Matrix Print
Print a 3x3 matrix using nested loops.
Suggested Areas of Study: Basic loop syntax and iterating through 2D arrays.

### Task 2: Multiplication Table
Print the multiplication table for numbers 1 to 5 using nested loops.
Suggested Areas of Study: Nested loop logic and arithmetic operations.

### Task 3: Triangular Pattern
Print a triangular pattern using nested loops.
Suggested Areas of Study: Nested loops for patterns and logic.

## 2 String Formatting:
*Introduction:*  
String formatting involves creating formatted strings with placeholders for dynamic values. It helps enhance the visual presentation of information.

### Task 1: Basic String Interpolation
Print a sentence with placeholders for a name and an age.
Suggested Areas of Study: String concatenation and placeholders.

### Task 2: Decimal Precision
Print a floating-point number with a specific number of decimal places.
Suggested Areas of Study: String formatting options for precision.

### Task 3: Table Formatting
Create a table-like format for a list of items using string formatting.
Suggested Areas of Study: Aligning columns and creating visually appealing output.

## 3 Mathematical Patterns:
*Introduction:*  
Mathematical patterns involve creating sequences or structures based on mathematical rules or formulas.

### Task 1: Number Pyramid
Print a pyramid of numbers following a specific pattern.
Suggested Areas of Study: Basic arithmetic patterns.

### Task 2: Fibonacci Sequence
Generate the first 10 numbers in the Fibonacci sequence.
Suggested Areas of Study: Understanding and implementing the Fibonacci sequence.

### Task 3: Prime Numbers
Print the first 15 prime numbers.
Suggested Areas of Study: Implementing algorithms for prime number generation.

## 4 Nested Lists and Comprehensions:

*Introduction:*  
Nested lists and comprehensions involve creating and manipulating lists within lists using concise syntax.

### Task 1: Flattening a Matrix
Write a function to flatten a 2D matrix into a single list using nested comprehensions.
Suggested Areas of Study: Understanding list comprehensions and nested structures.

### Task 2: Transposing a Matrix
Write a function to transpose a 2D matrix using nested comprehensions.
Suggested Areas of Study: Working with nested structures and comprehension logic.

### Task 3: Filtering a Matrix
Filter a matrix to include only even numbers using nested comprehensions.
Suggested Areas of Study: Conditional comprehensions and filtering.

## Combining Tasks:

## Task 1: Matrix Formatting
Generate a matrix and print it with proper formatting, combining nested loops, string formatting, and nested lists.
Suggested Areas of Study: Combining concepts from nested loops, string formatting, and nested lists.

## Task 2: Pattern with Data
Create a pattern based on prime numbers and print it with proper formatting, combining mathematical patterns and string formatting.
Suggested Areas of Study: Integrating patterns with data and formatting.

## Task 3: Advanced Matrix Operations
Perform advanced operations on a matrix, combining nested loops, mathematical patterns, and nested lists.
Suggested Areas of Study: Advanced matrix manipulations and nested comprehensions.

**Remember to gradually increase the complexity of each task and feel free to experiment with variations based on your understanding.**


