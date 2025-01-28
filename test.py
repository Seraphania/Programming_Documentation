import sys

def safe_divide(n,d):
    try:
        print(f"{n}/{d} = {n/d}")
    except ValueError:
        print("Please enter a valid number: ")
        sys.exit(1)
    except ZeroDivisionError:
        print("Error: Cannot divide by Zero!")
        d = int(input("Please enter another number: "))
        safe_divide(n,d)
    except:
        print("Something went wrong")
        sys.exit(1)

n = int(input("Please enter a numerator: "))
d = int(input("Please enter a denominator: "))
safe_divide(n,d)

### Does not actually handle ValueError because n/d are cast to ints outide the function. To actually use the `sys.exit(1)` cast to ints before trying the division; or the better option, make a `get_valid_integer()` function.