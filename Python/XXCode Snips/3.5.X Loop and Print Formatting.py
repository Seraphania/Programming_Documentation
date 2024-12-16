## Loops

# Request input (and check it's an integer)
while True:
    try:
        number = int(input("How many items are in this list? "))
        break
    except ValueError:
        print("Please enter an integer: ")
        
counter = 1
items = []

# Ask for the list items as many times as specified
while counter <= number:
    new_item = input(f"Please enter item number {counter}: ")
 # Keep track of the list items
    items.append(new_item)
    counter += 1
    
#Print the item list in reverse order
items.reverse()
print("Your list in reverse is ", *items, sep = "\n")


# printing the list using * operator separated by comma 
#print(*items)
 
# printing the list using * and sep operator
# print("printing lists separated by commas")
 
# print(*items, sep = ", ") 
 
# print in new line
# print("printing lists in new line")
 
# print(*items, sep = "\n")