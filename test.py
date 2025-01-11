import random as rand
even = []
odd = []

try:
    length = int(input("Please enter a number of variables: "))
except:
    print("No whole number entered, defaulting to 10")
    length = 11

if length > 100:
    print("that's a stupid number, I'm dong 100!")
    length = 101
elif length < 0:
    print("that's a stupid number, I'm dong 100!")
    length = 101

for i in range(1, length):
    num = rand.randint(1, 100)
    if num %2 == 0:
        even.append(num)
    else:
        odd.append(num)
    i += 1

print(f"Even numbers are: \n{even}")
print(f"Odd numbers are: \n{odd}")