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
