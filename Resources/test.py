a = 1

try:
    b = int(input("Please enter a number to divide a: "))
    a = a/b
    print("Success 1/", b ,"=",a)
except:
    print("There was an error")