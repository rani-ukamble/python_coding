# Assignment 38:

# Consider sample data as follows: sample_data=range(1,11)
# Create two functions: odd() and even()
# The function even() returns a list of all the even numbers from sample_data
# The function odd() returns a list of all the odd numbers from sample_data
# Create a function sum_of_numbers() which will accept the sample data and/or a function.
# If a function is not passed, the sum_of_numbers() should return the sum of all the numbers from sample_data
# If a function is passed, the sum_of_numbers() should return the sum of numbers returned from the function passed.

def odd(a, b):
    odd = [num for num in range(a, b+1) if num%2==1]
    return odd

def even(a, b):
    even = [num for num in range(a, b+1) if num%2==0]
    return even

def sum_of_numbers(a, b):
    l = [num for num in range(a,b+1)]
    
    print("1: Pass Even Function ")
    print("2: Pass Odd Function ")
    print("3: Don't Pass any Function ")

    choice = int(input("Enter choice : "))

    if choice ==1:
        return sum(even(a,b))
    elif choice==2:
        return sum(odd(a,b))
    else:
        return sum(l)



if __name__ == "__main__":
    a, b = 1, 11
    res = sum_of_numbers(a, b)
    print(res)