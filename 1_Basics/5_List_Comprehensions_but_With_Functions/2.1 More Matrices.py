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