# Assignment 32:

# The below function is written to check whether a given three digit number is an Armstrong number.
# Hint: An “Armstrong number” is an n-digit number that is equal to the sum of the nth powers of its individual digits.
# Example: 371 is an Armstrong number as 371 = 3^3 +7^3+ 1^3
# But the function is having errors/bugs, debug the program using the Eclipse debugger and correct it

def is_armstrog(n):
    n1 = n
    sum = 0
    while n1>0:
        rem = n1%10
        sum+=rem**3
        n1//=10 
    if n == sum:
        return True


if __name__ == "__main__":
    n = 371
    print(is_armstrog(n))

