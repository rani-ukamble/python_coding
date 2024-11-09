# Assignment 23:
# Write a python function,create_largest_number(), which accepts a list of numbers and returns the largest number 
# possible by concatenating the list of numbers.
# Note: Assume that all the numbers are two digit numbers.
# Also write the pytest test cases to test the program.

# Sample Input 
# 23,34,55 
# Expected Output
# 553423

def create_largest_number(a, b, c):
    a = str(a)
    b = str(b)
    c = str(c)
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    l.sort(reverse=True)
    res = ''.join(l)
    return int(res)

if __name__ == "__main__":
    a, b, c = 23,34,55
    print(create_largest_number(a,b,c))

