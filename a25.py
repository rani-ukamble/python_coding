# Assignment 25:

# Write a python function,check_double(number) which accepts a whole number and returns True if it satisfies the given 

# conditions.
# 1. The number and its double should have exactly the same number of digits.
# 2. Both the numbers should have the same digits ,but in different order.
# Otherwise it should return False.
# Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.

 
def check_double(n):
    l = []
    n1 = 2*n 
    n1 = str(n1)
    n = str(n) 
    for i in n1:
        l.append(i)
    for i in n:
        if i not in l:
            return False
    else:
        return True

        
print(check_double(125874))   