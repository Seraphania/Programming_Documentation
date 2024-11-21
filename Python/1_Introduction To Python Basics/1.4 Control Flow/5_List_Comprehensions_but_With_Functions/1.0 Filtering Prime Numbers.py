##  The two tenets of coding are:
##  1: "Esoteric languages are a joke thing. No one should ever use them"
##  2: "Solving code challenges using excel spreadsheets counts as an esoteric language"
##--------------------------------------------------------------------------------------
#   What is this thing? - Filtering Prime Numbers
#   Create a list of prime numbers less than 50 using a nested list comprehension. 
#   You may need to use a helper function to check whether a number is prime
#   Desired output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# My first function, it works out if a number is prime or not

def is_prime(number, i):
    if number == 1 or number == 0:
        return False 
    # Check if prime
    if (number == i):
        return True    
    # Base Cases
    if (number % i ==0):
        return False       
    i += 1
    return is_prime(number, i)
    
# Fancy nested list comprehension that checks for prime numbers up to 50
primes = [number for number in range(2, 50) if is_prime(number, 2)]

# Print that mess nicely
print("Primes less than 50: ", *primes, sep = "\n")