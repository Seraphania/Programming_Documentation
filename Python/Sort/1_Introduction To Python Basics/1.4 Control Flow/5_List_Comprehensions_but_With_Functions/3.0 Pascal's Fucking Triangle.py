##  The two tenets of coding are:
##  1: "Esoteric languages are a joke thing. No one should ever use them"
##  2: "Solving code challenges using excel spreadsheets counts as an esoteric language"
##--------------------------------------------------------------------------------------
#   What is this thing? - Generating a Pascal's Triangle
#   Generate the first five rows of Pascal's Triangle using a nested list comprehension. 
#   Desired output: 
#        1
#       1 1
#      1 2 1
#     1 3 3 1
#    1 4 6 4 1

# My manky attempt
def get_positive_integer(prompt):
    while True:
        try:
           num = int(input(prompt))
           if num > 0:
                return num
        except ValueError:
            print("please enter a positive number: ")
            
rows = get_positive_integer("How many rows do you want?: ")    
triangle = ["1"]
counter = 0
while counter < rows:
    current_row = triangle[-1]
    new_row = [1]
    for i in range(len(current_row) -1):
        ele = current_row[i] + current_row[i+1]
        new_row.append(ele)
        
    new_row.append(1)
    triangle.append(new_row)
    counter += 1 

# Stole this a bit really.    
last_row = triangle[-1]
number_width = len(str(max(last_row))) + 1
triangle_width = number_width * len(last_row)

for row in triangle:
    string = ""

    for number in row:
        number_string = str(number)
        string += number_string + ' ' * (number_width - len(number_string))

    print(string.center(triangle_width))
    
#######################################   
# Michael's version (more or less)
def get_positive_integer(prompt):
    while True:
        try:
           num = int(input(prompt))
           if num > 0:
                return num
        except ValueError:
            print("please enter a positive number")
            
print("\ntask 4.2: generate and print the first 10 rows of pascal's triangle using nested loops.")
rows = get_positive_integer("How many rows do you want?: ")
triangle = ["1"]
i = 0
while i < rows:
     last_line = triangle[i].split()
     j = 0
     new_line = "1"
     while j < len(last_line) - 1:
        ele = int(last_line[j]) + int(last_line[j+1])
        new_line = new_line + " " + str(ele)
        j += 1
     new_line = new_line + " 1"
     triangle.append(new_line)
     i += 1
     
last_row = len(triangle[-1])
for row in triangle:
        print(row.center(last_row))