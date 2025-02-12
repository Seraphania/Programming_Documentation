##  The two tenets of coding are:
##  1: "Esoteric languages are a joke thing. No one should ever use them"
##  2: "Solving code challenges using excel spreadsheets counts as an esoteric language"
##--------------------------------------------------------------------------------------
#   What is this thing? - Flattening a 2D Matrix
#   Given a 2D matrix (list of lists), 
#   flatten it into a single list using a nested list comprehension.
#   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   Desired output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Let the user decide how big the matrix should be
while True:
    try:
        rows = int(input("Enter number of rows for the Matrix? "))
        break
    except ValueError:
        print("Numbers must be integers.")
  
while True:
    try:
        columns = int(input("Enter number of columns for the Matrix? "))
        break
    except ValueError:
        print("Numbers must be integers.")
        
## Generate a sequential matrix that increments by 1 left to right, top to bottom and print it.
# This line generates a list (items) containing sequential numbers 
# starting from 1 up to the product of rows and columns (inclusive). 
# It uses the range() function to create a range of numbers and then converts it to a list.
items = list(range(1, rows*columns+1)) 

#This line creates a 2D matrix from the sequential items. 
# It uses a list comprehension to iterate over the items list, 
# taking slices of rows elements at a time. 
# The loop variable i starts from 0 and increments by rows in each iteration, 
# creating rows of the matrix.
matrix = [items[i:i+rows] for i in range(0, len(items), rows)] 

#This line prints the matrix with a nice format. 
# The *matrix syntax is used to unpack the elements of the 
# matrix as separate arguments to the print() function. 
# The sep="\n" argument sets the separator between items 
# to a newline character, creating a visual representation of rows.
print("Here's the matrix: ", *matrix, sep = "\n") 

## Iron the matrix nice and flat

# This line uses a nested list comprehension to flatten the 2D matrix
# into a single list (flat_matrix). It iterates over each row 
# in the matrix (`for row in matrix`), then iterates over each item in the row 
# (`for item in row`), appending each item to the flattened list.
flat_matrix = [item for row in matrix for item in row] 

# Print the ironed matrix 
print("Here is the stringy version: ", *flat_matrix)

input("Press the anykey to continue...")

###########################################
# Improved version from Chat GPT with functions
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

def generate_matrix(rows, columns):
    items = list(range(1, rows * columns + 1))
    return [items[i:i + columns] for i in range(0, len(items), columns)]

def flatten_matrix(matrix):
    return [item for row in matrix for item in row]

# Let the user decide how big the matrix should be
rows = get_positive_integer("Enter number of rows for the Matrix: ")
columns = get_positive_integer("Enter number of columns for the Matrix: ")

# Generate and print the matrix
matrix = generate_matrix(rows, columns)
print("Here's the matrix:")
for row in matrix:
    print(row)

# Iron the matrix nice and flat
flat_matrix = flatten_matrix(matrix)

# Print the ironed matrix 
print("Here is the stringy version:", *flat_matrix)

input("Press the anykey to continue...")

###########################################
##  The two tenets of coding are:
##  1: "Esoteric languages are a joke thing. No one should ever use them"
##  2: "Solving code challenges using excel spreadsheets counts as an esoteric language"
##--------------------------------------------------------------------------------------
#   What is this thing? - Transposing a Matrix
#   Given a 2D matrix, transpose it using a nested list comprehension. 
#   The transpose of a matrix is obtained by swapping its rows and columns.
#   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   Desired output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Function for getting positive integers from a user
def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num  
                break
            else:
                print("Please enter a positive integer. ")
        except ValueError:
            print("Please enter a valid integer. ")
        


# Let the user decide how big the matrix should be (taken from task 7)  
rows = get_positive_integer("Enter number of rows for the Matrix: ")        
columns = get_positive_integer("Enter number of columns for the Matrix: ")        
        
      
# Generate a sequential matrix that increments by 1 left to right, top to bottom and print it.
items = list(range(1, rows*columns+1)) 
matrix = [items[i:i+rows] for i in range(0, len(items), rows)] 
print("Here's the matrix: ", *matrix, sep = "\n")

