# Assignment 29:

# Given a number n, write a program to find the sum of the largest prime factors of each of nine consecutive numbers starting from n.

# g(n) = f(n) + f(n+1) + f(n+2) + f(n+3) + f(n+4) + f(n+5) + f(n+6) + f(n+7) + f(n+8)
# where, g(n) is the sum and f(n) is the largest prime factor of n
# For example,
# g(10)=f(10)+f(11)+f(12)+f(13)+f(14)+f(15)+f(16)+f(17)+f(18)
#  =5 + 11 + 3 + 13 + 7 + 5 + 2 + 17 + 3
#  =66



def largest_factor(n):
    if n<2:
        return None
    
    while n%2==0:
        largest = 2
        n//=2

    for i in range(3, int(n**0.5) + 1, 2):
        while n%i==0:
            largest = i
            n//=i

    if n>2:
        largest = n
    
    return largest

def sum_largest_prime_factors(n):
    curr_sum = 0
    for i in range(n , n+9):
        curr_sum += largest_factor(i)
    return curr_sum
       
print(sum_largest_prime_factors(10))
 
    

    
