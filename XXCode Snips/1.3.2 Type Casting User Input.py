## User input and Conditionals

# Request user's age
age = int(input ("What is your age? "))

# Use if Stetement to parse number and print a response
if age <= 17:   
    print ("No Booze for you!")
    
elif age <= 65:
    print ("Drink up while you can!")

else:
    print ("You're over the hill - you can still drink though!")