# Transpose the matrix so that the rows and columns are swapped

transp_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))] 
print("Here's the matrix: ", *transp_matrix, sep = "\n")

input("Press the anykey to continue...")

###########################################
##  The two tenets of coding are:
##  1: "Esoteric languages are a joke thing. No one should ever use them"
##  2: "Solving code challenges using excel spreadsheets counts as an esoteric language"
##--------------------------------------------------------------------------------------
#   What is this thing? - Generate a matrix
#   Generate a matrix, identifying where the rows and columns are
#   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   Desired output: r1c1 r1c2 r1c3
#                   r2c1 r2c2 r2c3
#                   r3c1 r3c2 r3c3

# Generate rows 3 rows, r1, r2, r3 - uses fstrings to append "r" to the generated row no.
rows = [f"r{x}" for x in range(1, 4)]
# same as above but for columns and "c"
columns = [f"c{x}" for x in range(1, 4)]
# Iterates over each item in each "rows" and "columns", concatenating each using fstrings. 
# Behold the dynamically created variables "row" and "col"!
# This fucked up the first time because I was concatenating the entire "rows" and "columns"
#   instead of the idividual elements from "rows" and "columns"
#   Those are pulled with the variables "col" and "row"
matrix = [[f"{row}{col}" for col in columns]for row in rows]

print("these are rows",*rows)
print("these are columns",*columns, sep = "\n")
print("this is a matrix made from the columns and rows")
# This is better than "print(*matrix, sep = "\n")" as it prints each row one at a time
# it's less likely to bugger up formatting, and means less memory load.
for row in matrix:
    print(*row)


#################################
##  The two tenets of coding are:
##  1: "Esoteric languages are a joke thing. No one should ever use them"
##  2: "Solving code challenges using excel spreadsheets counts as an esoteric language"
##--------------------------------------------------------------------------------------
#   What is this thing? - Given a 2D matrix (list of lists), 
#   Generate a matrix, identifying where the rows and columns are
#   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   Desired output: r1c1 r1c2 r1c3
#                   r2c1 r2c2 r2c3
#                   r3c1 r3c2 r3c3

# Lets do it again, except this time let the number of rows and columns come from the user:

# Function for getting positive integers from a user
def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num  
                break
            else:
                print("please enter a positive integer. ")
        except ValueError:
            print("please enter a valid integer. ")
 
# Let the user decide how big the matrix should be (taken from task 7)  
rows = get_positive_integer("enter number of rows for the matrix: ")     
columns = get_positive_integer("enter number of columns for the matrix: ")
        
# Generate the rows and columns with a prefix in front of each number  
rrows = [f"r{x}" for x in range(1, rows+1)]
ccolumns = [f"c{x}" for x in range(1, columns+1)]

# Build the damn matrix
matrix = [[f"{row}{col}" for col in ccolumns]for row in rrows]

# And print the silly thing
for row in matrix:
    print(*row)

input("Press the anykey to continue...")

###########################################
##  The two tenets of coding are:
##  1: "Esoteric languages are a joke thing. No one should ever use them"
##  2: "Solving code challenges using excel spreadsheets counts as an esoteric language"
##--------------------------------------------------------------------------------------
#   What is this thing? - Filtering Prime Numbers
#   Create a list of prime numbers less than 50 using a nested list comprehension. 
#   You may need to use a helper function to check whether a number is prime
#   Desired output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# My first function, it works out if a number is prime or not
def is_prime(number, i):
    if number == 1 or number == 0:
        return False 
    # Check if prime
    if (number == i):
        return True    
    # Base Cases
    if (number % i ==0):
        return False       
    i += 1
    return is_prime(number, i)
    
# Fancy nested list comprehension that checks for prime numbers up to 50
primes = [number for number in range(2, 50) if is_prime(number, 2)]

# Print that mess nicely
print("Primes less than 50: ", *primes, sep = "\n")

input("Press the anykey to continue...")