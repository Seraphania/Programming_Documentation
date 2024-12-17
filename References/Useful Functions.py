# Function to trannspose matrix
def new_func(trasnp_matrix):
    transp_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transp_matrix

transp_matrix = new_func(matrix) 
print("Here's the matrix: ", *transp_matrix, sep = "\n")

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
