# Assignment 42:

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# Write a python program to find and display the number of circular primes less than the given limit.



def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)):
        while n%i==0:
            return False
        return True
        
def getRotations(num):
    r = []
    for i in range(len(num)):
        rot = num[i:]+num[:i]
        r.append(int(rot))
    return r

def is_circular_prime(num):
    rotList = getRotations(num)
    return all(isPrime(item) for item in rotList)


print(is_circular_prime("971"))
