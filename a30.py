# from math import prod

# # Extended list of prime numbers to use for factorizing
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# def find_smallest_number(n):
#     # Check if input is a valid positive integer
#     if not isinstance(n, int) or n <= 0:
#         return "Input must be a positive integer."

#     # To store the smallest number found
#     smallest_number = float('inf')

#     # We will find combinations of exponents that yield exactly n divisors
#     def backtrack(current_divisors, current_product, exponent_index):
#         nonlocal smallest_number
        
#         # If we've formed a valid product with the required number of divisors
#         if current_divisors == n:
#             smallest_number = min(smallest_number, current_product)
#             return
        
#         # If the product exceeds the limit or if we exceed the divisor count, stop
#         if current_divisors > n or exponent_index >= len(primes):
#             return

#         # Try different exponents for the current prime
#         for exponent in range(1, n + 1):
#             new_product = current_product * (primes[exponent_index] ** (exponent - 1))
#             new_divisors = current_divisors * exponent
            
#             # Backtrack with the new product and updated divisor count
#             backtrack(new_divisors, new_product, exponent_index + 1)

#     # Start backtracking with the first prime and initial values
#     backtrack(1, 1, 0)

#     return smallest_number if smallest_number != float('inf') else "Error: Cannot find the smallest number for this divisor count due to prime list limitation."

# # Test the function
# print(find_smallest_number(3))  # Expected output: 120
