rows = [f"r{x}" for x in range(1, 4)]
columns = [f"c{x}" for x in range(1, 4)]
matrix = [[f"{row}{col}" for col in columns]for row in rows]

print("these are rows",*rows)
print("these are columns",*columns, sep = "\n")
print("this is a matrix made from the columns and rows")
for row in matrix:
    print(*row)


# This is more efficient than just print(*matrix) as it prints each row one at a time
# it's less likely to bugger up formatting, and means less memory load.
#  Let's break down the expression 
#  matrix = [['{}{}'.format(row, column) for column in columns] for row in rows] 
#  into its components:

# Outer List Comprehension (for row in rows):
# "for row in rows": 
# This is the outer loop that iterates over each element (row) in the rows list.

# Inner List Comprehension (for column in columns):
# "for column in columns": 
# This is the inner loop that iterates over each element (column) in the columns list.

# Expression Inside Inner List Comprehension ('{}{}'.format(row, column)):
# "'{}{}'.format(row, column)": 
# This is a string formatting expression using the format method. 
# It combines the current row and column values into a single string. 
# For example, if row is 'r1' and column is 'c1', the result would be 'r1c1'.

# Inner List (['{}{}'.format(row, column) 
# "for column in columns])":
# This is the inner list comprehension. 
# It generates a list of formatted strings for each column in the columns list.

# Outer List ([['{}{}'.format(row, column) for column in columns] for row in rows]):
# This is the outer list comprehension. 
# It generates a list of lists, # where each inner list is the result of the 
#   inner list comprehension for a specific row in the rows list.

# In summary, the entire expression creates a 2D matrix by combining each element 
#   from rows with each element from columns using string formatting. 
# The result is a matrix where each element is a combination of a row and a column.