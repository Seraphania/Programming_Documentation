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