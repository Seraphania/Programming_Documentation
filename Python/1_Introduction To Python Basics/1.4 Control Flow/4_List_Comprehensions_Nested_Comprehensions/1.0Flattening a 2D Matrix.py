##  The two tenets of coding are:
##  1: "Esoteric languages are a joke thing. No one should ever use them"
##  2: "Solving code challenges using excel spreadsheets counts as an esoteric language"
##--------------------------------------------------------------------------------------
#   What is this thing? - Flattening a 2D Matrix
#   Given a 2D matrix (list of lists), 
#   flatten it into a single list using a nested list comprehension.
#   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   Desired output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Let the user decide how big the matrix should be
# while True:
#     try:
#         rows = int(input("Enter number of rows for the Matrix? "))
#         break
#     except ValueError:
#         print("Numbers must be integers.")
  
# while True:
#     try:
#         columns = int(input("Enter number of columns for the Matrix? "))
#         break
#     except ValueError:
#         print("Numbers must be integers.")
        
# # Generate a sequential matrix that increments by 1 left to right, top to bottom and print it.
# items = list(range(1, rows*columns+1)) #This line generates a list (items) containing sequential numbers starting from 1 up to the product of rows and columns (inclusive). It uses the range() function to create a range of numbers and then converts it to a list.
# matrix = [items[i:i+rows] for i in range(0, len(items), rows)] #This line creates a 2D matrix from the sequential items. It uses a list comprehension to iterate over the items list, taking slices of rows elements at a time. The loop variable i starts from 0 and increments by rows in each iteration, creating rows of the matrix.
# print("Here's the matrix: ", *matrix, sep = "\n") #This line prints the matrix with a nice format. The *matrix syntax is used to unpack the elements of the matrix as separate arguments to the print() function. The sep="\n" argument sets the separator between items to a newline character, creating a visual representation of rows.

# # Iron the matrix nice and flat
# flat_matrix = [item for row in matrix for item in row] # This line uses a nested list comprehension to flatten the 2D matrix into a single list (flat_matrix). It iterates over each row in the matrix (for row in matrix), then iterates over each item in the row (for item in row), appending each item to the flattened list.

# # Print the ironed matrix 
# print("Here is the stringy version: ", *flat_matrix)


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