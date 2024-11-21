## User input and Conditionals

# Request user's age
age = input ("What is your age? ")

# Convert age to integer
int_age = int(age)

# Use if Stetement to parse number and print a response
if int_age <= 17:   
    print ("No Booze for you!")
    
elif int_age <= 65:
    print ("Drink up while you can!")

else:
    print ("You're over the hill - you can still drink though!")
